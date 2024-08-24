import time
import math


class Logger:
    def __init__(self, log_file='simulation_log.txt', metrics_to_log=None):
        self.log_file = log_file
        self.metrics_to_log = metrics_to_log if metrics_to_log is not None else []
        self.start_time = time.time()

        # Initialize log file
        with open(self.log_file, 'w') as file:
            file.write("Simulation Log\n")
            file.write("==============\n")

    def log(self, physics_engine):
        current_time = time.time() - self.start_time
        logs = [f"Time: {current_time:.2f}s"]

        if "bodies" in self.metrics_to_log:
            logs.append(f"Bodies: {len(physics_engine.bodies)}")

        if "live_microbes" in self.metrics_to_log and any(b['type'] == 'Microbe' for b in physics_engine.bodies):
            live_microbes = len(
                [m for m in physics_engine.bodies if m['type'] == 'Microbe' and m['alive']])
            logs.append(f"Live Microbes: {live_microbes}")

        if "mean_velocity" in self.metrics_to_log and self.supports_velocity(physics_engine.bodies):
            mean_velocity = self.calculate_mean_velocity(physics_engine.bodies)
            logs.append(f"Mean Velocity: {mean_velocity:.2f}")

        if "rms_velocity" in self.metrics_to_log and self.supports_velocity(physics_engine.bodies):
            rms_velocity = self.calculate_rms_velocity(physics_engine.bodies)
            logs.append(f"RMS Velocity: {rms_velocity:.2f}")

        if "total_energy" in self.metrics_to_log and self.supports_energy(physics_engine.bodies):
            total_energy = self.calculate_total_energy(physics_engine.bodies)
            logs.append(f"Total Energy: {total_energy:.2f}")

        log_entry = " | ".join(logs)

        # Print to console (optional)
        print(log_entry)

        # Append to log file
        with open(self.log_file, 'a') as file:
            file.write(log_entry + "\n")

    def supports_velocity(self, bodies):
        # Check if bodies have velocity attributes
        return all('vx' in body and 'vy' in body for body in bodies)

    def supports_energy(self, bodies):
        # Check if bodies have energy-related attributes
        return all('mass' in body and 'vx' in body and 'vy' in body for body in bodies)

    def calculate_mean_velocity(self, bodies):
        if not bodies or not self.supports_velocity(bodies):
            return 0
        total_velocity = sum(
            math.sqrt(body['vx']**2 + body['vy']**2) for body in bodies)
        return total_velocity / len(bodies)

    def calculate_rms_velocity(self, bodies):
        if not bodies or not self.supports_velocity(bodies):
            return 0
        total_velocity_squared = sum(
            body['vx']**2 + body['vy']**2 for body in bodies)
        return math.sqrt(total_velocity_squared / len(bodies))

    def calculate_total_energy(self, bodies):
        if not bodies or not self.supports_energy(bodies):
            return 0
        total_energy = sum(
            0.5 * body['mass'] * (body['vx']**2 + body['vy']**2) for body in bodies)
        return total_energy
