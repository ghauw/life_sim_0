import math
import random


class LifeEngine:
    def __init__(self, microbes, resources=100, seed=None):
        if seed is not None:
            random.seed(seed)  # Seed for reproducibility
        self.microbes = microbes
        self.resources = resources
        self.time_step = 0  # To be used for time-dependent functions like sine

        # Randomly initialize variables instead of hardcoded values
        self.growth_factor_base = random.uniform(0.01, 0.1)
        self.reproduction_base_rate = random.uniform(0.02, 0.1)
        self.reproduction_amplitude = random.uniform(0.01, 0.05)
        self.max_age = random.randint(80, 120)
        self.resource_depletion_rate = random.uniform(0.01, 0.1)

    def sigmoid_growth(self, growth_rate):
        return 1 / (1 + math.exp(-growth_rate))

    def sine_reproduction(self, time_step):
        # Sine function adjusted with random base rate and amplitude
        return self.reproduction_base_rate + self.reproduction_amplitude * math.sin(0.1 * time_step)

    def grow(self):
        for microbe in self.microbes:
            if microbe['alive'] and self.resources > 0:
                growth_factor = self.sigmoid_growth(
                    microbe['growth_rate']) * self.growth_factor_base
                microbe['growth_rate'] += growth_factor
                self.resources -= growth_factor * self.resource_depletion_rate

    def reproduce(self):
        new_microbes = []
        for microbe in self.microbes:
            if microbe['alive'] and self.resources > 0:
                reproduction_chance = self.sine_reproduction(self.time_step)
                if random.random() < reproduction_chance:
                    new_microbe = {
                        "type": "Microbe",
                        "age": 0,
                        "alive": True,
                        "growth_rate": microbe['growth_rate'],
                        # Ensure position is inherited or new one is generated
                        "x": microbe.get('x', random.uniform(0, 800)),
                        "y": microbe.get('y', random.uniform(0, 600))
                    }
                    new_microbes.append(new_microbe)
                    self.resources -= 1
        self.microbes.extend(new_microbes)

    def death(self):
        for microbe in self.microbes:
            if microbe['age'] > self.max_age or self.resources <= 0:
                microbe['alive'] = False

    def apply_life_cycle(self):
        print(
            f"Starting lifecycle with {len(self.microbes)} microbes and {self.resources} resources.")
        self.grow()
        self.reproduce()
        self.death()
        self.time_step += 1
        print(
            f"After lifecycle: {len([m for m in self.microbes if m['alive']])} alive, {len(self.microbes)} total")
