import Inputs from './Inputs.js'
import Outputs from './Outputs.js';

function InputAndOutput() {
  const [recipeLinks, setRecipeLinks] = useState([]);
  return (
    <div className="InputAndOutput">
      <Inputs />
      <Outputs links={recipeLinks} />
    </div>
  );
}

export default InputAndOutput;
