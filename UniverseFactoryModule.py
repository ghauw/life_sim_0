from Config import Config


class UniverseFactoryModule:
    def create_universe(self, universe_type):
        universe_type = universe_type.strip().lower()

        if universe_type == "":
            print("No input provided. Defaulting to 'Cosmic System'.")
            universe_type = "cosmic system"
        elif universe_type not in ["cosmic system", "microbial system", "atomic system"]:
            print(
                f"Unknown universe type: '{universe_type}'. Defaulting to 'Cosmic System'.")
            universe_type = "cosmic system"

        if universe_type == "cosmic system":
            return Config(
                num_bodies=self.get_valid_integer(
                    "Enter the number of celestial bodies (e.g., 50): ", default=50),
                gravitational_constant=self.get_valid_float(
                    "Enter the gravitational constant (e.g., 6.67430e-11): ", default=6.67430e-11),
                universe_type="Cosmic System"
            )
        elif universe_type == "microbial system":
            return Config(
                initial_population=self.get_valid_integer(
                    "Enter the initial population of microbes (e.g., 100): ", default=100),
                growth_rate=self.get_valid_float(
                    "Enter the growth rate (e.g., 0.1): ", default=0.1),
                reproduction_rate=self.get_valid_float(
                    "Enter the reproduction rate (e.g., 0.05): ", default=0.05),
                death_rate=self.get_valid_float(
                    "Enter the death rate (e.g., 0.02): ", default=0.02),
                universe_type="Microbial System"
            )
        elif universe_type == "atomic system":
            return Config(
                num_bodies=self.get_valid_integer(
                    "Enter the number of atoms (e.g., 100): ", default=100),
                charge_interaction=self.get_valid_float(
                    "Enter the charge interaction factor (e.g., 1.0): ", default=1.0),
                universe_type="Atomic System"
            )

    def get_valid_integer(self, prompt, default):
        user_input = input(prompt)
        if user_input == "":  # Handle empty input
            return default
        try:
            value = int(user_input)
            return value if value > 0 else default
        except ValueError:
            print("Invalid input. Using default value.")
            return default

    def get_valid_float(self, prompt, default):
        user_input = input(prompt)
        if user_input == "":  # Handle empty input
            return default
        try:
            value = float(user_input)
            return value if value > 0 else default
        except ValueError:
            print("Invalid input. Using default value.")
            return default
