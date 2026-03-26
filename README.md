# vehicle-performance-analyzer

This project analyzes vehicle acceleration using force-time data based on Newton’s Second Law (F = ma).

# Overview
The program allows users to input force values at specific time intervals and calculates the corresponding acceleration of a vehicle.

It then visualizes the results using a graph.

# Features
- User input for time and force values
- Acceleration calculation using F = ma
- Data validation using try-except blocks
- Graph visualization (Acceleration vs Time)
- Automatic saving of the graph as an image

# Example Output

![Acceleration Graph](acceleration_vs_time.png)

# Technical Details
- Language: Python
- Libraries: matplotlib
- Concepts used:
  - Lists
  - Loops
  - Exception handling
  - Basic physics (Newton’s Law)

# How to Run
1. Install matplotlib if not installed:
pip install matplotlib
2. Run the script:
python vehicle_performance_analyzer.py
3. Enter values in this format:
time,force
Example:
0,500
1,1200
2,2000
3,2800
4,3200
5,3500
6,3600

Type "stop" when finished.

# Purpose
This project was built to combine programming with basic engineering principles, specifically vehicle dynamics and force analysis.

It demonstrates practical use of Python in engineering problem-solving.
