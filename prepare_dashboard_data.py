import pandas as pd

# Load the original dataset
df = pd.read_csv("data/crashes.csv", low_memory=False)

# Keep the columns needed for the dashboard
columns = [
    "Crash Date/Time",
    "ACRS Report Type",
    "Weather"
]

dashboard_data = df[columns].copy()

# Save a smaller copy for the online dashboard
dashboard_data.to_csv("dashboard_data.csv", index=False)

print("Dashboard data created!")
print("Total rows:", len(dashboard_data))
print("Columns:", dashboard_data.columns.tolist())