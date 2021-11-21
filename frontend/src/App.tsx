import { useRef, useState } from "react";
import { ReactSketchCanvas } from "react-sketch-canvas";
import { makePrediction } from "./api";
import "./App.css";

const App = () => {
  const sketchRef = useRef<any>(null);
  const [prediction, setPrediction] = useState();
  const [isHidden, setHidden] = useState<boolean>(false);

  const handleSubmit = () => {
    sketchRef.current.exportImage('jpeg').then((imageResp: any) => {
      setHidden(true);
      // @ts-ignore
      makePrediction(imageResp).then((guessedResp: any) => {
        setHidden(false);
          setPrediction(guessedResp)
        }
      );
    });
  };

  const handleClear = (_e: any) => {
    sketchRef.current.clearCanvas();
    setHidden(true);
  }

  return (
    <div className="App">
      <div>
        <header className="App-header">
          <h1 className="App-title">Draw a digit</h1>
        </header>
        <div className="Main-container">
          <div className="Sketch-container">
            <ReactSketchCanvas
              ref={sketchRef}
              width="100%"
              height="100%"
              strokeWidth={7}
              strokeColor="black"
            />
          </div>
          {<h3 className="Guess-display">Predicted value is: {!isHidden && prediction}</h3>}
          {/* <div className="Buttons-container"> */}
            <button className="Button" onClick={handleSubmit}>Guess the number</button>
            <button className="Button" onClick={handleClear}>Clear</button>
          {/* </div> */}
        </div>      
      </div>
    </div>
  );
};

export default App;