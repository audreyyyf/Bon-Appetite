from flask import Flask, jsonify, request
from bs4 import BeautifulSoup as bs
from recipe_scrapers import scrape_me
from flask_cors import CORS



app = Flask(__name__)

CORS(app, origins=['http://localhost:3000'])

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get-recipes',  methods=['POST'])
def get_recipes_route():
    # Define inputs
    # Extract inputs from the request
    data = request.get_json()
    main = data.get('main', '')  # Example main ingredient
    want = data.get('want', [])   # Example list of ingredients the user wants
    dontWant = data.get('dontWant', [])  # Example list of ingredients the user doesn't want
    time_limit = data.get('time_limit', 100000)  # Example time limit

    # Print inputs for testing
    print("Main ingredient:", main)
    print("Want:", want)
    print("Don't want:", dontWant)
    print("Time limit:", time_limit)

    
     # Print inputs for testing
    print("Main ingredient:", main)
    print("Want:", want)
    print("Don't want:", dontWant)
    print("Time limit:", time_limit)

    # Call the web scraper function
    recipes = get_allrecipes(main, want, dontWant, time_limit)
    recipe1 = extract_recipe_info(results[0])

    return jsonify({'recipes': recipes} and recipe1)

def get_allrecipes(main, want, dontWant, time_limit):
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

# Function to extract info from recipes
def extract_recipe_info(recipe):
    website = scrape_me(recipe).host()
    recipe_name = scrape_me(recipe).title()
    total_time = scrape_me(recipe).total_time()
    servings = scrape_me(recipe).yields()
    image = scrape_me(recipe).image()
    return {'website': website, 'recipe_name': recipe_name, 'total_time': total_time, 'servings': servings, 'image': image}


def get_food52:
    # Food 52 Scrapper 

    main = "pasta"
    want = ['spinach']
    dontWant = ['olives'] 
    time_limit = 60

    scraper = scrape_me('https://food52.com/recipes/search?q='+main)

    #retrieves only the <a> tags from the page
    atags = scraper.links()

    # key to extract recipe dictionaries
    unique_key = 'collectable__img-link'
        
    # Extract dictionaries that only contain the recipe links
    recipes = [r for r in atags if unique_key in r.get('class', [])]

    # key to extract recipe links from dictionaries 
    link_key = 'href'
        
    # extract just the links from the dictionaries
    links = [k[link_key] for k in recipes]

    # append the base url to each recipe link
    base_url = 'https://food52.com'
    links = [base_url + link for link in links]

    # Array to store recipe links that meet the criteria
    link_matches = []

    # Iterate over recipe links that meet time and ingredient criteria
    for link in links:
        ingredients = scrape_me(link).ingredients()
        time = scrape_me(link).total_time()
        if check_ingredient_criteria(ingredients, want, dontWant) and (time <= time_limit):
            link_matches.append(link)
            

    link_matches