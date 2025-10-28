#!/usr/bin/env python3
"""
Smart Energy Efficiency System - Main Entry Point
Integrated system with camera detection, temperature monitoring, and Flask dashboard
"""

import os
import sys
import time
from datetime import datetime

class DetectionLogger:
    """Log detection events to file for project reporting"""
    
    def __init__(self, log_file="detection_log.txt"):
        self.log_file = log_file
        self.ensure_log_file()
    
    def ensure_log_file(self):
        """Create log file with header if it doesn't exist"""
        if not os.path.exists(self.log_file) or os.path.getsize(self.log_file) == 0:
            with open(self.log_file, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write("SMART ENERGY EFFICIENCY SYSTEM - DETECTION LOG\n")
                f.write("=" * 80 + "\n")
                f.write(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 80 + "\n\n")
    
    def log_event(self, event_type, message, fan_status=None):
        """Log an event with timestamp"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {event_type}: {message}"
        
        if fan_status is not None:
            log_entry += f" → Fan: {fan_status}"
        
        log_entry += "\n"
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        
        print(f"📝 Logged: {event_type} - {message}")
    
    def log_summary(self, total_detections, total_fan_on_time, energy_saved):
        """Add summary statistics to log"""
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write("\n" + "=" * 80 + "\n")
            f.write("SESSION SUMMARY\n")
            f.write("=" * 80 + "\n")
            f.write(f"Total Detections: {total_detections}\n")
            f.write(f"Fan ON Time: {total_fan_on_time} minutes\n")
            f.write(f"Energy Saved (estimated): {energy_saved:.2f} kWh\n")
            f.write("=" * 80 + "\n\n")

def print_banner():
    """Print welcome banner"""
    print("\n" + "=" * 60)
    print(" "*10 + "⚡ SMART ENERGY EFFICIENCY SYSTEM ⚡")
    print("=" * 60)
    print("\n🎯 ML-Powered Energy Management with Object Detection")
    print("📊 Real-time Monitoring & Intelligent Automation\n")

def print_menu():
    """Print main menu options"""
    print("=" * 60)
    print("SELECT OPERATION MODE:")
    print("=" * 60)
    print("1. 🎥 Human Detection (Camera) Only")
    print("2. 🌡️ Temperature + Human Detection (Combined)")
    print("3. 🌐 Live Flask Dashboard (Web Interface)")
    print("4. 🖥️  Streamlit Smart Dashboard (Advanced UI)")
    print("5. 📊 View Detection Logs")
    print("6. ❌ Exit")
    print("=" * 60)
    print()

def run_human_detection(logger):
    """Run option 1: Camera-based human detection only"""
    print("\n🎥 Starting Human Detection Mode...")
    print("Press 'Q' to quit and return to menu\n")
    logger.log_event("SYSTEM", "Started Human Detection mode")
    
    try:
        import cv2
        import torch
        
        print("⏳ Loading YOLO model...")
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        logger.log_event("MODEL", "YOLO model loaded successfully")
        
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            print("❌ Error: Could not open camera")
            logger.log_event("ERROR", "Camera initialization failed")
            return
        
        logger.log_event("CAMERA", "Camera opened successfully")
        print("✅ Camera initialized\n")
        
        fan_controller = None
        try:
            from fan_controller import FanController
            from utils import load_config
            config = load_config("config.yaml")
            fan_controller = FanController(config["gpio_pin"], config["off_delay"])
            print("✅ Fan controller initialized\n")
        except ImportError:
            print("⚠️ Fan controller not available (using simulation mode)\n")
        
        print("🔍 Detection Active - Press 'Q' to quit\n")
        detection_count = 0
        
        while True:
            ret, frame = camera.read()
            if not ret:
                break
            
            # Run detection
            results = model(frame)
            detections = results.pandas().xyxy[0]
            
            # Check for human detection
            human_detected = any(d['name'] == 'person' for _, d in detections.iterrows())
            
            if human_detected:
                detection_count += 1
                if fan_controller:
                    fan_controller.turn_on()
                    fan_controller.update_last_seen()
                    logger.log_event("DETECTION", f"Human detected (#{detection_count})", "ON")
                else:
                    logger.log_event("DETECTION", f"Human detected (#{detection_count}) - (Simulated)", "ON")
                print(f"👤 Human Detected! (#{detection_count}) - Fan: ON")
            else:
                if fan_controller:
                    fan_controller.turn_off()
                    logger.log_event("IDLE", "No human detected", "OFF")
            
            # Display frame
            cv2.imshow("Smart Energy System - Human Detection", results.render()[0])
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("\n⏹️  Stopping detection...")
                break
        
        camera.release()
        cv2.destroyAllWindows()
        
        logger.log_event("SYSTEM", f"Human Detection mode ended. Total detections: {detection_count}")
        print(f"\n✅ Session complete! Total detections: {detection_count}")
        
    except ImportError as e:
        print(f"\n❌ Error: Missing dependencies. Install: {e}")
        logger.log_event("ERROR", f"Import error: {str(e)}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        logger.log_event("ERROR", f"Unexpected error: {str(e)}")

def run_combined_mode(logger):
    """Run option 2: Temperature + Human Detection"""
    print("\n🌡️ Starting Combined Detection Mode...")
    print("Press 'Q' to quit and return to menu\n")
    logger.log_event("SYSTEM", "Started Combined Detection mode (Temperature + Camera)")
    
    try:
        import cv2
        import torch
        from temp_sensor import TemperatureSensor
        from fan_controller import FanController
        from utils import load_config
        
        print("⏳ Loading YOLO model...")
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        
        config = load_config("config.yaml")
        temp_sensor = TemperatureSensor(config["temp_threshold"])
        fan = FanController(config["gpio_pin"], config["off_delay"])
        
        logger.log_event("MODEL", "YOLO model and sensors loaded successfully")
        
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            print("❌ Error: Could not open camera")
            logger.log_event("ERROR", "Camera initialization failed")
            return
        
        print("✅ Camera and sensors initialized\n")
        logger.log_event("CAMERA", "Camera opened successfully")
        
        print("🔍 Detection Active - Press 'Q' to quit\n")
        detection_count = 0
        
        while True:
            ret, frame = camera.read()
            if not ret:
                break
            
            # Read temperature
            current_temp = temp_sensor.read_temp()
            
            # Run detection
            results = model(frame)
            detections = results.pandas().xyxy[0]
            human_detected = any(d['name'] == 'person' for _, d in detections.iterrows())
            
            # Logic: Fan ON if human detected AND temperature above threshold
            if human_detected and current_temp > config["temp_threshold"]:
                detection_count += 1
                fan.turn_on()
                fan.update_last_seen()
                logger.log_event("DETECTION", 
                    f"Human detected (#{detection_count}) at {current_temp:.1f}°C (above {config['temp_threshold']}°C)", 
                    "ON")
                print(f"👤 Human Detected! 🌡️ Temp: {current_temp:.1f}°C - Fan: ON")
            else:
                if not human_detected:
                    fan.turn_off()
                    logger.log_event("IDLE", "No human detected", "OFF")
                elif current_temp <= config["temp_threshold"]:
                    fan.turn_off()
                    logger.log_event("TEMP", f"Temp {current_temp:.1f}°C below threshold", "OFF")
            
            # Display frame with temperature
            display_text = f"Temp: {current_temp:.1f}°C | Threshold: {config['temp_threshold']}°C"
            cv2.putText(results.render()[0], display_text, (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.imshow("Smart Energy System - Combined Detection", results.render()[0])
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("\n⏹️  Stopping detection...")
                break
        
        camera.release()
        cv2.destroyAllWindows()
        
        logger.log_event("SYSTEM", f"Combined Detection mode ended. Total detections: {detection_count}")
        print(f"\n✅ Session complete! Total detections: {detection_count}")
        
    except ImportError as e:
        print(f"\n❌ Error: Missing dependencies. Install: {e}")
        logger.log_event("ERROR", f"Import error: {str(e)}")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        logger.log_event("ERROR", f"Unexpected error: {str(e)}")

def run_flask_dashboard(logger):
    """Run option 3: Flask dashboard"""
    print("\n🌐 Starting Flask Dashboard...")
    logger.log_event("SYSTEM", "Starting Flask dashboard server")
    
    try:
        import subprocess
        print("🚀 Launching Flask web server on http://localhost:5000")
        print("Press Ctrl+C to stop and return to menu\n")
        
        subprocess.run([sys.executable, "app_flask.py"])
        
    except KeyboardInterrupt:
        print("\n⏹️  Flask dashboard stopped")
        logger.log_event("SYSTEM", "Flask dashboard stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        logger.log_event("ERROR", f"Flask dashboard error: {str(e)}")

def run_streamlit_dashboard(logger):
    """Run option 4: Streamlit dashboard"""
    print("\n🖥️  Starting Streamlit Dashboard...")
    logger.log_event("SYSTEM", "Starting Streamlit dashboard server")
    
    try:
        import subprocess
        print("🚀 Launching Streamlit web server on http://localhost:8501")
        print("Press Ctrl+C to stop and return to menu\n")
        
        subprocess.run([sys.executable, "-m", "streamlit", "run", "smart_energy_app.py"])
        
    except KeyboardInterrupt:
        print("\n⏹️  Streamlit dashboard stopped")
        logger.log_event("SYSTEM", "Streamlit dashboard stopped by user")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        logger.log_event("ERROR", f"Streamlit dashboard error: {str(e)}")

def view_logs(logger):
    """View detection logs"""
    print("\n📊 Detection Logs:")
    print("=" * 60)
    
    try:
        with open(logger.log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        if len(lines) > 50:
            # Show last 50 lines
            print("(Showing last 50 lines)\n")
            for line in lines[-50:]:
                print(line.rstrip())
        else:
            for line in lines:
                print(line.rstrip())
        
        print("\n" + "=" * 60)
        print(f"📁 Log file: {os.path.abspath(logger.log_file)}")
        
    except FileNotFoundError:
        print("❌ Log file not found")
    except Exception as e:
        print(f"❌ Error reading log file: {str(e)}")
    
    input("\nPress Enter to continue...")

def main():
    """Main entry point"""
    logger = DetectionLogger()
    
    # Print welcome banner
    print_banner()
    
    while True:
        print_menu()
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                run_human_detection(logger)
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                run_combined_mode(logger)
                input("\nPress Enter to continue...")
            
            elif choice == '3':
                run_flask_dashboard(logger)
                input("\nPress Enter to continue...")
            
            elif choice == '4':
                run_streamlit_dashboard(logger)
                input("\nPress Enter to continue...")
            
            elif choice == '5':
                view_logs(logger)
            
            elif choice == '6':
                print("\n👋 Thank you for using Smart Energy Efficiency System!")
                print("📝 All detection events have been logged for your project report.")
                print("=" * 60)
                break
            
            else:
                print("\n❌ Invalid choice. Please enter 1-6.")
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("\n\n👋 System interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            logger.log_event("ERROR", f"Main loop error: {str(e)}")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
