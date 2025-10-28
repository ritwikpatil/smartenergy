#!/usr/bin/env python3
"""
Smart Energy Efficiency Framework with ML-based Object Tracking
A comprehensive web application for energy monitoring and optimization
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import time
import random
from typing import Dict, List, Tuple
import base64
from io import BytesIO
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Smart Energy Efficiency Framework",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Modern UI
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    /* Global Styles - Fresh Theme */
    .main {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 25%, #334155 50%, #1E293B 75%, #0F172A 100%);
    }
    
    /* Header Styles - Bold and Energetic */
    .main-header {
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 50%, #FFE66D 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -0.04em;
        font-family: 'Space Grotesk', sans-serif;
        text-shadow: 0 4px 20px rgba(255, 107, 107, 0.4);
    }
    
    .sub-header {
        font-size: 1.4rem;
        color: #CBD5E1;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 600;
        letter-spacing: 0.03em;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    /* Card Styles - Fresh Neo-Brutal Design */
    .metric-card {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF875A 50%, #FF6B9D 100%);
        padding: 2rem;
        border-radius: 24px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 8px 0 #0F172A, 0 8px 20px rgba(255, 107, 107, 0.4);
        border: 3px solid #0F172A;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s;
    }
    
    .metric-card:hover::before {
        left: 100%;
    }
    
    .metric-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 0 #0F172A, 0 12px 30px rgba(255, 107, 107, 0.5);
    }
    
    .metric-value {
        font-size: 3rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
        letter-spacing: -0.03em;
        text-shadow: 2px 2px 0px #0F172A;
    }
    
    .metric-label {
        font-size: 1rem;
        opacity: 1;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        text-shadow: 1px 1px 0px rgba(0,0,0,0.3);
    }
    
    /* Alert Cards - Bold and Vibrant */
    .alert-card {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF5555 100%);
        padding: 2rem;
        border-radius: 24px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 0 #0F172A, 0 8px 30px rgba(255, 107, 107, 0.5);
        border: 3px solid #0F172A;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        overflow: hidden;
    }
    
    .alert-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 0 #0F172A, 0 12px 40px rgba(255, 107, 107, 0.6);
    }
    
    .success-card {
        background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%);
        padding: 2rem;
        border-radius: 24px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 0 #0F172A, 0 8px 30px rgba(78, 205, 196, 0.5);
        border: 3px solid #0F172A;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        overflow: hidden;
    }
    
    .success-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 0 #0F172A, 0 12px 40px rgba(78, 205, 196, 0.6);
    }
    
    .info-card {
        background: linear-gradient(135deg, #A8E6CF 0%, #FFE66D 100%);
        padding: 2rem;
        border-radius: 24px;
        color: #0F172A;
        margin: 1rem 0;
        box-shadow: 0 8px 0 #0F172A, 0 8px 30px rgba(255, 230, 109, 0.5);
        border: 3px solid #0F172A;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
        overflow: hidden;
    }
    
    .info-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 0 #0F172A, 0 12px 40px rgba(255, 230, 109, 0.6);
    }
    
    /* Room Cards - Neo-Brutal Style */
    .room-card {
        background: linear-gradient(135deg, #2E3440 0%, #3B4252 50%, #434C5E 100%);
        border: 4px solid #0F172A;
        border-radius: 24px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 0 #0F172A, 0 10px 40px rgba(0, 0, 0, 0.3);
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        position: relative;
    }
    
    .room-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 6px;
        background: linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 50%, #FFE66D 100%);
        border-radius: 24px 24px 0 0;
    }
    
    .room-card:hover {
        box-shadow: 0 14px 0 #0F172A, 0 14px 50px rgba(78, 205, 196, 0.4);
        transform: translateY(-6px);
    }
    
    .room-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    .room-name {
        font-size: 1.5rem;
        font-weight: 900;
        color: #FFE66D;
        text-shadow: 2px 2px 0px #0F172A;
        letter-spacing: -0.02em;
    }
    
    .room-status {
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    .status-occupied {
        background: #dcfce7;
        color: #166534;
    }
    
    .status-empty {
        background: #fef2f2;
        color: #dc2626;
    }
    
    /* Appliance Status */
    .appliance-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .appliance-item {
        background: linear-gradient(135deg, rgba(248, 250, 252, 0.8) 0%, rgba(241, 245, 249, 0.8) 100%);
        border: 2px solid transparent;
        border-radius: 16px;
        padding: 1rem;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(10px);
    }
    
    .appliance-item:hover {
        background: linear-gradient(135deg, rgba(255, 255, 255, 1) 0%, rgba(248, 250, 252, 1) 100%);
        border-color: #cbd5e1;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }
    
    .appliance-name {
        font-size: 0.875rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .appliance-status {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .status-on {
        background: #dcfce7;
        color: #166534;
    }
    
    .status-off {
        background: #f1f5f9;
        color: #334155;
    }
    
    /* Buttons - Bold Neo-Brutal */
    .stButton > button {
        background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%);
        color: #0F172A;
        border: 3px solid #0F172A;
        border-radius: 16px;
        padding: 0.875rem 2.5rem;
        font-weight: 800;
        font-size: 1rem;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        box-shadow: 0 6px 0 #0F172A, 0 6px 20px rgba(78, 205, 196, 0.4);
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 0 #0F172A, 0 8px 30px rgba(78, 205, 196, 0.6);
        background: linear-gradient(135deg, #FFE66D 0%, #FFD93D 100%);
    }
    
    /* Sidebar - Dark Theme */
    .css-1d391kg {
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border-right: 4px solid #4ECDC4;
    }
    
    /* Tabs - Bold & Vibrant */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: transparent;
        border-bottom: 4px solid #4ECDC4;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #2E3440;
        border-radius: 16px;
        padding: 1.2rem 2rem;
        font-weight: 800;
        font-size: 1rem;
        color: #E5E7EB;
        transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
        border: 3px solid transparent;
        letter-spacing: 0.02em;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: #3B4252;
        border-color: #4ECDC4;
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(78, 205, 196, 0.3);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 50%, #FFE66D 100%);
        color: #0F172A;
        border: 3px solid #0F172A;
        box-shadow: 0 6px 0 #0F172A, 0 6px 20px rgba(255, 107, 107, 0.5);
        font-weight: 900;
    }
    
    /* Progress Bars */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 50%, #FFE66D 100%);
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(78, 205, 196, 0.4);
        border: 2px solid #0F172A;
    }
    
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #cbd5e1 0%, #94a3b8 100%);
        border-radius: 10px;
        border: 2px solid rgba(255, 255, 255, 0.8);
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #94a3b8 0%, #64748b 100%);
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { 
            opacity: 0; 
            transform: translateY(20px) scale(0.95); 
        }
        to { 
            opacity: 1; 
            transform: translateY(0) scale(1); 
        }
    }
    
    .fade-in {
        animation: fadeIn 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
            transform: scale(1);
        }
        50% {
            opacity: 0.8;
            transform: scale(1.05);
        }
    }
    
    /* Status Indicators */
    .status-indicator {
        display: inline-block;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        margin-right: 0.5rem;
        animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
    }
    
    .indicator-online {
        background: linear-gradient(135deg, #4ECDC4 0%, #44A08D 100%);
        box-shadow: 0 0 0 4px rgba(78, 205, 196, 0.4), 0 0 25px rgba(78, 205, 196, 0.6);
        border: 2px solid #0F172A;
    }
    
    .indicator-offline {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF5555 100%);
        box-shadow: 0 0 0 4px rgba(255, 107, 107, 0.4), 0 0 25px rgba(255, 107, 107, 0.6);
        border: 2px solid #0F172A;
    }
    
    .indicator-warning {
        background: linear-gradient(135deg, #FFE66D 0%, #FFD93D 100%);
        box-shadow: 0 0 0 4px rgba(255, 230, 109, 0.4), 0 0 25px rgba(255, 230, 109, 0.6);
        border: 2px solid #0F172A;
    }
    
    /* Background gradient - Dark & Dynamic */
    .main {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 25%, #334155 50%, #1E293B 75%, #0F172A 100%);
        min-height: 100vh;
        position: relative;
    }
    
    .main::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 50%, rgba(255, 107, 107, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 80% 80%, rgba(78, 205, 196, 0.15) 0%, transparent 50%),
            radial-gradient(circle at 40% 20%, rgba(255, 230, 109, 0.1) 0%, transparent 50%);
        pointer-events: none;
    }
</style>
""", unsafe_allow_html=True)

