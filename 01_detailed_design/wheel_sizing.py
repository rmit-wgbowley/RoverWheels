"""
Filename: wheel_sizing.py

Description:
    Sizes the outer diameter of 
    the wheel based on system requirements.
"""

from pathlib import Path
from picounits import Parser

# Importing derived units notion for users.
ROOT_DIR = Path(__file__).resolve().parents[0]
Parser.import_derived(ROOT_DIR / "derived.ut")
