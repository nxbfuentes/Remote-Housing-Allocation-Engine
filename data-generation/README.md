📋 Data Schema Design
Dataset A: Internal Asset Ledger (internal_asset_ledger.csv)

Business Context: Represents a 5,000-record snapshot of existing social housing assets across Western Australia.

Columns: House_ID, Community_Name, Region (e.g., Kimberley, Pilbara, Goldfields), Current_Overcrowding_Index (scaled 1–10), Last_Refurbished_Date, Asset_Condition_Score.

Dataset B: External Greenfield Opportunities (greenfield_base_points.csv)

Business Context: Sourced external regional candidate points for potential new structural construction plots.

Columns: Site_ID, Proposed_Region, Latitude, Longitude, Native_Title_Status (Approved vs. Pending).