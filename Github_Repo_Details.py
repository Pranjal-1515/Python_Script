import requests
import pandas as pd

# Fetch public repositories for the provided username.
url = f"https://api.github.com/users/Pranjal-1515/repos"
response = requests.get(url)
repos = response.json()

# Prepare a list with the repo details.
data = []
for repo in repos:
    data.append({
        "Name": repo["name"],
        "URL": repo["html_url"],
        "Description": repo["description"],
        "Stars": repo["stargazers_count"]
    })

# Create and export the Excel file.
df = pd.DataFrame(data)
excel_file = "github_repos.xlsx"
df.to_excel(excel_file, index=False)
print(f"Excel file '{excel_file}' created successfully!")
