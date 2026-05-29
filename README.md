# Remote-Housing-Allocation-Engine

🛠️ What the Project Does (The Mechanics)
The project builds an end-to-end data pipeline that acts as a Strategic Allocation Engine, processing data through three technical layers:


Generates Synthetic Asset & Greenfield Data (Python): It creates a realistic representation of the WA Department of Housing’s assets, generating thousands of records containing asset decay, refurbishment dates, and overcrowding indices, alongside potential new "greenfield" site coordinates.


Performs Spatial Proximity Drawing (QGIS): Because Power BI cannot natively calculate raw geographic coordinate math, the project uses QGIS to map the greenfield locations against existing infrastructure grids (schools, medical hubs). It calculates the exact distance matrix from proposed sites to these services and exports a clean geospatial matrix.


Models Strategic Funding Constraints (Power BI): It ingests both the internal housing ledger and the new QGIS spatial matrix into an optimized Star Schema. Using advanced DAX, it synthesizes this information to score locations and model future construction goals.

🎯 What the Project Achieves (The Business Value)
Instead of just displaying static charts, this framework achieves concrete operational and policy outcomes:

1. Pinpoints Optimal Greenfield Sites
By cross-referencing external spatial proximity data with Native Title Status, the project automatically highlights the most viable land for expansion. It isolates locations with "Pending" titles to protect capital, while highlighting "Approved" areas that are close to vital utility grids.

2. Balances Refurbishments vs. Brand New Builds
The Department faces a constant trade-off: Do we fix an existing house or build a new one? The project achieves an automated way to balance this by creating a Funding Priority Index (FPI). This measure ranks funding urgency based on:

Severe overcrowding indices.

Length of time since the property was last refurbished.

Proximity to critical education and healthcare services.

3. Maps Out a Clear Path to "Closing the Gap" Milestones
The framework introduces a Target Velocity Tracker. This allows executives to use a timeline slider (e.g., aiming for the 2031 benchmark) to see exactly how many houses must be constructed per quarter in specific greenfield zones to successfully de-escalate remote overcrowding indices in time.

🏁 Summary of Strategic Impact
Ultimately, this project achieves evidence-based decision-making. It proves to a hiring panel that you understand public sector data isn't just about writing code—it’s about turning disparate, messy geospatial and structural data into an automated pipeline that puts "good homes" where they are needed most, ensuring optimal community outcomes under a highly constrained government budget.


🏗️ Phase 1: Python Data Generation
We will need a Python script to build two distinct, cross-referenced CSV files.
📋 The Two Datasets We Are Creating:
📋 Data Schema Design
Dataset A: Internal Asset Ledger (internal_asset_ledger.csv)

Business Context: Represents a 5,000-record snapshot of existing social housing assets across Western Australia.

Columns: House_ID, Community_Name, Region (e.g., Kimberley, Pilbara, Goldfields), Current_Overcrowding_Index (scaled 1–10), Last_Refurbished_Date, Asset_Condition_Score.

Dataset B: External Greenfield Opportunities (greenfield_base_points.csv)

Business Context: Sourced external regional candidate points for potential new structural construction plots.

Columns: Site_ID, Proposed_Region, Latitude, Longitude, Native_Title_Status (Approved vs. Pending).