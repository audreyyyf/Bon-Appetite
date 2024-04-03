import React, { useState } from 'react';
import Logo from '../Images/Logo.png'; 

function Outputs({ recipes, loading }) {

  if (!Array.isArray(recipes)) {
    console.log(recipes);
    console.log("not an array");
    return null; // or render a loading indicator or placeholder
 
  }
    return (
      <div className="OutputPanel">
        <div>
          <h2>Recipe Links:</h2>
          {loading && (
          <div className="loading-image">
            <img src={Logo} alt="Loading..." />
          </div>
        )}
          <ul>
            {recipes.map((recipe, index) => (
              <li key={index}>
                <a href={recipe} target="_blank" rel="noopener noreferrer">{recipe}</a>
              </li>
            ))}
          </ul>
        </div>
      </div>
    );
  }
  
  export default Outputs;