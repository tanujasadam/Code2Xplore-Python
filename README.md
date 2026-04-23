# Autonomous Smart City Data Intelligence System

##  Overview
This project is part of the Code2Xplore – 60 Days Challenge (Day 7).  
It simulates a smart city environment by generating and analyzing multi-source sensor data such as traffic density, air quality index (AQI), and energy consumption.

The system uses Python and Data Science tools to analyze, classify, and predict risk zones for better urban decision-making.

##  Objectives
- Simulate smart city data using random values  
- Store data using list of dictionaries  
- Perform analysis using NumPy and Pandas  
- Classify zones into risk categories  
- Detect high-risk patterns  
- Implement a custom risk scoring system  

##  Features
- Data simulation for multiple zones  
- Conversion to Pandas DataFrame  
- Matrix operations using NumPy  
- Risk score calculation  
- Zone classification (Safe, High Risk, Energy Critical)  
- Identify top 3 worst zones  
- Pattern detection and analysis  

##  Data Format
Each record contains:

{
    "zone": int,
    "traffic": int (0–100),
    "air_quality": int (0–300),
    "energy": int (0–500)
}

##  Technologies Used
- Python  
- Pandas  
- NumPy  
- random module  
- math module  

##  Risk Score Formula
risk_score = (traffic * 0.4 + AQI * 0.4 + energy * 0.2)

##  Classification Rules
- AQI > 200 OR traffic > 80 → High Risk  
- energy > 400 → Energy Critical  
- traffic < 30 AND AQI < 100 → Safe Zone  

##  Output
- DataFrame with processed data  
- Categorized zones  
- Top 3 worst zones  
- Risk statistics (max, avg, min)  
- Final system decision:
  - City Stable  
  - Moderate Risk  
  - High Alert  
  - Critical Emergency  

##  Test Cases
- Extreme pollution  
- Zero traffic  
- Random spikes  

##  Personalization Applied
- Dataset shuffled based on register number rule  
- Custom risk formula used  
- Manual sorting implemented (without sort_values())  

## Project Structure
Smart-City-Data-System/
│── main.py  
│── README.md  
│── output/ (optional)

##  How to Run

git clone https://github.com/your-username/smart-city-system.git  
cd smart-city-system  
python main.py  

## Learning Outcomes
- Learned data analysis using Pandas and NumPy  
- Understood real-world data simulation  
- Built custom logic for classification  
- Improved problem-solving skills  


##  Unique Insight
A smart city is defined by how efficiently it uses data to improve safety, sustainability, and quality of life.
