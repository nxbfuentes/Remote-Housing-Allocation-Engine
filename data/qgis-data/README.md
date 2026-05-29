🗺️ Step 2: Spatial Layer Processing (QGIS)
Power BI lacks local coordinate math architectures. Processing geographic features inside QGIS first provides the essential infrastructure proximity variables.

🛠️ Direct Procedural Instructions
Initialize Your Environment: Open QGIS and create a blank workspace via Project -> New.

Ingest Greenfield Coordinates:

Navigate to Layer -> Add Layer -> Add Delimited Text Layer...

Select greenfield_base_points.csv. Target Name: Greenfield_Sites.

Ensure X Field is mapped to Longitude and Y Field to Latitude.

Set Geometry CRS to EPSG:4326 - WGS 84. Click Add and Close.

Establish Infrastructure Anchors:

Save a local flat file named critical_infrastructure_hubs.csv containing coordinates for key Western Australian regional service hubs (e.g., Broome Health Campus, Karratha Health Campus).

Ingest this file following the exact process above. Target Name: Infrastructure_Hubs.

Geodetic Vector Re-Projection (Crucial Step):

Why: Running direct geometry distance equations on EPSG:4326 returns inaccurate values in angular degrees instead of metrics like meters. We must re-project these into a modern meter-based Australian geodetic datum.

Right-click Greenfield_Sites -> Export -> Save Features As...

Name the output Greenfield_Projected and change the destination CRS to EPSG:7844 - GDA2020.

Repeat this step for Infrastructure_Hubs, saving the output as Infrastructure_Projected using EPSG:7844. Remove the original unprojected layers from your panel.

Execute Distance Matrix Math:

Open Vector -> Analysis Tools -> Distance Matrix.

Input Layer: Greenfield_Projected (Unique Key: Site_ID).

Target Layer: Infrastructure_Projected (Unique Key: Hub_ID).

Output Matrix Type: Linear distance matrix.

Check Use only the nearest (k) target points and set it to 1. Run the calculation tool.

Export Calculated Attributes:

Right-click the newly generated Distance Matrix scratch layer -> Export -> Save Features As...

Format: Comma Separated Value [CSV]. Save as spatial_greenfield_matrix.csv.

🏃‍♂️ Metric Scaling Script
Because the EPSG:7844 matrix outputs distances as raw meters, run a quick script in data generation 'matrix-standardiser.py'  to convert the values to standard kilometers before modeling, making a new csv filed called spatial_greenfield_matrix_standard.csv. 
