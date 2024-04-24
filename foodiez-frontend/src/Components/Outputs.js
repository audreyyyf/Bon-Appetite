import React, { useState } from 'react';
import Logo from '../Images/Logo.png'; 
import { Carousel } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';


function Outputs({ recipes, loading }) {

  console.log('Recipes prop:', recipes);

  if (!recipes || typeof recipes !== 'object') {
    console.log("Invalid recipes object");
    return null; // or render a loading indicator or placeholder
  }



 
  if (loading) {
    return (
      <div className="OutputPanel">
        <div className="loading-image">
          <img src={Logo} alt="Loading..." />
        </div>
      </div>
    );
  }


  const { allrecipesArray, food52Array, delishArray, myRecipesArray } = recipes;
  
  console.log("allrecipesArray:", allrecipesArray);
  console.log("food52Array", food52Array);
  console.log("delishArray", delishArray);
  console.log("myRecipesArray", myRecipesArray);
  const allEmpty = allrecipesArray.length === 0 && food52Array.length === 0 && delishArray.length === 0 && myRecipesArray.length === 0;
  return (
    <div className="OutputPanel">
      <div>
        <h2>Recipe Links:</h2>
        {allEmpty ? (
          <p>Recipes will show up here</p>
        ) : (
          <div className="container">
            <div className="row">
              {allrecipesArray.length > 0 && (
                <div className="col">
                  <h3>AllRecipes</h3>
                  <Carousel>
                    {allrecipesArray.map((recipe, index) => (
                      <Carousel.Item key={index}>
                        <a href={recipe} target="_blank" rel="noopener noreferrer">{recipe}</a>
                      </Carousel.Item>
                    ))}
                  </Carousel>
                </div>
              )}
              {food52Array.length > 0 && (
                <div className="col">
                  <h3>Food52</h3>
                  <Carousel>
                    {food52Array.map((recipe, index) => (
                      <Carousel.Item key={index}>
                        <a href={recipe} target="_blank" rel="noopener noreferrer">{recipe}</a>
                      </Carousel.Item>
                    ))}
                  </Carousel>
                </div>
              )}
              {delishArray.length > 0 && (
                <div className="col">
                  <h3>Delish</h3>
                  <Carousel>
                    {delishArray.map((recipe, index) => (
                      <Carousel.Item key={index}>
                        <a href={recipe} target="_blank" rel="noopener noreferrer">{recipe}</a>
                      </Carousel.Item>
                    ))}
                  </Carousel>
                </div>
              )}
              {myRecipesArray.length > 0 && (
                <div className="col">
                  <h3>My Recipes</h3>
                  <Carousel>
                    {myRecipesArray.map((recipe, index) => (
                      <Carousel.Item key={index}>
                        <a href={recipe} target="_blank" rel="noopener noreferrer">{recipe}</a>
                      </Carousel.Item>
                    ))}
                  </Carousel>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Outputs;