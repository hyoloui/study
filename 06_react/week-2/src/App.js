import React from "react";
import "./App.css";
// import StyledCompo from "./component/StyledCompo";
// import Update from "./component/Update";
// import UseEffect from "./component/UseEffect"
import { useSelector, useDispatch } from "react-redux"; // import 해주세요.
import { plusOne, minusOne } from "./redux/modules/counter";
const App = () => {
    const dispatch = useDispatch();
    const state = useSelector((state)=>state)
    const number = useSelector((state)=>state.counter.number)
    console.log(number)
    
    return (
        <>
            <div id="component">
                {/* <StyledCompo/> */}

                {/* <Update /> */}

                {/* <UseEffect/> */}
            </div>

            {number}
            <button
                onClick={() => {
                    dispatch(plusOne());
                }}
            >
                +1
                
            </button>
            <button
                onClick={() => {
                    dispatch(minusOne());
                }}
            >
                -1
            </button>
        </>
    );
};

export default App;
