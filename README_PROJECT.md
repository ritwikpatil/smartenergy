# ⚡ Smart Energy Efficiency System

An intelligent energy management system with ML-based human detection, temperature monitoring, and automated fan control.

## 🎯 Features

- **ML-Powered Human Detection** - Real-time camera-based person detection using YOLO
- **Temperature Monitoring** - Smart threshold-based automatic control
- **Flask Dashboard** - Live web interface with video feed
- **Streamlit Advanced UI** - Professional dashboard with analytics and AI features
- **Detection Logging** - Automatic event logging for project reports
- **Multi-Mode Operation** - Choose your preferred operation mode

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
pip install torch torchvision opencv-python flask streamlit plotly pandas numpy pyyaml tqdm
```

### 2. Run the System

```bash
python main.py
```

### 3. Select Operation Mode

The system will show a menu:

```
==========================================
⚡ SMART ENERGY EFFICIENCY SYSTEM ⚡
==========================================

SELECT OPERATION MODE:
==========================================
1. 🎥 Human Detection (Camera) Only
2. 🌡️ Temperature + Human Detection (Combined)
3. 🌐 Live Flask Dashboard (Web Interface)
4. 🖥️  Streamlit Smart Dashboard (Advanced UI)
5. 📊 View Detection Logs
6. ❌ Exit
==========================================
```

## 📋 Operation Modes

### Option 1: Human Detection Only
- Uses camera to detect people in real-time
- Automatically turns fan ON when human detected
- Turns OFF when no person detected
- Press 'Q' to quit

### Option 2: Combined Mode (Temperature + Camera)
- Combines human detection with temperature monitoring
- Fan turns ON only when:
  - Human is detected AND
  - Temperature is above threshold (default: 27°C)
- More energy-efficient operation
- Press 'Q' to quit

### Option 3: Flask Dashboard
- Opens web interface at http://localhost:5000
- Live video feed with detection overlay
- Real-time object tracking visualization
- Access from any device on your network

### Option 4: Streamlit Dashboard (Recommended)
- Opens advanced UI at http://localhost:8501
- **Features:**
  - Real-time energy monitoring
  - AI-powered energy saving tips
  - Action log for manual controls
  - Energy waste alerts
  - Advanced analytics with AI summaries
  - ML model training interface
  - Multi-room management (6 rooms)
  - Temperature threshold control
- Professional modern interface
- Best for project demonstrations

### Option 5: View Detection Logs
- Shows all detection events
- Timestamped logs
- Perfect for project reports
- Saved to `detection_log.txt`

### Option 6: Exit
- Gracefully exits the system
- All events are logged for reporting

## 📊 Detection Logging

All events are automatically logged to `detection_log.txt` with timestamps:

```
[2024-01-15 14:30:25] SYSTEM: Started Human Detection mode
[2024-01-15 14:30:30] CAMERA: Camera opened successfully
[2024-01-15 14:30:45] DETECTION: Human detected (#1) → Fan: ON
[2024-01-15 14:31:12] IDLE: No human detected → Fan: OFF
[2024-01-15 14:35:00] SYSTEM: Human Detection mode ended. Total detections: 45
```

**Perfect for:** Project reports, lab assignments, demo presentations

## 🏗️ Project Structure

```
automatic_fan_/
├── main.py                    # Main entry point with menu
├── app_flask.py               # Flask web dashboard
├── smart_energy_app.py        # Streamlit advanced dashboard
├── fan_controller.py          # Fan control logic
├── temp_sensor.py             # Temperature monitoring
├── utils.py                   # Configuration utilities
├── config.yaml                # System configuration
├── templates/
│   └── index.html            # Flask dashboard template
├── requirements.txt           # Dependencies
├── detection_log.txt          # Auto-generated event logs
└── README_PROJECT.md          # This file
```

## ⚙️ Configuration

Edit `config.yaml` to customize settings:

```yaml
gpio_pin: 17           # GPIO pin for fan control
off_delay: 15          # Seconds before turning fan off
temp_threshold: 27     # Temperature threshold in Celsius
```

## 🎓 Perfect for Mini-Project Report

### What to Include:

1. **Introduction**
   - Smart energy management using AI
   - Purpose: Reduce energy waste with intelligent automation

2. **Features Demonstrated**
   - Real-time human detection
   - Temperature-based control
   - Web dashboards
   - Detection logging
   - Energy analytics

3. **Technical Stack**
   - Python 3.x
   - YOLO (Object Detection)
   - OpenCV (Camera)
   - Flask/Streamlit (Web UI)
   - GPIO (Hardware Control)

4. **Results**
   - Show detection_log.txt
   - Screenshots of dashboards
   - Energy savings calculations
   - Detection accuracy

5. **Screenshots to Capture**
   - Human detection with person bounding boxes
   - Streamlit dashboard (all tabs)
   - Flask video feed
   - Detection log file
   - Fan control in action

## 🌐 Network Access

### Flask Dashboard
- Local: http://localhost:5000
- Network: http://YOUR_IP:5000

### Streamlit Dashboard
- Local: http://localhost:8501
- Network: http://YOUR_IP:8501

## 🔧 Troubleshooting

### Camera not working?
```bash
# Check available cameras
import cv2
print([i for i in range(10) if cv2.VideoCapture(i).isOpened()])
```

### Dependencies missing?
```bash
pip install --upgrade -r requirements.txt
```

### GPIO issues (Raspberry Pi)?
```bash
sudo pip install RPi.GPIO
```

## 📈 For Project Report

### Key Points to Highlight:

1. **Innovation**: AI-powered energy management
2. **Practical Application**: Real-world energy savings
3. **Technical Skills**: ML, Computer Vision, Web Development
4. **Efficiency**: Automated system reduces manual intervention
5. **Scalability**: Can monitor multiple rooms/appliances

### Sample Report Sections:

- **Abstract**: Brief overview
- **Methodology**: Technical approach
- **Results**: Detection log analysis
- **Conclusion**: Energy savings achieved
- **Future Work**: Extensions possible

## 📞 Support

For issues or questions, check the logs in `detection_log.txt` for detailed event history.

---

**Made with ⚡ for Smart Energy Management**


