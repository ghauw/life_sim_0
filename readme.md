# Sayan Simulation

This project is a simulation environment using Pygame to model different types of systems: Cosmic, Microbial, and Atomic. The simulation includes custom rendering, physics, and logging.

## Project Structure

- **main.py**: The entry point of the simulation.
- **Renderer.py**: Handles the rendering of all bodies in the simulation.
- **PhysicsEngine.py**: Applies physics rules based on the selected universe type.
- **LifeEngine.py**: Manages growth, reproduction, and death in the microbial system.
- **LoggerEngine.py**: Logs metrics such as time, body count, and velocities.
- **SimulationConfig.py**: Configures the simulation based on user or random input.
- **UniverseFactoryModule.py**: Creates different types of universes (Cosmic, Microbial, Atomic).
- **test_simulation.py**: Runs multiple iterations of the simulation for testing purposes.

## How to Run

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd sayan_sim