class OccupancyDetector:
    """ML-based occupancy detection system"""
    
    def __init__(self):
        self.model_loaded = False
        self.load_model()
    
    def load_model(self):
        """Load or initialize the occupancy detection model"""
        try:
            # Simulate model loading
            self.model_loaded = True
            st.success("✅ Occupancy Detection Model Loaded")
        except Exception as e:
            st.error(f"❌ Model loading failed: {e}")
            self.model_loaded = False
    
    def detect_occupancy(self, image_data=None) -> Tuple[bool, float, int]:
        """
        Detect occupancy in the given image
        Returns: (is_occupied, confidence, person_count)
        """
        if not self.model_loaded:
            return False, 0.0, 0
        
        # Simulate ML detection with some randomness
        confidence = random.uniform(0.7, 0.95)
        person_count = random.randint(0, 3)
        is_occupied = person_count > 0 and confidence > 0.5
        
        return is_occupied, confidence, person_count

class Room:
    """Room management class"""
    
    def __init__(self, room_id: str, name: str, appliances: List[str]):
        self.room_id = room_id
        self.name = name
        self.appliances = {app: False for app in appliances}
        self.occupancy_history = []
        self.energy_consumption = {app: 0.0 for app in appliances}
        self.last_occupancy_check = datetime.now()
        self.is_occupied = False
        self.occupancy_confidence = 0.0
        self.person_count = 0
    
    def update_occupancy(self, is_occupied: bool, confidence: float, person_count: int):
        """Update room occupancy status"""
        self.is_occupied = is_occupied
        self.occupancy_confidence = confidence
        self.person_count = person_count
        self.last_occupancy_check = datetime.now()
        
        # Add to history
        self.occupancy_history.append({
            'timestamp': datetime.now(),
            'is_occupied': is_occupied,
            'confidence': confidence,
            'person_count': person_count
        })
        
        # Keep only last 100 records
        if len(self.occupancy_history) > 100:
            self.occupancy_history = self.occupancy_history[-100:]
    
    def toggle_appliance(self, appliance: str):
        """Toggle appliance on/off"""
        if appliance in self.appliances:
            self.appliances[appliance] = not self.appliances[appliance]
    
    def get_energy_waste(self) -> float:
        """Calculate energy waste (appliances on but no occupancy)"""
        if not self.is_occupied and any(self.appliances.values()):
            return sum(self.energy_consumption.values())
        return 0.0
    
    def get_appliance_count(self) -> int:
        """Get count of appliances that are on"""
        return sum(1 for status in self.appliances.values() if status)

class EnergyMonitor:
    """Energy monitoring and analytics system"""
    
    def __init__(self):
        self.rooms = {}
        self.energy_savings_history = []
        self.total_energy_saved = 0.0
        self.initialize_rooms()
    
    def initialize_rooms(self):
        """Initialize default rooms and appliances"""
        default_rooms = {
            'living_room': ['TV', 'Air Conditioner', 'Lights', 'Fan'],
            'bedroom_1': ['Air Conditioner', 'Lights', 'Fan', 'Charger'],
            'bedroom_2': ['Air Conditioner', 'Lights', 'Fan', 'Laptop'],
            'kitchen': ['Refrigerator', 'Microwave', 'Lights', 'Exhaust Fan'],
            'office': ['Computer', 'Monitor', 'Lights', 'Printer'],
            'bathroom': ['Lights', 'Exhaust Fan', 'Water Heater']
        }
        
        for room_id, appliances in default_rooms.items():
            room_name = room_id.replace('_', ' ').title()
            self.rooms[room_id] = Room(room_id, room_name, appliances)
    
    def add_room(self, room_id: str, name: str, appliances: List[str]):
        """Add a new room"""
        self.rooms[room_id] = Room(room_id, name, appliances)
    
    def update_room_occupancy(self, room_id: str, is_occupied: bool, confidence: float, person_count: int):
        """Update occupancy for a specific room"""
        if room_id in self.rooms:
            self.rooms[room_id].update_occupancy(is_occupied, confidence, person_count)
    
    def get_energy_alerts(self) -> List[Dict]:
        """Get energy waste alerts"""
        alerts = []
        for room in self.rooms.values():
            waste = room.get_energy_waste()
            if waste > 0:
                alerts.append({
                    'room': room.name,
                    'waste': waste,
                    'appliances_on': room.get_appliance_count(),
                    'timestamp': room.last_occupancy_check
                })
        return alerts
    
    def calculate_energy_savings(self):
        """Calculate total energy savings"""
        total_waste = sum(room.get_energy_waste() for room in self.rooms.values())
        self.total_energy_saved += total_waste * 0.1  # Simulate savings
        
        self.energy_savings_history.append({
            'timestamp': datetime.now(),
            'savings': self.total_energy_saved,
            'waste_prevented': total_waste
        })
        
        # Keep only last 100 records
        if len(self.energy_savings_history) > 100:
            self.energy_savings_history = self.energy_savings_history[-100:]

