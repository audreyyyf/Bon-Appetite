import React, { useState } from 'react';

function Inputs() {
  const [inputs, setInputs] = useState(['']);

  const handleChange = (index, event) => {
    const newInputs = [...inputs];
    newInputs[index] = event.target.value;
    setInputs(newInputs);
  };

  const addInput = () => {
    setInputs([...inputs, '']);
  };

  const removeInput = index => {
    const newInputs = [...inputs];
    newInputs.splice(index, 1);
    setInputs(newInputs);
  };

  return (
    <div className="InputPanel">
      <div className="InputLabel">
        <h2>Ingredients you want:</h2>
      </div>
      <div className="InputBoxes">
        {inputs.map((input, index) => (
          <div key={index}>
            <input className="input"
              type="text"
              value={input}
              onChange={event => handleChange(index, event)}
            />
            <button onClick={() => removeInput(index)}>Remove</button>
          </div>
        ))}
        <button  onClick={addInput}>Add Input</button>
      </div>
      <div className="InputLabel">
        <h2>Ingredients you can't have:</h2>
      </div>
      <div className="InputBoxes">
        {inputs.map((input, index) => (
          <div key={index}>
            <input className="input"
              type="text"
              value={input}
              onChange={event => handleChange(index, event)}
            />
            <button onClick={() => removeInput(index)}>Remove</button>
          </div>
        ))}
        <button  onClick={addInput}>Add Input</button>
      </div>

    </div>
  );
}

export default Inputs;
