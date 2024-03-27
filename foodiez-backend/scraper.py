from flask import Flask, jsonify
from bs4 import BeautifulSoup as bs
from recipe_scrapers import scrape_me

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get-recipes')
def get_recipes_route():
    # Define inputs
    main = 'beef'  # Example main ingredient
    want = []  # Example list of ingredients the user wants
    dontWant = []  # Example list of ingredients the user doesn't want
    time_limit = 100000  # Example time limit

    # Call the web scraper function
    recipes = get_recipes(main, want, dontWant, time_limit)

    return jsonify({'recipes': recipes})

def get_recipes(main, want, dontWant, time_limit):
    scraper = scrape_me('https://www.allrecipes.com/search?q=' + main)
    atags = scraper.links()
    unique_key = 'data-doc-id'
    recipes = [r for r in atags if unique_key in r]
    link_key = 'href'
    links = [k[link_key] for k in recipes]

    link_matches = []
    for link in links:
        ingredients = scrape_me(link).ingredients()
        time = scrape_me(link).total_time()
        if check_ingredient_criteria(ingredients, want, dontWant) and (time <= time_limit):
            link_matches.append(link)

    return link_matches

def check_ingredient_criteria(ingredients, want, dontWant):
    for ingredient in want:
        if ingredient.lower() not in ''.join(ingredients).lower():
            return False
    for ingredient in dontWant:
        if ingredient.lower() in ''.join(ingredients).lower():
            return False
    return True

if __name__ == '__main__':
    print("Backend script started")
    app.run(debug=True)
