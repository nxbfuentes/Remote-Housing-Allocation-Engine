import pandas as pd

df_matrix = pd.read_csv("data/qgis-data/spatial_greenfield_matrix.csv")
# QGIS default field output names are typically 'InputID', 'TargetID', and 'Distance'
df_matrix.rename(columns={'InputID': 'Site_ID', 'Distance': 'Proximity_To_Infrastructure_KM'}, inplace=True)
df_matrix['Proximity_To_Infrastructure_KM'] = df_matrix['Proximity_To_Infrastructure_KM'] / 1000.0

# Re-merge the spatial metrics with your original greenfield fields
df_base = pd.read_csv("data/greenfield_base_points.csv")
df_final_spatial = pd.merge(df_base, df_matrix[['Site_ID', 'Proximity_To_Infrastructure_KM']], on='Site_ID', how='left')

df_final_spatial.to_csv("data/qgis-data/spatial_greenfield_matrix_standard.csv", index=False)
print("🏁 Phase 2 Success: Spatial distances scaled to standard Kilometers.")