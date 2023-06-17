import pandas as pd
from googlesearch import search

# Load the Excel sheet
df = pd.read_excel('names.xlsx')

# Iterate over each name in the sheet
for name in df['Full Name']:
    # Generate a search query for the LinkedIn profile
    query = f"LinkedIn {name}"
    
    # Perform the search
    for link in search(query, num_results=1):
        # Extract the LinkedIn profile link
        if "linkedin.com/in/" in link:
            linkedin_url = link
            break
    else:
        linkedin_url = "No LinkedIn profile found"
    
    # Print the name and LinkedIn profile link
    print(f"{name}: {linkedin_url}")
