# Smart Campus Energy Analyzer 

This project is a Python program created for the **Code2Xplore – 60 Days Challenge (Day 7)**.  
It analyzes energy consumption data from different campus buildings and generates an efficiency report.

## Project Overview
The Smart Campus Energy Analyzer processes a list of energy readings and classifies them into categories based on energy usage levels. The program also calculates total consumption and identifies inefficient energy patterns.

## Features
- Accepts multiple energy readings
- Classifies energy usage into categories
- Stores categorized data using a dictionary
- Calculates total energy consumption
- Detects:
  - Overconsumption
  - Balanced Usage
  - Energy Waste
- Displays a final energy efficiency report

## Technologies Used
- Python
- Lists
- Loops (`for`)
- Conditional Statements
- List Comprehension
- Dictionary
- Tuple

## Energy Classification Rules

| Energy Reading | Category |
|----------------|----------|
| `< 0` | Invalid |
| `0 – 50` | Efficient |
| `51 – 150` | Moderate |
| `> 150` | High Consumption |

## Example Input
[20, 70, 160, -5, 40, 120]
