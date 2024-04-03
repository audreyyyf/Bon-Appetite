import React, { useState } from 'react';

import Inputs from './Inputs.js'
import Outputs from './Outputs.js';

function InputAndOutput() {
  const [recipes, setRecipes] = useState([]);

  const handleRecipesChange = (newRecipes) => {
    setRecipes(newRecipes);
  };

  return (
    <div className="InputAndOutput">
      <Inputs onDataReceived={handleRecipesChange} />
      <Outputs recipes={recipes} />
    </div>
  );
}

export default InputAndOutput;
