from googlesearch import search
import pandas as pd

query = input("Enter your search query: ").strip()
print(f"Searching Google for: {query}...\n")

results = []
try:
    for url in search(query, num_results=5):
        results.append(url)
except Exception as e:
    print("Error while searching:", e)
    exit()

# Prepare correct column structure for email follow-up
df = pd.DataFrame({
    'Name': [f'Team {i+1}' for i in range(len(results))],
    'Email': ['' for _ in range(len(results))],  # Empty emails to fill manually
    'Link': results
})

output_path = "sample_data/leads.csv"
df.to_csv(output_path, index=False)

print(f"\n Leads saved to: {output_path}")
print(df.to_string(index=False))  # This prints all rows, 

