#!/user/bin/env python
# -*- coding: utf-8 -*-


class AlarmSensor:
    def run(self):
        print("Alarm Ring...")
class WaterSprinker:
    def run(self):
        print("Spray Water...")
class EmergencyDialer:
    def run(self):
        print("Dial 119...")

"""
if __name__=="__main__":
    alarm_sensor=AlarmSensor()
    water_sprinker=WaterSprinker()
    emergency_dialer=EmergencyDialer()
    alarm_sensor.run()
    water_sprinker.run()
    emergency_dialer.run()
"""

class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor=AlarmSensor()
        self.water_sprinker=WaterSprinker()
        self.emergency_dialer=EmergencyDialer()
    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()

if __name__=="__main__":
    emergency_facade=EmergencyFacade()
    emergency_facade.runAll()
