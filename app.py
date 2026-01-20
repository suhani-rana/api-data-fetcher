import requests
import csv

def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: API request failed")
        return []

    return response.json()

def save_to_csv(posts):
    with open("posts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "title", "body"])

        for post in posts[:20]:  # only saving first 20 posts
            writer.writerow([post["id"], post["title"], post["body"]])

    print("Saved data to posts.csv")

if __name__ == "__main__":
    print("Fetching data from API...")
    posts_data = get_posts()

    if posts_data:
        save_to_csv(posts_data)
