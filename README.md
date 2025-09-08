# 🚀 Motor Control App

A Python Kivy-based GUI application for controlling and monitoring a motor system. This app includes a login system, RPM control, emergency stop, live data monitoring, and scheduling features — all designed with future Bluetooth integration in mind.

---

## 📦 Features

### 🔐 Login System
- Secure login screen with username and password inputs
- Default credentials: `admin / admin`
- Invalid login triggers a popup alert

### 🎛 Motor Control Panel
- RPM control slider (0–5000)
- Live RPM display
- Emergency STOP button with instant feedback

### 📊 Live Data Monitoring
- Simulated temperature and current readings
- Auto-updates every 2 seconds
- Placeholder for future Bluetooth sensor data

### ⏰ Scheduling Feature
- Define `OnTime` and `OffTime` (HH:MM format)
- Background time checks every minute
- Console logs for scheduled motor ON/OFF events

### 📡 Bluetooth Integration (Planned)
- Placeholder for pybluez or similar library
- Future support for:
  - Sending commands: `RPM:<value>`, `STOP`, `ON`, `OFF`
  - Receiving sensor data: Temperature, Current, RPM

---

## 🛠 Installation

### Requirements
- Python 3.7+
- Kivy

### Install Dependencies
```bash
pip install kivy
