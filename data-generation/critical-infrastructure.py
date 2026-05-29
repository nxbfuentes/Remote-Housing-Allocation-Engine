import pandas as pd
import os

os.makedirs("data", exist_ok=True)

# Define high-value critical infrastructure anchor hubs across regional WA
infrastructure_data = [
    # Kimberley Hubs
    {
        "Hub_ID": "INF-001",
        "Hub_Name": "Broome Regional Health Campus",
        "Facility_Type": "Health",
        "Region": "Kimberley",
        "Latitude": -17.9544,
        "Longitude": 122.2361,
    },
    {
        "Hub_ID": "INF-002",
        "Hub_Name": "Kununurra District High School",
        "Facility_Type": "Education",
        "Region": "Kimberley",
        "Latitude": -15.7736,
        "Longitude": 128.7384,
    },
    # Pilbara Hubs
    {
        "Hub_ID": "INF-003",
        "Hub_Name": "Karratha Health Campus",
        "Facility_Type": "Health",
        "Region": "Pilbara",
        "Latitude": -20.7383,
        "Longitude": 116.8415,
    },
    {
        "Hub_ID": "INF-004",
        "Hub_Name": "Hedland Senior High School",
        "Facility_Type": "Education",
        "Region": "Pilbara",
        "Latitude": -20.3175,
        "Longitude": 118.5925,
    },
    # Goldfields Hubs
    {
        "Hub_ID": "INF-005",
        "Hub_Name": "Kalgoorlie Regional Hospital",
        "Facility_Type": "Health",
        "Region": "Goldfields",
        "Latitude": -30.7410,
        "Longitude": 121.4646,
    },
    {
        "Hub_ID": "INF-006",
        "Hub_Name": "Leonora Community Health Centre",
        "Facility_Type": "Health",
        "Region": "Goldfields",
        "Latitude": -28.8851,
        "Longitude": 121.3292,
    },
    # Mid West Hubs
    {
        "Hub_ID": "INF-007",
        "Hub_Name": "Geraldton Regional Hospital",
        "Facility_Type": "Health",
        "Region": "Mid West",
        "Latitude": -28.7770,
        "Longitude": 114.6144,
    },
    {
        "Hub_ID": "INF-008",
        "Hub_Name": "Meekatharra District High School",
        "Facility_Type": "Education",
        "Region": "Mid West",
        "Latitude": -26.5933,
        "Longitude": 118.4984,
    },
    # Gascoyne Hubs
    {
        "Hub_ID": "INF-009",
        "Hub_Name": "Carnarvon Health Campus",
        "Facility_Type": "Health",
        "Region": "Gascoyne",
        "Latitude": -24.8826,
        "Longitude": 113.6622,
    },
    {
        "Hub_ID": "INF-010",
        "Hub_Name": "Exmouth District High School",
        "Facility_Type": "Education",
        "Region": "Gascoyne",
        "Latitude": -21.9322,
        "Longitude": 114.1264,
    },
]

# Convert to DataFrame
df_infra = pd.DataFrame(infrastructure_data)

# Save to your workspace directory
df_infra.to_csv("data/critical_infrastructure_hubs.csv", index=False)

print(
    "✨ Success: 'critical_infrastructure_hubs.csv' generated with regional WA hub coordinates."
)
