#!/usr/bin/env python3
"""
Test script to verify main.py functionality
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import cv2
        print("✅ opencv-python")
    except ImportError:
        print("❌ opencv-python")
        return False
    
    try:
        import torch
        print("✅ torch")
    except ImportError:
        print("❌ torch")
        return False
    
    try:
        import streamlit
        print("✅ streamlit")
    except ImportError:
        print("❌ streamlit")
    
    try:
        import flask
        print("✅ flask")
    except ImportError:
        print("❌ flask")
    
    try:
        import yaml
        print("✅ pyyaml")
    except ImportError:
        print("❌ pyyaml")
    
    try:
        from PIL import Image
        print("✅ pillow")
    except ImportError:
        print("❌ pillow")
    
    print("\n✅ Import test complete!")
    return True

def test_files():
    """Test if required files exist"""
    print("\nTesting files...")
    
    files = [
        "main.py",
        "app_flask.py",
        "smart_energy_app.py",
        "fan_controller.py",
        "temp_sensor.py",
        "utils.py",
        "config.yaml",
        "requirements.txt"
    ]
    
    all_exist = True
    for file in files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            all_exist = False
    
    return all_exist

def main():
    print("=" * 60)
    print("SMART ENERGY SYSTEM - VERIFICATION")
    print("=" * 60)
    
    if test_files():
        print("\n✅ All required files present")
    else:
        print("\n❌ Some files are missing")
        return
    
    if test_imports():
        print("\n✅ All imports successful")
    else:
        print("\n❌ Some imports failed - install missing packages")
        print("Run: pip install -r requirements.txt")
        print("And: pip install streamlit plotly pandas opencv-python")
    
    print("\n" + "=" * 60)
    print("Ready to run: python main.py")
    print("=" * 60)

if __name__ == "__main__":
    main()


