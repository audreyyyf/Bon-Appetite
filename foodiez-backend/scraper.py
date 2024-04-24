from flask import Flask, jsonify, request
from bs4 import BeautifulSoup as bs
from recipe_scrapers import scrape_me
from flask_cors import CORS
from queue import Queue
import threading
import time



app = Flask(__name__)

CORS(app, origins=['http://localhost:3000'])

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

    
    # Create queues for storing results
    allrecipes_queue = Queue()
    food52_queue = Queue()
    delish_queue = Queue()


    # Create threads for each function
    thread_allrecipes = threading.Thread(target=get_allrecipes, args=(main, want, dontWant, time_limit, allrecipes_queue ))
    thread_food52 = threading.Thread(target=get_food52, args=(main, want, dontWant, time_limit, food52_queue))
    thread_delish = threading.Thread(target=get_delish, args=(main, want, dontWant, time_limit, delish_queue))

    # Start threads
    thread_allrecipes.start()
    thread_food52.start()
    thread_delish.start()

    # Wait for threads to complete
    thread_allrecipes.join()
    thread_food52.join()
    thread_delish.join()

        # Get results from queues
    allrecipes_result = allrecipes_queue.get()
    food52_result = food52_queue.get()
    delish_result = delish_queue.get()

    return jsonify(allrecipes_result=allrecipes_result, food52_result=food52_result, delish_result=delish_result)
    #return jsonify({'allrecipes': allrecipes_result, 'food52': food52_result})

    

def get_allrecipes(main, want, dontWant, time_limit, result_queue):
    # AllRecipes Scraper
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

    result_queue.put(link_matches)
    return



def get_food52(main, want, dontWant, time_limit, result_queue):
    # Food 52 Scraper 
    scraper = scrape_me('https://food52.com/recipes/search?q='+main)
    atags = scraper.links()
    unique_key = 'collectable__img-link' 
    recipes = [r for r in atags if unique_key in r.get('class', [])]
    link_key = 'href'    
    links = [k[link_key] for k in recipes]
    base_url = 'https://food52.com'
    links = [base_url + link for link in links]
    link_matches = []
    for link in links:
        ingredients = scrape_me(link).ingredients()
        time = scrape_me(link).total_time()
        if check_ingredient_criteria(ingredients, want, dontWant):
            link_matches.append(link)

    result_queue.put(link_matches)
    return

# Delish Scrapper


def get_delish(main, want, dontWant, time_limit, result_queue):
    scraper = scrape_me('https://www.delish.com/search/?q=' + main)

    #retrieves only the <a> tags from the page
    atags = scraper.links()
    atags

    # key to extract recipe dictionaries
    unique_key = 'data-vars-ga-outbound-link'
        
    # Extract dictionaries that only contain the recipe links
    recipes = [r for r in atags if unique_key in r]
        
    # key to extract recipe links from dictionaries 
    link_key = 'href'
        
    # extract just the links from the dictionaries
    links = [k[link_key] for k in recipes]
    links

    # append the base url to each recipe link
    base_url = 'https://www.delish.com/'
    links = [base_url + link for link in links]

    # Array to store recipe links that meet the criteria
    link_matches = []

    for link in links:
        ingredients = scrape_me(link).ingredients()
        time = scrape_me(link).total_time()
        if check_ingredient_criteria(ingredients, want, dontWant) and (time <= time_limit):
            link_matches.append(link)

    result_queue.put(link_matches)


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

