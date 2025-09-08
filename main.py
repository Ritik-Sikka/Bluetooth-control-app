from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.clock import Clock
from datetime import datetime
import random

# Default credentials
USERNAME = "admin"
PASSWORD = "admin"

# Scheduling times
OnTime = "19:35"
OffTime = "19:36"

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        login_button = Button(text='Login', on_press=self.validate_login)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_button)
        self.add_widget(layout)

    def validate_login(self, instance):
        if self.username_input.text == USERNAME and self.password_input.text == PASSWORD:
            self.manager.current = 'control'
        else:
            Popup(title='Error',
                  content=Label(text='Invalid Username/Password'),
                  size_hint=(None, None), size=(300, 200)).open()

class ControlScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rpm_value = 0
        self.temperature = "--"
        self.current = "--"

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        layout.add_widget(Label(text='Motor Control Panel', font_size=24))

        # RPM Slider
        self.rpm_label = Label(text='RPM: 0')
        self.rpm_slider = Slider(min=0, max=5000, value=0)
        self.rpm_slider.bind(value=self.update_rpm)
        layout.add_widget(self.rpm_label)
        layout.add_widget(self.rpm_slider)

        # Emergency Stop
        stop_button = Button(text='Emergency STOP', background_color=(1, 0, 0, 1))
        stop_button.bind(on_press=self.emergency_stop)
        layout.add_widget(stop_button)

        # Live Data
        self.temp_label = Label(text='Temperature: -- °C')
        self.current_label = Label(text='Current: -- A')
        layout.add_widget(self.temp_label)
        layout.add_widget(self.current_label)

        # Schedule
        self.schedule_label = Label(text=f'Schedule → ON: {OnTime}, OFF: {OffTime}')
        layout.add_widget(self.schedule_label)

        self.add_widget(layout)

        # Start updates
        Clock.schedule_interval(self.update_live_data, 2)
        Clock.schedule_interval(self.check_schedule, 60)

    def update_rpm(self, instance, value):
        self.rpm_value = int(value)
        self.rpm_label.text = f'RPM: {self.rpm_value}'
        print(f'Send to motor: RPM:{self.rpm_value}')  # Placeholder for Bluetooth

    def emergency_stop(self, instance):
        print("Send to motor: STOP")  # Placeholder for Bluetooth
        Popup(title='Emergency',
              content=Label(text='Motor stopped immediately!'),
              size_hint=(None, None), size=(300, 200)).open()

    def update_live_data(self, dt):
        self.temperature = round(random.uniform(30.0, 90.0), 2)
        self.current = round(random.uniform(1.0, 10.0), 2)
        self.temp_label.text = f'Temperature: {self.temperature} °C'
        self.current_label.text = f'Current: {self.current} A'

    def check_schedule(self, dt):
        now = datetime.now().strftime("%H:%M")
        if now == OnTime:
            print("Motor ON (scheduled)")
            # Placeholder: Send Bluetooth command "ON"
        elif now == OffTime:
            print("Motor OFF (scheduled)")
            # Placeholder: Send Bluetooth command "OFF"

class MotorControlApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(ControlScreen(name='control'))
        return sm

if __name__ == '__main__':
    MotorControlApp().run()