def log_action(action_type, room, appliance, status):
    """Log an action to the action log"""
    action = {
        'timestamp': datetime.now(),
        'type': action_type,
        'room': room,
        'appliance': appliance,
        'status': status
    }
    st.session_state.action_log.insert(0, action)
    # Keep only last 100 actions
    if len(st.session_state.action_log) > 100:
        st.session_state.action_log = st.session_state.action_log[:100]

def generate_energy_tips():
    """Generate AI-powered energy saving tips"""
    tips = [
        {
            'title': 'Optimize AC Usage',
            'description': 'Set your AC to 27°C and use ceiling fans for circulation. This can save up to 30% on cooling costs.',
            'impact': 'High',
            'savings': 'Up to 30%'
        },
        {
            'title': 'Smart Lighting',
            'description': 'Turn off lights in empty rooms. Use LEDs which consume 80% less energy than incandescent bulbs.',
            'impact': 'Medium',
            'savings': 'Up to 50% on lighting'
        },
        {
            'title': 'Unplug Unused Electronics',
            'description': 'Many devices consume power even when off. Unplug chargers and unused appliances.',
            'impact': 'Medium',
            'savings': '5-10% monthly'
        },
        {
            'title': 'Monitor Peak Hours',
            'description': 'Shift heavy appliance usage to off-peak hours to save on electricity bills.',
            'impact': 'High',
            'savings': '15-20% on rates'
        },
        {
            'title': 'Use Natural Ventilation',
            'description': 'Open windows during cooler parts of the day to reduce AC dependency.',
            'impact': 'Low',
            'savings': '10-15% on cooling'
        },
        {
            'title': 'Automate Energy Management',
            'description': 'Use the occupancy detection to automatically turn off appliances in empty rooms.',
            'impact': 'High',
            'savings': '20-40% monthly'
        }
    ]
    return random.sample(tips, 3)

def generate_ai_summary():
    """Generate AI-powered energy consumption summary"""
    total_energy = sum(sum(room.energy_consumption.values()) for room in st.session_state.energy_monitor.rooms.values())
    occupied_rooms = sum(1 for room in st.session_state.energy_monitor.rooms.values() if room.is_occupied)
    total_appliances = sum(len(room.appliances) for room in st.session_state.energy_monitor.rooms.values())
    apps_on = sum(room.get_appliance_count() for room in st.session_state.energy_monitor.rooms.values())
    
    summary = f"""
    **Energy Consumption Analysis Summary**
    
    Your energy management system shows:
    - **Total Energy Usage:** {total_energy:.2f} kWh
    - **Occupied Rooms:** {occupied_rooms} out of {len(st.session_state.energy_monitor.rooms)} rooms
    - **Appliances Active:** {apps_on} out of {total_appliances} total appliances
    - **Efficiency Rate:** {((total_appliances - apps_on) / total_appliances * 100) if total_appliances > 0 else 0:.1f}% optimized
    - **Energy Savings:** {st.session_state.energy_monitor.total_energy_saved:.2f} kWh saved
    
    **Key Insights:**
    {'✓ Most rooms are efficiently managed' if apps_on / total_appliances < 0.5 else '⚠ Some rooms may need optimization'}
    {'✓ Occupancy detection is working well' if occupied_rooms > 0 else '⚠ No active occupancy detected'}
    {'✓ Appliances are being used efficiently' if apps_on < total_appliances * 0.6 else '⚠ Consider reducing appliance usage'}
    
    **Recommendations:**
    - Use occupancy detection to automatically control appliances
    - Monitor temperature thresholds to optimize HVAC usage
    - Review energy tips for additional savings opportunities
    """
    
    return summary

def initialize_session_state():
    """Initialize Streamlit session state"""
    if 'energy_monitor' not in st.session_state:
        st.session_state.energy_monitor = EnergyMonitor()
    
    if 'occupancy_detector' not in st.session_state:
        st.session_state.occupancy_detector = OccupancyDetector()
    
    if 'selected_room' not in st.session_state:
        st.session_state.selected_room = 'living_room'
    
    if 'ml_model_training_data' not in st.session_state:
        st.session_state.ml_model_training_data = []
    
    # New features: Action Log, Temperature Threshold, Energy Tips, AI Summaries
    if 'action_log' not in st.session_state:
        st.session_state.action_log = []
    
    if 'temperature_threshold' not in st.session_state:
        st.session_state.temperature_threshold = 27.0
    
    if 'energy_tips_generated' not in st.session_state:
        st.session_state.energy_tips_generated = []
    
    if 'ai_summary' not in st.session_state:
        st.session_state.ai_summary = None

