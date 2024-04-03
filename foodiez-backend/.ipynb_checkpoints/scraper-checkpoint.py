from flask import Flask
from bs4 import BeautifulSoup as bs
import requests
from recipe_scrapers import scrape_me

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
print("Backend script started");

# allrecipes scrapper

# the main dish or ingredient the user inputs
main = 'beef'

# default arrays of the ingredients the user wants and does not want
want = [] * 2
dontWant = [] * 3

# default time limit
time_limit = 100000

############  USER CHANGES THESE VALUES ^^ ONLY IF THEY PROVIDE INPUT, OTHERWISE LEAVE AS IS ##################################

def get_recipes(main, want, dontWant, time_limit):
    scraper = scrape_me('https://www.allrecipes.com/search?q='+ main)
    
    #retrieves only the <a> tags from the page
    atags = scraper.links()
    
    # key to extract recipe dictionaries
    unique_key = 'data-doc-id'
    
    # Extract dictionaries that only contain the recipe links
    recipes = [r for r in atags if unique_key in r]
    
    # key to extract recipe links from dictionaries 
    link_key = 'href'
    
    # extract just the links from the dictionaries
    links = [k[link_key] for k in recipes]
    
    # Function to check if recipes pass ingredient criteria
    def check_ingredient_criteria(ingredients, want, dontWant):
        for ingredient in want:
            if ingredient.lower() not in ''.join(ingredients).lower():
                return False
        for ingredient in dontWant:
            if ingredient.lower() in ''.join(ingredients).lower():
                return False
        return True

    # Array to store recipe links that meet the criteria
    link_matches = []

    # Iterate over recipe links that meet time and ingredient criteria
    for link in links:
        ingredients = scrape_me(link).ingredients()
        time = scrape_me(link).total_time()
        if check_ingredient_criteria(ingredients, want, dontWant) and (time <= time_limit):
            link_matches.append(link)

    return link_matches