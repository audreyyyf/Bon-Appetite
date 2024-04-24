import React, { useState } from 'react';

import Inputs from './Inputs.js'
import Outputs from './Outputs.js';

function InputAndOutput() {
  const [recipes, setRecipes] = useState({ allrecipesArray: [], food52Array: [], delishArray: [], myRecipesArray: [] });
  const [loading, setLoading] = useState(false);

  const handleRecipesChange = (newRecipes) => {
    setRecipes(newRecipes);
    console.log('New recipes data:', newRecipes); // Log the received data
  };



  return (
    <div className="InputAndOutput">
      <Inputs onDataReceived={handleRecipesChange} setLoading={setLoading} />
      <Outputs recipes={recipes}  loading={loading} />
    </div>
  );
}

export default InputAndOutput;
