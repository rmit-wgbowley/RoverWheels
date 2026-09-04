### 01_detailed_design

All detailed design was conducted using Python with the `picounits` type system for dimensional analysis and parameter files.

---

### Wheel Sizing Model

This analytical model uses the maximum and minimum allowed diameters and the maximum drivetrain RPM to calculate the resulting velocity for different percentages of on-time, where distance is given by $d = v \cdot t$.

<div align="center"><img src="../03_media/detailed_design_output.png" alt="Wheel Sizing" style="max-width: 600px">
<p><em>Figure 1: Resulting table showing speeds for the full validated diameter range.</em></p></div>

The model contains the following parameters, which were used to construct the table:

```uiv
[numerics]
diameter_step: 5 m(m)

# ----------------------------

[req]
max_diameter: 130 m(m)
min_diameter: 80 m(m)

max_speed: 0.07 (m*s^-1)
min_speed: 0.041 (m*s^-1)

# ----------------------------

[drivetrain]
max_frequency: 0.167 (s^-1)

# ----------------------------
```

> Model: [wheel_sizing](./wheel_diameter/wheel_sizing.py)  
> Parameters: [parameters.uiv](./wheel_diameter/parameters.uiv)

---