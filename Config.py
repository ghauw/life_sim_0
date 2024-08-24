class Config:
    def __init__(self,
                 num_bodies: int = 0,
                 gravitational_constant: float = 0.0,
                 initial_population: int = 0,
                 growth_rate: float = 0.0,
                 reproduction_rate: float = 0.0,
                 death_rate: float = 0.0,
                 charge_interaction: float = 0.0,
                 universe_type: str = ''):
        self.num_bodies = num_bodies
        self.gravitational_constant = gravitational_constant
        self.initial_population = initial_population
        self.growth_rate = growth_rate
        self.reproduction_rate = reproduction_rate
        self.death_rate = death_rate
        self.charge_interaction = charge_interaction
        self.universe_type = universe_type
