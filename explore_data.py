from pathlib import Path

Path("visualizations").mkdir(exist_ok=True)
import pandas as pd

# Load the crash data
df = pd.read_csv("data/crashes.csv", low_memory=False)

# Count rows and columns
print("Total rows:", len(df))
print("Total columns:", len(df.columns))
print(df["Crash Date/Time"].head(5).to_list())
# Convert crash dates
dates = pd.to_datetime(
    df["Crash Date/Time"],
    format="%m/%d/%Y %I:%M:%S %p",
    errors="coerce"
)
print("Unparsed dates:", dates.isna().sum())
print("\nEarliest crash:", dates.min())
print("Latest crash:", dates.max())

# Count crash report types
print("\nCrash report types:")
print(df["ACRS Report Type"].value_counts())

# Check missing values
print("\nMissing values by column:")
print(df.isnull().sum().sort_values(ascending=False))

# Check duplicate report numbers
print("\nDuplicate report numbers:")
print(df["Report Number"].duplicated().sum())


# Count crashes by year
df["Crash Year"] = dates.dt.year

yearly_crashes = df["Crash Year"].value_counts().sort_index()

print("\nCrashes by year:")
print(yearly_crashes)


import matplotlib.pyplot as plt

# Exclude incomplete year 2026
complete_years = yearly_crashes[yearly_crashes.index < 2026]

# Create chart
plt.figure(figsize=(11, 6))

bars = plt.bar(
    complete_years.index,
    complete_years.values,
    color="#2563EB"
)

# Add crash counts above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 100,
        f"{int(height):,}",
        ha="center",
        fontsize=9
    )

plt.title("Montgomery County Traffic Crashes (2015–2025)", fontsize=15)
plt.xlabel("Year")
plt.ylabel("Number of Reported Crashes")

plt.xticks(complete_years.index)
plt.ylim(0, 14000)
plt.grid(axis="y", alpha=0.2)

plt.tight_layout()

# Save image
plt.savefig("visualizations/crashes_by_year.png", dpi=300)

plt.show()

# Analyze crashes by day of the week
df["Day of Week"] = dates.dt.day_name()

# Put the days in the correct order
days = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

# Count crashes for each day
daily_crashes = df["Day of Week"].value_counts()

# Reorder the results
daily_crashes = daily_crashes.reindex(days)

print("\nCrashes by day of the week:")
print(daily_crashes)


# Create a chart for crashes by weekday
plt.figure(figsize=(10, 6))

bars = plt.bar(
    daily_crashes.index,
    daily_crashes.values,
    color="#2563EB"
)

# Add crash counts above the bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 150,
        f"{int(height):,}",
        ha="center",
        fontsize=10
    )

plt.title("Montgomery County Traffic Crashes by Day of Week", fontsize=14)
plt.xlabel("Day of Week")
plt.ylabel("Number of Reported Crashes")

plt.ylim(0, 23000)
plt.grid(axis="y", alpha=0.2)
plt.tight_layout()

# Save the chart
plt.savefig("visualizations/crashes_by_weekday.png", dpi=300)

plt.show()

# Analyze crashes by hour of the day
df["Crash Hour"] = dates.dt.hour

# Count crashes during each hour
hourly_crashes = df["Crash Hour"].value_counts()

# Put the hours in order from 0 to 23
hourly_crashes = hourly_crashes.sort_index()

print("\nCrashes by hour of the day:")
print(hourly_crashes)

# Create a chart for crashes by hour
plt.figure(figsize=(12, 6))

plt.bar(
    hourly_crashes.index,
    hourly_crashes.values,
    color="#2563EB"
)

plt.title("Montgomery County Traffic Crashes by Hour", fontsize=15)
plt.xlabel("Hour of Day (24-Hour Clock)")
plt.ylabel("Number of Reported Crashes")

# Show all 24 hours on the x-axis
plt.xticks(range(24))

plt.ylim(0, 10500)
plt.grid(axis="y", alpha=0.2)
plt.tight_layout()

# Save the chart
plt.savefig("visualizations/crashes_by_hour.png", dpi=300)

plt.show()

# Analyze crash severity
severity_counts = df["ACRS Report Type"].value_counts()

# Calculate the percentage for each category
severity_percentages = (
    severity_counts / len(df)
) * 100

print("\nCrash severity percentages:")
print(severity_percentages.round(2))

# Create a chart for crash severity
plt.figure(figsize=(10, 5))

bars = plt.barh(
    severity_percentages.index,
    severity_percentages.values,
    color=["#2563EB", "#E69F00", "#D55E5E"]
)

# Add percentage labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 0.5,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.2f}%",
        va="center"
    )

plt.title("Montgomery County Crashes by Severity", fontsize=15)
plt.xlabel("Percentage of Reported Crashes")
plt.ylabel("Crash Type")

plt.xlim(0, 75)
plt.gca().invert_yaxis()
plt.grid(axis="x", alpha=0.2)
plt.tight_layout()

plt.savefig("visualizations/crashes_by_severity.png", dpi=300)

plt.show()
