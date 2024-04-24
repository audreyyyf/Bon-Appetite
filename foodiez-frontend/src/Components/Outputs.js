import React, { useState } from 'react';
import Logo from '../Images/Logo.png'; 
import Carousel from 'react-bootstrap/Carousel';

function Outputs({ recipes, loading }) {

  console.log('Recipes prop:', recipes);

  if (!recipes || typeof recipes !== 'object') {
    console.log("Invalid recipes object");
    return null; // or render a loading indicator or placeholder
  }

  const { allrecipesArray, food52Array } = recipes;
  
  console.log("allrecipesArray:", allrecipesArray);
  console.log("food52Array", food52Array);
  return (
    <div className="OutputPanel">
      <div>
        <h2>Recipe Links:</h2>
        {loading && (
          <div className="loading-image">
            <img src={Logo} alt="Loading..." />
          </div>
        )}
        <div className="container">
          <div className="row">
            <div className="col">
              <h3>AllRecipes</h3>
              <Carousel >
                {allrecipesArray.map((recipe, index) => (
                  <Carousel.Item key={index}>
                    <a href={recipe} target="_blank" rel="noopener noreferrer">{recipe}</a>
                    
                  </Carousel.Item>
                ))}
              </Carousel>
            </div>
            <div className="col">
              <h3>Food52</h3>
              <Carousel >
                {food52Array.map((recipe, index) => (
                  <Carousel.Item key={index}>
                    <a href={recipe} target="_blank" rel="noopener noreferrer">{recipe}</a>
                    
                  </Carousel.Item>
                ))}
              </Carousel>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Outputs;