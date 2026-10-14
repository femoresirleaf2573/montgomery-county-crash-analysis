# Montgomery County Traffic Crash Analysis

## About This Project

For this project, I wanted to get more experience working with real-world data and see how I could use what I've been learning in Information Science outside of class.

I decided to look at traffic crashes in Montgomery County, Maryland, to see if there were any noticeable patterns. I was mainly interested in when crashes happen the most, how serious they tend to be, and whether things like weather or time of day showed any interesting trends.

I used a public dataset from Montgomery County that includes 126,010 reported crashes between January 2015 and October 2026.

I started by exploring the data in Python, then used SQL to practice writing queries and comparing results. After that, I built an interactive dashboard so the information would be easier to look through instead of just having a bunch of numbers and charts.

## Tools I Used

- **Python:** To work with the dataset and analyze the information
- **pandas:** To organize, filter, and group the data
- **Matplotlib:** To create charts showing different crash patterns
- **SQL and SQLite:** To query the dataset and check my results
- **Streamlit:** To build the interactive dashboard
- **Plotly:** To make charts that users can interact with
- **GitHub:** To save and organize my work

## What I Found

After going through the data, a few things stood out to me.

**1. Most crashes involved property damage.**

Out of the 126,010 crashes, 83,295 were classified as property damage crashes. There were also 42,307 injury crashes and 408 fatal crashes. Property damage made up about 66% of the total.

**2. Crashes happened more often in the afternoon.**

When I compared crashes by hour, I noticed that the numbers were especially high around 3 PM to 5 PM. This makes sense with people getting off work and traffic being heavier, although the dataset doesn't directly tell us why those crashes happened.

**3. There was a noticeable drop in crashes during 2020.**

In 2019, there were 11,665 reported crashes, compared to 8,070 in 2020. That was one of the biggest changes I noticed when looking at the yearly data. The timing lines up with the COVID-19 pandemic, although I can't say for sure how much of the decrease was caused by it.

**4. Most recorded crashes happened during clear weather.**

At first, I thought it was interesting that clear weather had so many more crashes than rain or snow. But I also realized that this doesn't necessarily mean clear weather is more dangerous. There could simply be more people driving when the weather is good.

## Cleaning the Data

One thing I noticed while working with the dataset was that some information wasn't recorded consistently.

For example, some weather conditions were labeled `CLEAR` while others were labeled `Clear`. I also found `RAINING` and `Rain`, even though they were describing the same general condition.

I used Python and SQL to combine those values so they wouldn't be counted as completely different categories.

This was a good reminder that even when you're using an official dataset, you still have to check the information before analyzing it.

## Interactive Dashboard

After finishing the initial analysis, I wanted to make something that would let people explore the data themselves.

I built a dashboard using Streamlit and Plotly. It lets users:

- Choose a range of years to look at
- Filter crashes by severity
- See how many total, injury, and fatal crashes were reported
- Compare crash totals across different years
- Look at crash patterns throughout the day
- Explore the weather conditions recorded during crashes

The charts update based on the filters selected.

## How to Run It

To run the dashboard on your own computer:

1. Clone or download this repository.
2. Install the Python packages using `pip install -r requirements.txt`.
3. Download the dataset from [Montgomery County Open Data](https://data.montgomerycountymd.gov/Public-Safety/Crash-Reporting-Incidents-Data/bhju-22kf).
4. Save the downloaded CSV as `data/crashes.csv`.
5. Open the project folder in your terminal and run `streamlit run dashboard.py`.

I didn't upload the full CSV file to GitHub because of its size.

## Things to Keep in Mind

There are a few limitations with this project.

The dataset includes records through October 7, 2026, so the 2026 numbers don't represent a full year. Some records also have missing information, and not every category was recorded consistently.

Another important thing is that the number of crashes under a certain condition doesn't automatically tell us how dangerous that condition is. For example, I would need additional information about traffic volume to make a fair comparison between daytime and nighttime driving.

## What I Learned

This project gave me a better understanding of what goes into working with a real dataset.

Before this, most of my experience with Python came from class assignments. This was an opportunity to use it for something different and work through the process of exploring data, checking for problems, writing SQL queries, and turning the results into visualizations.

I also got more comfortable using GitHub and learned how to build a basic interactive dashboard.

There are still things I want to improve as I get more experience, but this project helped me get started with data analysis and gave me something I can continue building on.

## Data Source

[Montgomery County Open Data — Crash Reporting Incidents](https://data.montgomerycountymd.gov/Public-Safety/Crash-Reporting-Incidents-Data/bhju-22kf)