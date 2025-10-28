# 📖 Usage Guide - Smart Energy Efficiency System

## 🎮 How to Use the System

### Quick Start

1. **Launch the system:**
   ```bash
   python main.py
   ```

2. **You'll see this menu:**
   ```
   ============================================================
   ⚡ SMART ENERGY EFFICIENCY SYSTEM ⚡
   ============================================================
   
   SELECT OPERATION MODE:
   ============================================================
   1. 🎥 Human Detection (Camera) Only
   2. 🌡️ Temperature + Human Detection (Combined)
   3. 🌐 Live Flask Dashboard (Web Interface)
   4. 🖥️  Streamlit Smart Dashboard (Advanced UI)
   5. 📊 View Detection Logs
   6. ❌ Exit
   ============================================================
   ```

3. **Enter your choice (1-6)**

---

## 🎥 Mode 1: Human Detection

**What it does:**
- Opens your camera
- Uses AI (YOLO) to detect people in real-time
- Automatically turns fan ON when person detected
- Turns OFF when no person visible

**How to use:**
1. Select option 1
2. Wait for camera to open
3. Face the camera - fan will turn on automatically
4. Press 'Q' to quit and return to menu

**Perfect for:** Basic demonstration of AI detection

---

## 🌡️ Mode 2: Combined Detection (Temperature + Camera)

**What it does:**
- Combines human detection with temperature monitoring
- Fan turns ON only when:
  - ✅ Person is detected AND
  - ✅ Temperature > 27°C (threshold)
- More energy-efficient!

**How to use:**
1. Select option 2
2. Camera opens with temperature display
3. Fan turns on only in hot conditions with people present
4. Press 'Q' to quit

**Perfect for:** Energy efficiency demonstration

---

## 🌐 Mode 3: Flask Dashboard

**What it does:**
- Opens web interface at http://localhost:5000
- Shows live video feed with detection overlay
- Real-time object tracking visualization

**How to use:**
1. Select option 3
2. Wait for server to start
3. Open browser to http://localhost:5000
4. Press Ctrl+C to stop

**Perfect for:** Web-based monitoring

---

## 🖥️ Mode 4: Streamlit Dashboard (RECOMMENDED)

**What it does:**
- Opens advanced dashboard at http://localhost:8501
- Most comprehensive interface with:
  - ✨ Real-time energy monitoring
  - 💡 AI-powered energy saving tips
  - 📋 Action log for all controls
  - ⚠️ Energy waste alerts
  - 📊 Advanced analytics with AI summaries
  - 🤖 ML model training interface
  - 🌡️ Temperature threshold control

**How to use:**
1. Select option 4
2. Wait for dashboard to load
3. Open browser to http://localhost:8501
4. Explore all 6 tabs!
5. Press Ctrl+C to stop

**Perfect for:** Complete project demonstration

---

## 📊 Mode 5: View Detection Logs

**What it does:**
- Shows all detection events with timestamps
- Perfect for project reports
- Automatically generated during operation

**How to use:**
1. Select option 5
2. View the event log
3. Press Enter to return to menu

**Perfect for:** Writing project reports

---

## ❌ Mode 6: Exit

Safely exits the system and saves all logs.

---

## 📝 Detection Logging

Every event is automatically saved to `detection_log.txt`:

```
[2024-01-15 14:30:25] SYSTEM: Started Human Detection mode
[2024-01-15 14:30:30] CAMERA: Camera opened successfully
[2024-01-15 14:30:45] DETECTION: Human detected (#1) → Fan: ON
[2024-01-15 14:31:12] IDLE: No human detected → Fan: OFF
```

**Use this in your project report!**

---

## 🎓 Tips for Project Demo

### Before Demo:

1. **Test all modes** to ensure they work
2. **Position camera** so you're clearly visible
3. **Check temperature** - ensure it's above threshold for Mode 2
4. **Prepare browser** - know which URLs to open

### During Demo:

1. **Start with Mode 1** - Show basic detection
2. **Show Mode 2** - Explain energy efficiency
3. **Launch Mode 4** - Show professional dashboard
4. **View logs** - Show automated tracking
5. **Explain AI** - YOLO object detection

### Demo Script:

```
Good morning/afternoon!

Today I'm presenting a Smart Energy Efficiency System that uses 
AI and machine learning to automatically manage energy consumption.

[Run Mode 1 - Human Detection]
As you can see, the camera detects me in real-time. The system 
automatically turns the fan on.

[Run Mode 2 - Combined]
Now, combining temperature monitoring, the fan only turns on 
when both conditions are met - a person is present AND it's hot.
This saves energy!

[Run Mode 4 - Streamlit]
Here's the advanced dashboard with real-time monitoring, AI tips,
and detailed analytics. You can see energy savings, alerts, and more.

[Show Logs]
All events are automatically logged. Here's the complete history.

This system demonstrates practical AI application for energy management.
Thank you!
```

---

## 🚀 Quick Commands

```bash
# Run the system
python main.py

# Run Streamlit only (fastest way)
streamlit run smart_energy_app.py

# Run Flask only
python app_flask.py

# View logs
python main.py  # Then select option 5

# Check system
python test_main.py
```

---

## 📱 Mobile Access

If your computer and mobile device are on the same network:

1. Find your computer's IP address
2. Use network URL shown in Streamlit (e.g., http://192.168.1.100:8501)
3. Open on mobile browser

---

## 🎯 What Each Mode Shows

| Mode | Technology | Best For |
|------|------------|----------|
| 1 | Camera + AI | Basic AI demo |
| 2 | Camera + AI + Sensors | Energy efficiency |
| 3 | Web + Video | Remote monitoring |
| 4 | Advanced UI | Complete project |
| 5 | Logging | Report data |

---

**Enjoy demonstrating your Smart Energy System! ⚡**


