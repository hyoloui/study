import React from "react";
import './App.css';
import StyledCompo from "./component/StyledCompo";
import Update from "./component/Update";
import UseEffect from "./component/UseEffect"


const App = () => {

  return (
    <>
      <div id="component">
        <StyledCompo/>

        <Update />

        <UseEffect/>
      </div>

      
    </>
  );
};

export default App;