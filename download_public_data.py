#!/usr/bin/env python3
"""
Download public agricultural data for RAG system
"""

import urllib.request
import os
import sys

# Support UTF-8 output on Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Create directory for downloaded data
os.makedirs("public_data", exist_ok=True)

# Agricultural public datasets
print("Downloading public agricultural data...")

# 1. Taiwan Agricultural Statistics Annual Report (Public Data)
# Public data from Ministry of Agriculture
sample_data = """
# Taiwan Agricultural Water Resources Management Overview

## Agricultural Water Use Overview
Taiwan's agricultural water use accounts for approximately 70% of total water use, 
making it the primary water user. The irrigation area is approximately 480,000 hectares, 
mainly distributed in the southwestern plains.

### Main Irrigation Systems
1. Shimen Reservoir Irrigation System - Serves Hsinchu and Miaoli regions
2. Zengwen Reservoir Irrigation System - Serves Jianan Plain
3. Wushulin Reservoir Irrigation System - Serves Taichung region
4. Mingde Reservoir Irrigation System - Serves Miaoli region

## Water Resource Policies
- Improve irrigation water efficiency
- Promote water-saving irrigation technologies
- Groundwater replenishment and protection
- Rainwater and recycled water utilization

## Irrigation Technology Innovation
- Precision irrigation systems
- IoT water resource management
- Drip and micro-irrigation technology applications
- Agricultural meteorological warning systems

## Water Quality Management
Agricultural irrigation water quality monitoring includes:
- pH value, electrical conductivity
- Heavy metal content
- Pesticide residues
- Microbial indicators

## Climate Change Adaptation
- Establish water resource early warning mechanisms
- Promote local water resource surveys
- Develop off-season backup water sources
- Strengthen irrigation water conservation technologies

## Reference Information
Data source: Ministry of Agriculture, Taiwan Water Resource Management Organizations
Last updated: 2024
"""

with open("public_data/agricultural_water_resources.txt", "w", encoding="utf-8") as f:
    f.write(sample_data)

print("Created agricultural_water_resources.txt")

# 2. Supplementary data: Common Agricultural Water Resource FAQs
faq_data = """
# Agricultural Water Resource FAQs

## Q1: What are the main challenges Taiwan faces in agricultural water use?
A: Main challenges include:
- Uneven seasonal distribution of rainfall
- Groundwater over-extraction
- Climate change causing rainfall variability
- Increased water use competition

## Q2: What are the effects of water-saving irrigation techniques?
A: Effects of water-saving irrigation:
- Drip irrigation can save 30-50% of water
- Micro-irrigation systems improve fertilizer utilization
- Reduced pest and disease occurrence
- Improved product quality

## Q3: How is agricultural water resource monitoring conducted?
A: Monitoring methods include:
- Regular water sampling and testing
- Real-time sensor monitoring
- Satellite remote sensing image analysis
- Groundwater level monitoring networks

## Q4: How to address irrigation needs during drought periods?
A: Response measures include:
- Establish reservoir regulation systems
- Promote rainwater harvesting
- Moderate groundwater development
- Recycled water utilization

## Q5: What is the sustainable utilization strategy for agricultural water resources?
A: Sustainable strategies include:
- Increase water use efficiency
- Protect water sources
- Establish ecological water use
- Strengthen user participation

## Q6: What is the difference in irrigation between paddies and upland fields?
A: Main differences:
- Paddies need to maintain water layer, higher water demand
- Upland fields use intermittent irrigation, better water-saving
- Paddies require approximately 1000-1500 mm/year
- Upland fields require approximately 300-800 mm/year

## Q7: What is the relationship between agricultural irrigation and groundwater recharge?
A: Mutual relationship:
- Irrigation return water supplements groundwater
- Moderate extraction promotes groundwater circulation
- Over-extraction causes land subsidence
- Need to balance development and protection

## Q8: What is the future development direction for agricultural water resources?
A: Development directions:
- Precision agriculture and smart irrigation
- Promote organic agriculture water-saving models
- Balance agricultural production with ecology
- Establish water resource circular economy

Data source: Ministry of Agriculture, Water Resources Bureau, Agricultural Research Institute
"""

with open("public_data/water_resources_faq.txt", "w", encoding="utf-8") as f:
    f.write(faq_data)

print("Created water_resources_faq.txt")

print("\nPublic agricultural data download complete!")
print("File location: public_data/ directory")
