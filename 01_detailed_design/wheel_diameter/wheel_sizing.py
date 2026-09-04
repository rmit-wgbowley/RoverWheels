"""
Filename: wheel_sizing.py

Description:
    Sizes the outer diameter of 
    the wheel based on system requirements.
"""

from math import pi
from pathlib import Path
from picounits import Parser, TIME

# Importing derived units notion for users.
ROOT_DIR = Path(__file__).resolve().parents[0]
Parser.import_derived(ROOT_DIR / "../derived.ut")

# Open simulation parameters
parameters = Parser.open(ROOT_DIR / "parameters.uiv")
day_in_seconds = 24 * 60 * 60 * TIME

diameter_range = parameters.req.max_diameter - parameters.req.min_diameter
steps = diameter_range // parameters.numerics.diameter_step

for index in range(0, int(steps)):
    # Computes the new diameter & circumference
    diameter = parameters.req.min_diameter + parameters.numerics.diameter_step * index
    circumference = 2 * pi * (diameter / 2)

    # Computes speed at fixed rpm and distance per day
    speed = circumference * parameters.drivetrain.max_frequency
    distance = speed * day_in_seconds

    # Checks if the speed is within the requirements
    valid = "*"
    if parameters.req.max_speed >= speed >= parameters.req.min_speed:
        valid = "x"

    print(
        f"[{valid}] Dia: {diameter}, "
        f"Circ: {circumference}, "
        f"Speed: {speed}, "
        f"m/day: [100%: {distance}, 75%: {distance * 3/4}, "
        f"50%: {distance * 1/2}, 25%: {distance * 1/4}]"
    )
