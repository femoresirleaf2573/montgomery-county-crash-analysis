import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Montgomery County Crash Dashboard",
    page_icon="🚗",
    layout="wide"
)

st.title("Montgomery County Traffic Crash Dashboard")
st.write("Exploring traffic crash patterns from 2015 to 2026.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("dashboard_data.csv", low_memory=False)

    df = df.rename(columns={
        "Crash Date/Time": "Crash Date/Time",
        "ACRS Report Type": "ACRS Report Type",
        "Weather": "Weather"
    })

    df["Crash Date/Time"] = pd.to_datetime(
        df["Crash Date/Time"],
        format="%m/%d/%Y %I:%M:%S %p",
        errors="coerce"
    )

    df["Year"] = df["Crash Date/Time"].dt.year
    df["Hour"] = df["Crash Date/Time"].dt.hour

    return df


df = load_data()

# Sidebar year filter
years = sorted(df["Year"].dropna().unique().astype(int))

start_year, end_year = st.sidebar.slider(
    "Select year range",
    min_value=min(years),
    max_value=max(years),
    value=(min(years), 2025)
)

selected_severities = st.sidebar.multiselect(
    "Select crash severity",
    sorted(df["ACRS Report Type"].dropna().unique()),
    default=sorted(df["ACRS Report Type"].dropna().unique())
)

filtered_df = df[
    df["Year"].between(start_year, end_year)
    & df["ACRS Report Type"].isin(selected_severities)
]
# Summary statistics
total_crashes = len(filtered_df)
injury_crashes = (filtered_df["ACRS Report Type"] == "Injury Crash").sum()
fatal_crashes = (filtered_df["ACRS Report Type"] == "Fatal Crash").sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Crashes", f"{total_crashes:,}")
col2.metric("Injury Crashes", f"{injury_crashes:,}")
col3.metric("Fatal Crashes", f"{fatal_crashes:,}")

st.divider()

# Chart 1: Crashes by year
year_counts = (
    filtered_df.groupby("Year")
    .size()
    .reset_index(name="Crashes")
)

fig_year = px.line(
    year_counts,
    x="Year",
    y="Crashes",
    markers=True,
    title="Crashes by Year"
)

st.plotly_chart(fig_year, use_container_width=True)

# Chart 2: Crash severity
severity_counts = (
    filtered_df["ACRS Report Type"]
    .value_counts()
    .reset_index()
)
severity_counts.columns = ["Severity", "Crashes"]

fig_severity = px.bar(
    severity_counts,
    x="Severity",
    y="Crashes",
    title="Crashes by Severity",
    color="Severity"
)


# Chart 3: Crashes by hour
hour_counts = (
    filtered_df.groupby("Hour")
    .size()
    .reset_index(name="Crashes")
)

fig_hour = px.bar(
    hour_counts,
    x="Hour",
    y="Crashes",
    title="Crashes by Hour of Day"
)

left_col, right_col = st.columns(2)

with left_col:
    st.plotly_chart(fig_severity, width="stretch")

with right_col:
    st.plotly_chart(fig_hour, width="stretch")
st.caption("Source: Montgomery County Open Data - Crash Reporting Incidents")
# Clean inconsistent weather categories
weather = filtered_df["Weather"].fillna("Unknown").str.strip().str.upper()

weather = weather.replace({
    "RAINING": "RAIN",
    "SNOWING": "SNOW",
    "N/A": "UNKNOWN"
})

weather_counts = weather.value_counts().head(10).reset_index()
weather_counts.columns = ["Weather", "Crashes"]

fig_weather = px.bar(
    weather_counts,
    x="Weather",
    y="Crashes",
    title="Top 10 Weather Conditions During Crashes"
)

st.plotly_chart(fig_weather, width="stretch")

st.info(
    "Note: 2026 data is incomplete. The dataset currently ends on October 7, 2026. "
    "Weather categories describe recorded conditions, not necessarily crash causes."
)

st.divider()

st.subheader("Key Findings — Full Dataset")
st.caption("These findings describe all recorded crashes, regardless of the filters selected above.")
st.write(
    "• Property damage crashes make up the majority of recorded crashes."
)

st.write(
    "• Crash counts tend to be highest during afternoon commuting hours."
)

st.write(
    "• Recorded crashes decreased substantially in 2020 compared with 2019."
)

st.write(
    "• Most crashes occurred under clear weather conditions, "
    "but this does not mean clear weather causes more crashes."
)