def main():
    """Main application function"""
    initialize_session_state()
    
    # Header with modern design
    st.markdown('<h1 class="main-header">⚡ Smart Energy Efficiency Framework</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">ML-Powered Energy Monitoring & Optimization System 🔋</p>', unsafe_allow_html=True)
    
    # Status bar with bold design
    st.markdown(
        '''
        <div style="background: linear-gradient(135deg, #2E3440 0%, #3B4252 50%, #434C5E 100%);
                    border: 4px solid #0F172A;
                    border-radius: 24px; padding: 1.5rem 2rem; margin-bottom: 2rem;
                    box-shadow: 0 10px 0 #0F172A, 0 10px 40px rgba(0, 0, 0, 0.4);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center;">
                    <div class="status-indicator indicator-online"></div>
                    <span style="color: #4ECDC4; font-weight: 800; font-size: 1.1rem; letter-spacing: 0.02em;
                               text-shadow: 2px 2px 0px #0F172A; font-family: 'Space Grotesk', sans-serif;">SYSTEM ONLINE</span>
                </div>
                <div style="text-align: center;">
                    <span style="color: #E5E7EB; font-weight: 700; font-size: 1rem;">
                        Last Updated: <span style="color: #FFE66D; font-weight: 900; text-shadow: 2px 2px 0px #0F172A;" id="time"></span>
                    </span>
                </div>
                <div style="display: flex; align-items: center;">
                    <div class="status-indicator indicator-online"></div>
                    <span style="color: #4ECDC4; font-weight: 800; font-size: 1.1rem; letter-spacing: 0.02em;
                               text-shadow: 2px 2px 0px #0F172A; font-family: 'Space Grotesk', sans-serif;">ML ACTIVE</span>
                </div>
            </div>
        </div>
        <script>
            function updateTime() {
                const now = new Date();
                document.getElementById('time').textContent = now.toLocaleTimeString('en-US', {hour12: false});
            }
            setInterval(updateTime, 1000);
            updateTime();
        </script>
        ''',
        unsafe_allow_html=True
    )
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Sidebar with bold design
    with st.sidebar:
        st.markdown('''
        <div style="text-align: center; margin-bottom: 2rem; padding: 1.5rem; 
                    background: linear-gradient(135deg, #2E3440 0%, #3B4252 100%);
                    border-radius: 24px; border: 4px solid #0F172A;
                    box-shadow: 0 8px 0 #0F172A;">
            <h2 style="color: #FFE66D; margin: 0; font-size: 2rem; font-weight: 900; 
                       letter-spacing: -0.02em; text-shadow: 3px 3px 0px #0F172A;
                       font-family: 'Space Grotesk', sans-serif;">🎛️ CONTROL PANEL</h2>
            <p style="color: #4ECDC4; margin: 0.5rem 0 0 0; font-size: 1rem; font-weight: 700;
                      text-transform: uppercase; letter-spacing: 0.1em;">System Controls & Settings</p>
        </div>
        ''', unsafe_allow_html=True)
        
        # Room selection
        st.markdown("### 🏠 Room Selection")
        room_options = {room_id: room.name for room_id, room in st.session_state.energy_monitor.rooms.items()}
        selected_room_id = st.selectbox("Choose Room", options=list(room_options.keys()), 
                                      format_func=lambda x: room_options[x], key="room_selector")
        st.session_state.selected_room = selected_room_id
        
        # Quick stats with bold design
        current_room = st.session_state.energy_monitor.rooms[selected_room_id]
        status_color = '#4ECDC4' if current_room.is_occupied else '#FF6B6B'
        st.markdown(f'''
        <div style="background: linear-gradient(135deg, #2E3440 0%, #3B4252 100%);
                    padding: 1.5rem; border-radius: 20px; margin: 1rem 0;
                    box-shadow: 0 8px 0 #0F172A; border: 3px solid #0F172A;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.75rem; align-items: center;">
                <span style="color: #E5E7EB; font-size: 0.9rem; font-weight: 800;">STATUS:</span>
                <span style="color: {status_color}; 
                           font-weight: 900; font-size: 1rem; 
                           padding: 0.5rem 1rem; border-radius: 16px;
                           background: {status_color}; color: #0F172A;
                           border: 2px solid #0F172A; text-transform: uppercase;">
                    {'OCCUPIED' if current_room.is_occupied else 'EMPTY'}
                </span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.75rem; align-items: center;">
                <span style="color: #E5E7EB; font-size: 0.9rem; font-weight: 800;">APPLIANCES ON:</span>
                <span style="color: #FFE66D; font-weight: 900; font-size: 1.5rem; text-shadow: 2px 2px 0px #0F172A;">{current_room.get_appliance_count()}</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #E5E7EB; font-size: 0.9rem; font-weight: 800;">PEOPLE:</span>
                <span style="color: #FFE66D; font-weight: 900; font-size: 1.5rem; text-shadow: 2px 2px 0px #0F172A;">{current_room.person_count}</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Manual controls
        st.markdown("### 🎮 Manual Controls")
        if st.button("🔄 Toggle Occupancy", key="manual_occupancy", use_container_width=True):
            current_room = st.session_state.energy_monitor.rooms[selected_room_id]
            new_occupancy = not current_room.is_occupied
            st.session_state.energy_monitor.update_room_occupancy(
                selected_room_id, new_occupancy, 1.0, 1 if new_occupancy else 0
            )
            st.rerun()
        
        if st.button("💡 Turn On All", key="turn_on_all", use_container_width=True):
            for appliance in current_room.appliances:
                current_room.appliances[appliance] = True
            st.success("All appliances turned on!")
            st.rerun()
        
        if st.button("🔌 Turn Off All", key="turn_off_all", use_container_width=True):
            for appliance in current_room.appliances:
                current_room.appliances[appliance] = False
                log_action("Manual Override", current_room.name, appliance, False)
            st.success("All appliances turned off!")
            st.rerun()
        
        if st.button("💡 Turn On All", key="turn_on_all_sidebar", use_container_width=True):
            for appliance in current_room.appliances:
                current_room.appliances[appliance] = True
                log_action("Manual Override", current_room.name, appliance, True)
            st.success("All appliances turned on!")
            st.rerun()
        
        # Emergency controls
        st.markdown("### 🚨 Emergency Controls")
        if st.button("⚠️ EMERGENCY SHUTDOWN", key="emergency_off", use_container_width=True):
            for room in st.session_state.energy_monitor.rooms.values():
                for appliance in room.appliances:
                    room.appliances[appliance] = False
            st.error("🚨 EMERGENCY: All appliances turned off!")
            st.rerun()
        
        # System status with bold design
        st.markdown("### 📊 System Status")
        st.markdown(f'''
        <div style="background: linear-gradient(135deg, #2E3440 0%, #3B4252 100%);
                    padding: 1.5rem; border-radius: 20px; margin: 1rem 0;
                    box-shadow: 0 8px 0 #0F172A; border: 3px solid #0F172A;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.75rem; align-items: center;">
                <span style="color: #E5E7EB; font-size: 0.9rem; font-weight: 800;">TOTAL ROOMS:</span>
                <span style="color: #FFE66D; font-weight: 900; font-size: 1.5rem; text-shadow: 2px 2px 0px #0F172A;">{len(st.session_state.energy_monitor.rooms)}</span>
            </div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.75rem; align-items: center;">
                <span style="color: #E5E7EB; font-size: 0.9rem; font-weight: 800;">ENERGY SAVED:</span>
                <span style="color: #4ECDC4; font-weight: 900; font-size: 1.3rem; text-shadow: 2px 2px 0px #0F172A;">{st.session_state.energy_monitor.total_energy_saved:.1f} kWh</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #E5E7EB; font-size: 0.9rem; font-weight: 800;">ML STATUS:</span>
                <span style="color: #4ECDC4; font-weight: 900; font-size: 0.95rem; 
                           padding: 0.5rem 1rem; border-radius: 16px;
                           background: #4ECDC4; color: #0F172A;
                           border: 2px solid #0F172A; text-transform: uppercase;">ACTIVE</span>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Left navigation (Firebase Studio-like)
    with st.sidebar:
        st.markdown("### 🧭 Navigation")
        nav_choice = st.radio(
            "Go to",
            options=[
                "🏠 Overview",
                "📟 Devices",
                "📊 Analytics",
                "🧾 Events",
                "⚙️ Automations",
                "💡 Energy Tips",
                "🔧 Settings",
                "🤖 AI Lab",
            ],
            index=0,
            key="left_nav_choice",
        )

    # Route to selected page
    if nav_choice == "🏠 Overview":
        show_dashboard()
    elif nav_choice == "📟 Devices":
        show_devices()
    elif nav_choice == "📊 Analytics":
        show_analytics()
    elif nav_choice == "🧾 Events":
        show_events()
    elif nav_choice == "⚙️ Automations":
        show_automations()
    elif nav_choice == "💡 Energy Tips":
        show_energy_tips()
    elif nav_choice == "🔧 Settings":
        show_settings()
    elif nav_choice == "🤖 AI Lab":
        show_ml_model_interface()

    # Footer / status bar
    st.markdown(
        '''
        <div style="margin-top:2rem; border-top: 4px solid #0F172A;">
          <div style="display:flex; flex-wrap:wrap; gap:.75rem; align-items:center; justify-content:space-between; padding: 1rem 0;">
            <div style="color:#94a3b8; font-weight:700; letter-spacing:.02em;">⚡ Smart Energy • UI v2</div>
            <div style="display:flex; gap:.5rem; align-items:center;">
              <span style="background:#2E3440; border:2px solid #0F172A; color:#E5E7EB; padding:.35rem .6rem; border-radius:10px; font-weight:700; font-size:.8rem;">Streamlit</span>
              <span style="background:#2E3440; border:2px solid #0F172A; color:#E5E7EB; padding:.35rem .6rem; border-radius:10px; font-weight:700; font-size:.8rem;">Realtime Simulation</span>
            </div>
          </div>
        </div>
        ''',
        unsafe_allow_html=True,
    )

def show_devices():
    """Devices page listing rooms and appliances with quick controls"""
    st.header("📟 Devices")
    for room_id, room in st.session_state.energy_monitor.rooms.items():
        with st.expander(f"{room.name} — {room.get_appliance_count()} on", expanded=False):
            cols = st.columns(3)
            with cols[0]:
                st.write(f"Occupancy: {'🟢' if room.is_occupied else '🔴'}")
            with cols[1]:
                st.write(f"People: {room.person_count}")
            with cols[2]:
                st.write(f"Confidence: {room.occupancy_confidence:.0%}")

            grid_cols = st.columns(4)
            i = 0
            for appliance, status in room.appliances.items():
                with grid_cols[i % 4]:
                    toggled = st.toggle(f"{appliance}", value=status, key=f"dev_{room_id}_{appliance}")
                    if toggled != status:
                        room.appliances[appliance] = toggled
                        log_action("Device Toggle", room.name, appliance, toggled)
                i += 1

def show_events():
    """Events page based on action_log"""
    st.header("🧾 Events")
    if not st.session_state.action_log:
        st.info("No events yet. Interact with devices to generate events.")
        return
    for action in st.session_state.action_log[:50]:
        status_icon = "✅" if action['status'] else "❌"
        st.write(f"{action['timestamp'].strftime('%Y-%m-%d %H:%M:%S')} • {action['type']} • {action['room']} • {action['appliance']} • {status_icon}")

def show_automations():
    """Automations page: simple rules for occupancy/temperature"""
    st.header("⚙️ Automations")
    if 'automation_rules' not in st.session_state:
        st.session_state.automation_rules = {
            'turn_off_when_empty': True,
            'target_temp_threshold': st.session_state.temperature_threshold,
        }

    st.subheader("Rules")
    st.session_state.automation_rules['turn_off_when_empty'] = st.checkbox(
        "Turn off all appliances in empty rooms",
        value=st.session_state.automation_rules['turn_off_when_empty'],
    )
    st.session_state.automation_rules['target_temp_threshold'] = st.slider(
        "Comfort temperature threshold (°C)", 20.0, 35.0,
        value=float(st.session_state.automation_rules['target_temp_threshold']), step=0.5,
    )

    if st.button("Apply Automations Now"):
        apply_automations()
        st.success("Automations applied")

    st.caption("Automations run when you click the button. You can schedule this in production.")

def apply_automations():
    """Apply simple automation rules to rooms"""
    rules = st.session_state.automation_rules
    for room in st.session_state.energy_monitor.rooms.values():
        if rules.get('turn_off_when_empty') and not room.is_occupied:
            for appliance in list(room.appliances.keys()):
                if room.appliances[appliance]:
                    room.appliances[appliance] = False
                    log_action("Automation", room.name, appliance, False)

def show_settings():
    """Settings page for thresholds and theme"""
    st.header("🔧 Settings")
    st.subheader("Temperature")
    st.session_state.temperature_threshold = st.slider(
        "Global temperature threshold (°C)", 20.0, 35.0,
        value=float(st.session_state.temperature_threshold), step=0.5,
    )
    st.subheader("Theme")
    dark_mode = st.toggle("Dark mode (UI preset)", value=True, disabled=True)
    st.caption("Dark mode is enabled by default in this UI.")

def show_dashboard():
    """Display main dashboard"""
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    # Update occupancy for all rooms (simulate real-time detection)
    for room_id, room in st.session_state.energy_monitor.rooms.items():
        is_occupied, confidence, person_count = st.session_state.occupancy_detector.detect_occupancy()
        st.session_state.energy_monitor.update_room_occupancy(room_id, is_occupied, confidence, person_count)
    
    # Calculate energy savings
    st.session_state.energy_monitor.calculate_energy_savings()
    
    # Key metrics with modern cards
    st.markdown("### 📊 System Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    total_rooms = len(st.session_state.energy_monitor.rooms)
    occupied_rooms = sum(1 for room in st.session_state.energy_monitor.rooms.values() if room.is_occupied)
    total_appliances_on = sum(room.get_appliance_count() for room in st.session_state.energy_monitor.rooms.values())
    energy_saved = st.session_state.energy_monitor.total_energy_saved
    
    with col1:
        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">{total_rooms}</div>
            <div class="metric-label">Total Rooms</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">{occupied_rooms}</div>
            <div class="metric-label">Occupied Rooms</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">{total_appliances_on}</div>
            <div class="metric-label">Appliances ON</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col4:
        st.markdown(f'''
        <div class="metric-card">
            <div class="metric-value">{energy_saved:.1f}</div>
            <div class="metric-label">Energy Saved (kWh)</div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Room status grid with modern cards
    st.markdown("### 🏢 Room Status Overview")
    
    for room_id, room in st.session_state.energy_monitor.rooms.items():
        waste = room.get_energy_waste()
        status_class = "status-occupied" if room.is_occupied else "status-empty"
        status_text = "Occupied" if room.is_occupied else "Empty"
        
        st.markdown(f'''
        <div class="room-card">
            <div class="room-header">
                <div class="room-name">{room.name}</div>
                <div class="room-status {status_class}">{status_text}</div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <div>
                    <span style="color: #334155; font-size: 0.875rem; font-weight: 600;">👥 People: {room.person_count}</span>
                    <span style="color: #334155; font-size: 0.875rem; margin-left: 1rem; font-weight: 600;">Confidence: {room.occupancy_confidence:.1%}</span>
                </div>
                <div>
                    {f'<span style="color: #dc2626; font-weight: 700;">⚠️ Waste: {waste:.1f} kWh</span>' if waste > 0 else '<span style="color: #059669; font-weight: 700;">✅ Efficient</span>'}
                </div>
            </div>
            <div class="appliance-grid">
        ''', unsafe_allow_html=True)
        
        for appliance, status in room.appliances.items():
            status_class = "status-on" if status else "status-off"
            st.markdown(f'''
                <div class="appliance-item">
                    <div class="appliance-name">{appliance}</div>
                    <div class="appliance-status {status_class}">{'ON' if status else 'OFF'}</div>
                </div>
            ''', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Control buttons
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button(f"🔄 Toggle All", key=f"toggle_all_{room_id}"):
                for appliance in room.appliances:
                    room.toggle_appliance(appliance)
                st.rerun()
        with col2:
            if st.button(f"💡 Turn On All", key=f"on_all_{room_id}"):
                for appliance in room.appliances:
                    room.appliances[appliance] = True
                st.rerun()
        with col3:
            if st.button(f"🔌 Turn Off All", key=f"off_all_{room_id}"):
                for appliance in room.appliances:
                    room.appliances[appliance] = False
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_room_management():
    """Display room management interface"""
    st.header("🏢 Room Management")
    
    selected_room = st.session_state.energy_monitor.rooms[st.session_state.selected_room]
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader(f"Room: {selected_room.name}")
        
        # Occupancy status
        status_color = "🟢" if selected_room.is_occupied else "🔴"
        st.write(f"**Occupancy Status:** {status_color} {'Occupied' if selected_room.is_occupied else 'Empty'}")
        st.write(f"**Confidence:** {selected_room.occupancy_confidence:.1%}")
        st.write(f"**Person Count:** {selected_room.person_count}")
        st.write(f"**Last Check:** {selected_room.last_occupancy_check.strftime('%H:%M:%S')}")
        
        # Manual occupancy detection
        st.subheader("Manual Occupancy Detection")
        uploaded_file = st.file_uploader("Upload Image for Occupancy Detection", 
                                       type=['png', 'jpg', 'jpeg'], key="occupancy_upload")
        
        if uploaded_file is not None:
            if st.button("Detect Occupancy", key="detect_occupancy"):
                # Simulate processing
                with st.spinner("Processing image..."):
                    time.sleep(2)
                    is_occupied, confidence, person_count = st.session_state.occupancy_detector.detect_occupancy()
                    st.session_state.energy_monitor.update_room_occupancy(
                        selected_room.room_id, is_occupied, confidence, person_count
                    )
                    st.success(f"Detection complete! Occupied: {is_occupied}, Confidence: {confidence:.1%}")
                    st.rerun()
    
    with col2:
        st.subheader("Appliance Control")
        
        for appliance, status in selected_room.appliances.items():
            col_a, col_b = st.columns([2, 1])
            with col_a:
                st.write(f"**{appliance}**")
            with col_b:
                if st.button("Toggle", key=f"appliance_{appliance}"):
                    selected_room.toggle_appliance(appliance)
                    st.rerun()
        
        # Add new appliance
        st.subheader("Add New Appliance")
        new_appliance = st.text_input("Appliance Name", key="new_appliance")
        if st.button("Add Appliance", key="add_appliance") and new_appliance:
            selected_room.appliances[new_appliance] = False
            selected_room.energy_consumption[new_appliance] = 0.0
            st.success(f"Added {new_appliance}")
            st.rerun()

def show_alerts():
    """Display energy alerts"""
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    alerts = st.session_state.energy_monitor.get_energy_alerts()
    
    if not alerts:
        st.markdown('''
        <div class="success-card">
            <h4 style="margin: 0 0 0.5rem 0; font-size: 1.25rem;">🎉 All Systems Efficient</h4>
            <p style="margin: 0; opacity: 0.9;">No energy waste detected! All rooms are operating efficiently.</p>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
        <div class="info-card">
            <h4 style="margin: 0 0 0.5rem 0; font-size: 1.25rem;">📊 Alert Summary</h4>
            <p style="margin: 0; opacity: 0.9;">Found {len(alerts)} energy waste alert(s) requiring attention</p>
        </div>
        ''', unsafe_allow_html=True)
        
        for i, alert in enumerate(alerts):
            st.markdown(f"""
            <div class="alert-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <h4 style="margin: 0; font-size: 1.25rem;">⚠️ Energy Waste Alert #{i+1}</h4>
                    <span style="background: rgba(255,255,255,0.2); padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.875rem; font-weight: 500;">HIGH PRIORITY</span>
                </div>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                    <div>
                        <strong>Room:</strong> {alert['room']}
                    </div>
                    <div>
                        <strong>Appliances ON:</strong> {alert['appliances_on']}
                    </div>
                    <div>
                        <strong>Waste:</strong> {alert['waste']:.2f} kWh
                    </div>
                    <div>
                        <strong>Time:</strong> {alert['timestamp'].strftime('%H:%M:%S')}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Historical alerts
    st.subheader("📈 Alert History")
    
    # Generate some sample historical data
    historical_alerts = []
    for i in range(20):
        historical_alerts.append({
            'timestamp': datetime.now() - timedelta(hours=i),
            'room': random.choice(list(st.session_state.energy_monitor.rooms.keys())),
            'waste': random.uniform(0.5, 5.0),
            'type': random.choice(['High Energy Usage', 'Unoccupied Room', 'Appliance Left On'])
        })
    
    df_alerts = pd.DataFrame(historical_alerts)
    df_alerts['timestamp'] = pd.to_datetime(df_alerts['timestamp'])
    
    fig = px.line(df_alerts, x='timestamp', y='waste', 
                  title='Energy Waste Over Time',
                  labels={'waste': 'Energy Waste (kWh)', 'timestamp': 'Time'})
    st.plotly_chart(fig, use_container_width=True)

def show_analytics():
    """Display analytics and insights"""
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    st.markdown("### 📊 Energy Analytics & Insights")
    
    # AI Summary Section
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### 🤖 AI-Powered Energy Summary")
    with col2:
        if st.button("📝 Generate Summary", key="generate_summary", use_container_width=True):
            with st.spinner("🤖 AI is analyzing your energy consumption..."):
                time.sleep(2)
                st.session_state.ai_summary = generate_ai_summary()
                st.rerun()
    
    if st.session_state.ai_summary:
        st.markdown('''
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 16px; margin: 1rem 0;">
            <div style="white-space: pre-line; line-height: 1.8;">
        ''' + st.session_state.ai_summary + '''
            </div>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.info("👆 Click the button above to generate an AI-powered analysis of your energy consumption!")
    
    # Energy savings over time
    st.subheader("💰 Energy Savings Trend")
    
    if st.session_state.energy_monitor.energy_savings_history:
        df_savings = pd.DataFrame(st.session_state.energy_monitor.energy_savings_history)
        df_savings['timestamp'] = pd.to_datetime(df_savings['timestamp'])
        
        fig = px.line(df_savings, x='timestamp', y='savings',
                     title='Cumulative Energy Savings Over Time',
                     labels={'savings': 'Energy Saved (kWh)', 'timestamp': 'Time'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No savings data available yet. Start using the system to see analytics!")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Room efficiency comparison
    st.subheader("🏠 Room Efficiency Comparison")
    
    room_data = []
    for room_id, room in st.session_state.energy_monitor.rooms.items():
        room_data.append({
            'Room': room.name,
            'Occupancy Rate': random.uniform(0.3, 0.9),  # Simulated data
            'Energy Efficiency': random.uniform(0.6, 0.95),
            'Appliances Count': len(room.appliances),
            'Waste': room.get_energy_waste()
        })
    
    df_rooms = pd.DataFrame(room_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.bar(df_rooms, x='Room', y='Occupancy Rate',
                    title='Room Occupancy Rates',
                    color='Occupancy Rate',
                    color_continuous_scale='RdYlGn')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.bar(df_rooms, x='Room', y='Energy Efficiency',
                    title='Room Energy Efficiency',
                    color='Energy Efficiency',
                    color_continuous_scale='RdYlGn')
        st.plotly_chart(fig, use_container_width=True)
    
    # Energy consumption breakdown
    st.subheader("⚡ Energy Consumption Breakdown")
    
    consumption_data = []
    for room_id, room in st.session_state.energy_monitor.rooms.items():
        for appliance, status in room.appliances.items():
            if status:
                consumption_data.append({
                    'Room': room.name,
                    'Appliance': appliance,
                    'Consumption': random.uniform(0.1, 2.0)  # Simulated consumption
                })
    
    if consumption_data:
        df_consumption = pd.DataFrame(consumption_data)
        fig = px.sunburst(df_consumption, path=['Room', 'Appliance'], values='Consumption',
                         title='Energy Consumption by Room and Appliance')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No appliances currently running.")

def show_ml_model_interface():
    """Display ML model training and testing interface"""
    st.header("🤖 ML Model Training & Testing")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Model Training")
        
        # Simulate training data collection
        st.write("**Training Data Collection**")
        
        if st.button("Collect Training Sample", key="collect_sample"):
            # Simulate collecting a training sample
            sample = {
                'timestamp': datetime.now(),
                'room': st.session_state.selected_room,
                'is_occupied': random.choice([True, False]),
                'features': {
                    'light_level': random.uniform(0, 1),
                    'motion_detected': random.choice([True, False]),
                    'sound_level': random.uniform(0, 1),
                    'temperature': random.uniform(20, 30)
                }
            }
            st.session_state.ml_model_training_data.append(sample)
            st.success("Training sample collected!")
        
        st.write(f"**Training Samples Collected:** {len(st.session_state.ml_model_training_data)}")
        
        if st.button("Train Model", key="train_model") and st.session_state.ml_model_training_data:
            with st.spinner("Training model..."):
                time.sleep(3)
                st.success("Model training completed!")
        
        # Model performance metrics
        st.subheader("Model Performance")
        
        metrics = {
            'Accuracy': random.uniform(0.85, 0.95),
            'Precision': random.uniform(0.80, 0.90),
            'Recall': random.uniform(0.85, 0.95),
            'F1-Score': random.uniform(0.82, 0.92)
        }
        
        for metric, value in metrics.items():
            st.metric(metric, f"{value:.3f}")
    
    with col2:
        st.subheader("Model Testing")
        
        # Test image upload
        test_image = st.file_uploader("Upload Test Image", 
                                    type=['png', 'jpg', 'jpeg'], 
                                    key="test_image")
        
        if test_image is not None:
            st.image(test_image, caption="Test Image", use_column_width=True)
            
            if st.button("Test Model", key="test_model"):
                with st.spinner("Testing model..."):
                    time.sleep(2)
                    is_occupied, confidence, person_count = st.session_state.occupancy_detector.detect_occupancy()
                    
                    st.success("Model test completed!")
                    st.write(f"**Prediction:** {'Occupied' if is_occupied else 'Empty'}")
                    st.write(f"**Confidence:** {confidence:.1%}")
                    st.write(f"**Person Count:** {person_count}")
        
        # Model visualization
        st.subheader("Model Visualization")
        
        # Simulate model architecture visualization
        st.write("**Model Architecture:**")
        st.code("""
        Input Layer (Image) 
            ↓
        Convolutional Layers (CNN)
            ↓
        Feature Extraction
            ↓
        Dense Layers
            ↓
        Output Layer (Occupancy Classification)
        """)
        
        # Training progress
        if st.session_state.ml_model_training_data:
            progress = min(len(st.session_state.ml_model_training_data) / 100, 1.0)
            st.progress(progress)
            st.write(f"Training Progress: {progress:.1%}")

def show_energy_tips():
    """Display AI-powered energy saving tips"""
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    # Temperature threshold setting
    st.markdown("### 🌡️ Manual Temperature Threshold")
    st.session_state.temperature_threshold = st.slider(
        "Set Temperature Threshold (°C)",
        min_value=20.0,
        max_value=35.0,
        value=st.session_state.temperature_threshold,
        step=0.5,
        key="temp_threshold"
    )
    
    st.markdown(f'''
    <div style="background: #f8fafc; padding: 1rem; border-radius: 12px; margin: 1rem 0;">
        <p style="margin: 0; color: #334155; font-size: 0.875rem; font-weight: 600;">
            Current threshold: <strong style="color: #0f172a; font-weight: 800;">{st.session_state.temperature_threshold}°C</strong>
        </p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Generate tips button
    if st.button("💡 Generate My Energy Saving Tips", use_container_width=True):
        with st.spinner("🔄 Generating personalized AI-powered tips..."):
            time.sleep(1)
            st.session_state.energy_tips_generated = generate_energy_tips()
            st.rerun()
    
    # Display tips
    if st.session_state.energy_tips_generated:
        st.markdown("### ✨ Your Personalized Energy Tips")
        
        for i, tip in enumerate(st.session_state.energy_tips_generated):
            impact_colors = {
                'High': '#ef4444',
                'Medium': '#f59e0b',
                'Low': '#10b981'
            }
            
            st.markdown(f'''
            <div style="background: white; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1.5rem; margin: 1rem 0; border-left: 4px solid {impact_colors.get(tip['impact'], '#64748b')};">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1rem;">
                    <h4 style="margin: 0; color: #1e293b; font-size: 1.125rem;">{tip['title']}</h4>
                    <span style="background: {impact_colors.get(tip['impact'], '#64748b')}; color: white; padding: 0.25rem 0.75rem; border-radius: 20px; font-size: 0.75rem; font-weight: 600;">
                        {tip['impact']} IMPACT
                    </span>
                </div>
                <p style="color: #334155; margin: 0 0 1rem 0; line-height: 1.6; font-weight: 500;">{tip['description']}</p>
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="color: #10b981; font-weight: 600; font-size: 0.875rem;">💰 Savings: {tip['savings']}</span>
                </div>
            </div>
            ''', unsafe_allow_html=True)
    else:
        st.info("👆 Click the button above to generate your personalized energy saving tips!")
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_action_log():
    """Display action log for manual appliance controls"""
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    if not st.session_state.action_log:
        st.markdown('''
        <div class="info-card">
            <h4 style="margin: 0 0 0.5rem 0; font-size: 1.25rem;">📋 Action Log</h4>
            <p style="margin: 0; opacity: 0.9;">No actions recorded yet. Start controlling appliances to see them here!</p>
        </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown("### 📋 Recent Actions")
        
        for action in st.session_state.action_log[:10]:  # Show last 10 actions
            status_icon = "✅" if action['status'] else "❌"
            status_text = "ON" if action['status'] else "OFF"
            time_str = action['timestamp'].strftime("%H:%M:%S")
            
            st.markdown(f'''
            <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 1rem; margin: 0.5rem 0;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong style="color: #1e293b;">{action['type']}</strong> - {action['room']} - {action['appliance']}
                    </div>
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <span style="color: {'#10b981' if action['status'] else '#ef4444'}; font-weight: 600;">
                            {status_icon} {status_text}
                        </span>
                        <span style="color: #334155; font-size: 0.875rem; font-weight: 600;">{time_str}</span>
                    </div>
                </div>
            </div>
            ''', unsafe_allow_html=True)
    
    # Add summary
    if st.session_state.action_log:
        total_actions = len(st.session_state.action_log)
        recent_actions = [a for a in st.session_state.action_log if (datetime.now() - a['timestamp']).seconds < 3600]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Actions", total_actions)
        with col2:
            st.metric("Last Hour", len(recent_actions))
        with col3:
            on_actions = sum(1 for a in st.session_state.action_log if a['status'])
            st.metric("Turned ON", on_actions)
    
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
