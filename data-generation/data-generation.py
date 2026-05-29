import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuration & Random Seed Seed Initialization
np.random.seed(42)
random.seed(42)
record_count = 5000
greenfield_count = 150

regions = ["Kimberley", "Pilbara", "Goldfields", "Mid West", "Gascoyne"]
communities = {
    "Kimberley": ["Ardyaloon", "Beagle Bay", "Bidyadanga", "Warmun", "Kalumburu"],
    "Pilbara": ["Yandeyarra", "Jigalong", "Cheeditha", "Wakathuni"],
    "Goldfields": ["Coonana", "Tjuntjuntjara", "Wongatha Wonganarra"],
    "Mid West": ["Mungullah", "Pia Wadjari", "Yulga Jinna"],
    "Gascoyne": ["Carnarvon Reserve", "Burringurrah"],
}

# --- 1. GENERATE DATASET A: INTERNAL ASSET LEDGER ---
asset_data = []
for i in range(1, record_count + 1):
    region = random.choice(regions)
    community = random.choice(communities[region])
    overcrowding = int(np.clip(np.random.normal(5.5, 2.2), 1, 10))
    condition = int(np.clip(np.random.normal(6.0, 1.8), 1, 10))

    # Back-calculate a refurbishment date based on condition logic
    years_ago = random.randint(0, 15) if condition > 4 else random.randint(12, 30)
    refurb_date = (
        datetime.now() - timedelta(days=years_ago * 365 + random.randint(0, 364))
    ).strftime("%Y-%m-%d")

    asset_data.append(
        {
            "House_ID": f"HSG-{i:05d}",
            "Community_Name": community,
            "Region": region,
            "Current_Overcrowding_Index": overcrowding,
            "Last_Refurbished_Date": refurb_date,
            "Asset_Condition_Score": condition,
        }
    )

df_assets = pd.DataFrame(asset_data)
df_assets.to_csv("internal_asset_ledger.csv", index=False)

# --- 2. GENERATE DATASET B: EXTERNAL GREENFIELD OPPORTUNITIES ---
# Approximate bounding coordinate grids matching WA geographic bounds
wa_bounds = {
    "Kimberley": {"lat": (-18.0, -14.0), "lon": (122.0, 128.5)},
    "Pilbara": {"lat": (-23.5, -20.5), "lon": (116.0, 121.0)},
    "Goldfields": {"lat": (-31.0, -26.0), "lon": (121.0, 126.0)},
    "Mid West": {"lat": (-29.0, -26.0), "lon": (114.5, 118.0)},
    "Gascoyne": {"lat": (-26.0, -23.5), "lon": (113.5, 116.0)},
}

greenfield_data = []
for j in range(1, greenfield_count + 1):
    region = random.choice(regions)
    bounds = wa_bounds[region]
    lat = round(random.uniform(bounds["lat"][0], bounds["lat"][1]), 5)
    lon = round(random.uniform(bounds["lon"][0], bounds["lon"][1]), 5)
    native_title = random.choices(["Approved", "Pending"], weights=[0.65, 0.35])[0]

    greenfield_data.append(
        {
            "Site_ID": f"GF-SITE-{j:03d}",
            "Proposed_Region": region,
            "Latitude": lat,
            "Longitude": lon,
            "Native_Title_Status": native_title,
        }
    )

df_greenfield = pd.DataFrame(greenfield_data)
df_greenfield.to_csv("greenfield_base_points.csv", index=False)

print("✨ Phase 1 Success: Data layers written to CSV workspace formats.")

