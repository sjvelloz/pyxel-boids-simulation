# Pyxel Boids Simulation

A 2D aquarium simulation and flocking algorithm built with Python and [Pyxel](https://github.com/kitao/pyxel).

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pyxel](https://img.shields.io/badge/Pyxel-Engine-FF0044?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<p align="center">
  <img src="boid.gif" alt="Aquarium Simulation Demo" width="700"/>
</p>

## Overview

This project simulates autonomous fish movement using an emergent flocking behavior (inspired by Craig Reynolds' Boids model). Each fish reacts dynamically to surrounding entities in real time, steering and aligning its velocity vector with nearby neighbors.

To render smooth movement in a retro pixel-art engine, the sprites are drawn dynamically as oriented triangles using custom trigonometric calculations (`math.atan2`, `sin`, `cos`) based on each entity's velocity.

### Prerequisites

Ensure you have Python installed on your system (version 3.8 or higher).

### Installation

1. Clone this repository
2. Navigate into the project directory
3. Install required dependencies (`pip install pyxel`)
4. Run the file `main.py`
