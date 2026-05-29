### 📊 Step 3: Data Modeling & Optimization (Power BI)

#### 📐 Relationship Architecture (Star Schema)

To keep the analytical model highly performant, transform the flat-file connections into a clean **Star Schema**.

* **Fact Table:** `internal_asset_ledger` (5,000 unique housing profiles).
* **Dimension Table:** `spatial_greenfield_matrix` (Geospatial candidate properties).
* **Conformed Dimension:** Build a single, unique `Dim_Region` table using DAX or Power Query (`Dim_Region = DISTINCT(internal_asset_ledger[Region])`). Connect both the Fact and spatial Dimension tables to this region master via clean **1-to-Many (1:*) single-direction relationships**.

```
┌───────────────────────────┐
│  spatial_greenfield_matrix│
└──────────────┬────────────┘
               │ *
               │
               │ 1
┌──────────────┴────────────┐
│         Dim_Region        │
└──────────────┬────────────┘
               │ 1
               │
               │ *
┌──────────────┴────────────┐
│   internal_asset_ledger   │
└───────────────────────────┘

```

#### 🧮 Advanced DAX Formula Implementations

##### Metric 1: The Funding Priority Index (FPI)

This measure synthesizes operational overcrowding with physical asset degradation and proximity risks to generate a unified priority score from 1 to 100.

```dax
Funding Priority Index = 
VAR AvgOvercrowding = AVERAGE(internal_asset_ledger[Current_Overcrowding_Index])
VAR AvgCondition = AVERAGE(internal_asset_ledger[Asset_Condition_Score])
VAR AvgProximity = AVERAGE(spatial_greenfield_matrix[Proximity_To_Infrastructure_KM])

-- Normalize and reverse condition scores (Lower physical condition scores indicate urgent risk)
VAR ConditionWeight = (11 - AvgCondition) * 3.5
VAR OvercrowdingWeight = AvgOvercrowding * 4.5
VAR SpatialIsolationWeight = IF(ISBLANK(AvgProximity), 0, MIN(AvgProximity * 0.5, 20))

RETURN
IF(
    ISBLANK(AvgOvercrowding),
    BLANK(),
    ConditionWeight + OvercrowdingWeight + SpatialIsolationWeight
)

```

##### Metric 2: Closing the Gap Target Velocity Tracker

This formula dynamically calculates the quarterly building production rate required to clear regional high-overcrowding backlogs based on an executive timeline slicer.

```dax
Target Velocity Tracker = 
VAR SelectedMilestoneYear = SELECTEDVALUE('Target Year Parameter'[Target Year Parameter], 2031)
VAR CurrentYear = YEAR(TODAY())
VAR YearsRemaining = SelectedMilestoneYear - CurrentYear
VAR QuartersRemaining = YearsRemaining * 4

-- Count total severe assets with an overcrowding index threshold above 7
VAR HighRiskBacklog = CALCULATE(
    COUNT(internal_asset_ledger[House_ID]), 
    internal_asset_ledger[Current_Overcrowding_Index] >= 7
)

RETURN
IF(
    QuartersRemaining <= 0,
    HighRiskBacklog,
    DIVIDE(HighRiskBacklog, QuartersRemaining, 0)
)

```
