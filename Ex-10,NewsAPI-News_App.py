import requests

# Prompt the user to input the type of news they are interested in
query = input("What type of news are you interested in? ")

# Replace 'your_api_key' with your actual API key from NewsAPI
api_key = '0aa6e3a31374438080d83d640c8fa0f4'
# Construct the URL for the NewsAPI request with the user's query
url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api_key}"

# Make a GET request to the NewsAPI
response = requests.get(url)

# Parse the JSON response
news = response.json()

# Check if the request was successful
if response.status_code == 200:
    # Iterate through the list of articles and print their titles and descriptions
    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("--------------------------------------")
else:
    print(f"Error: {news['message']}")
