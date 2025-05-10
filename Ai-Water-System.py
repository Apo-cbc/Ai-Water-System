import random
import time

class SmartWaterSystem:
    def __init__(self):
        self.pressure = 50
        self.flow_rate = 100
        self.energy_usage = 0

    def detect_leak(self, flow_rate, pressure):
        leak_detected = flow_rate > 120 or pressure < 30
        return leak_detected

    def adjust_pressure(self, current_hour):
        if 6 <= current_hour <= 9 or 18 <= current_hour <= 22:
            self.pressure = 70
        else:
            self.pressure = 40

    def calculate_energy_usage(self):
        self.energy_usage += self.pressure * 0.05

    def simulate_operation(self, duration_hours=24):
        for hour in range(duration_hours):
            self.adjust_pressure(hour)
            simulated_flow = random.randint(80, 130)
            leak = self.detect_leak(simulated_flow, self.pressure)

            print(f"Hour {hour}: Pressure={self.pressure} psi, Flow={simulated_flow} L/min")

            if leak:
                print(f"  ⚠️ Leak detected at hour {hour}! Immediate action required!")
            
            self.calculate_energy_usage()
            time.sleep(0.1) 

        print(f"Total Energy Usage: {self.energy_usage:.2f} kWh")

if __name__ == '__main__':
    system = SmartWaterSystem()
    system.simulate_operation()
