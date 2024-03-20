
import React, { useState } from 'react';
import '../App.css'; // Import the CSS file

function Inputs() {
  const [inputs1, setInputs1] = useState(['']);

  const handleChange1 = (index, event) => {
    const newInputs = [...inputs1];
    newInputs[index] = event.target.value;
    setInputs1(newInputs);
  };

  const addInput1 = () => {
    setInputs1([...inputs1, '']);
  };

  const removeInput1 = index => {
    const newInputs = [...inputs1];
    newInputs.splice(index, 1);
    setInputs1(newInputs);
  };

  const [inputs2, setInputs2] = useState(['']);

  const handleChange2 = (index, event) => {
    const newInputs = [...inputs2];
    newInputs[index] = event.target.value;
    setInputs2(newInputs);
  };

  const addInput2 = () => {
    setInputs2([...inputs2, '']);
  };

  const removeInput2 = index => {
    const newInputs = [...inputs2];
    newInputs.splice(index, 1);
    setInputs2(newInputs);
  };

  return (
    <div className="InputPanel">
      <div className="InputSection1">
        <div className="InputLabel">
          <h2>Ingredients you want:</h2>
        </div>
        <div className="InputBoxes">
          {inputs1.map((input, index) => (
            <div key={index}>
              <input className="input"
                type="text"
                value={input}
                onChange={event => handleChange1(index, event)}
              />
              <button onClick={() => removeInput1(index)}>Remove</button>
            </div>
          ))}
          <button  onClick={addInput1}>Add Input</button>
        </div>
      </div>
      <div className="InputSection2">
        <div className="InputLabel">
          <h2>Ingredients you can't have:</h2>
        </div>
        <div className="InputBoxes">
          {inputs2.map((input, index) => (
            <div key={index}>
              <input className="input"
                type="text"
                value={input}
                onChange={event => handleChange2(index, event)}
              />
              <button onClick={() => removeInput2(index)}>Remove</button>
            </div>
          ))}
          <button  onClick={addInput2}>Add Input</button>
        </div>
        <div className="InputLabel">
            <h2> How much time you have: </h2>
        </div>
      </div>
      <div class="InputSliders">
        <input type="range" min="1" max="100"  class="slider" id="slider1" style={{ backgroundColor: 'black', border: '1px solid #4CAF50' }} />
        <input type="range" min="1" max="100"  class="slider" id="slider2" style={{ backgroundColor: '#4CAF50', border: '1px solid #4CAF50' }} />
      </div>

    </div>
  );
}

export default Inputs;
