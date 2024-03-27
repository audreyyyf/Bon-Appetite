import React, { useState } from 'react';


function Outputs({ links }) {
    return (
      <div className="OutputPanel">
        <h2> Here is your shit</h2>
        <div>
          <h2>Recipe Links:</h2>
          <ul>
            {links.map((link, index) => (
              <li key={index}>
                <a href={link} target="_blank" rel="noopener noreferrer">{link}</a>
              </li>
            ))}
          </ul>
        </div>
      </div>
    );
  }
  
  export default Outputs;