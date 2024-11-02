# GitHub Users in Delhi

This repository contains data about GitHub users in Delhi with over 100 followers and their repositories. 

GitHub Data Scraper: This project leverages GitHub’s API to retrieve and analyze repository and user data, offering insights into developer trends and engagement. The gitscrap.py script performs data scraping tasks, focusing on user activity and repository statistics to uncover meaningful patterns. Insights from this analysis highlight key areas for optimizing developer workflows and enhancing project visibility. 

Data Scraping Process: The gitscrap.py script connects to the GitHub API, retrieving comprehensive datasets on both repositories and users. Utilizing Python’s requests library, the script iteratively fetches data by navigating through pagination to ensure the capture of all relevant records. Each data point is parsed and organized into a structured format before saving it as a CSV for analysis.

## Files

1. `users.csv`: Contains information about 425 GitHub users in Delhi with over 100 followers
2. `repositories.csv`: Contains information about 30074 public repositories from these users
3. `gitscrap.py`: Python script used to collect this data

## Data Collection

- Data collected using GitHub API
- Date of collection: 2024-10-29
- Only included users with 100+ followers
- Up to 500 most recently pushed repositories per user
I used the GitHub API and Python scripts to gather data on Delhi-based users with over 100 followers, iterating through profile pages to collect comprehensive details.

## Interesting Insight

Found that developers associated with educational institutions are among the most popular in Delhi’s GitHub community.
Repositories with higher fork counts tend to show consistent activity and maintenance, which often correlates with longer-term project relevance.


## Developer Recommendation

Contributing to popular open-source repositories and being associated with an educational institution may help increase followers and visibility.
Open issues and welcoming contribution guidelines significantly increase engagement rates, leading to a more robust project lifecycle.
