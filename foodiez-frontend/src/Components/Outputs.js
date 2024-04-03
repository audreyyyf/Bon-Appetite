import React, { useState } from 'react';


function Outputs({ recipes }) {
  if (!Array.isArray(recipes)) {
    console.log(recipes);
    console.log("not an array");
    return null; // or render a loading indicator or placeholder
 
  }
    return (
      <div className="OutputPanel">
        <div>
          <h2>Recipe Links:</h2>
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