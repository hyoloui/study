import React, {useState} from "react";
import "./App.css";
import { useSelector, useDispatch } from "react-redux"; // import 해주세요.
import { addNumber, deleteNumber } from "./redux/modules/counter";
const App = () => {
    const [number, setNumber] = useState(0);
    const globalNumber = useSelector((state)=>state.counter.number);
    const dispatch = useDispatch();

    const onChangeHandler = (event) => {
        const{value} = event.target;
        setNumber(+value)
    }
    const onClickAddNumberHandler = () => {
        dispatch(addNumber(number));
    }
    const onClickDeleteNumberHandler = () => {
        dispatch(deleteNumber(number))
    }
    console.log(number);
    
    return (
        <>
            <div id="component">
                {/* <StyledCompo/> */}

                {/* <Update /> */}

                {/* <UseEffect/> */}
            </div>

            <div>
                {globalNumber}
                <input type="number" onChange={onChangeHandler}/>
                <button onClick={onClickAddNumberHandler}>더하기</button>
                <button onClick={onClickDeleteNumberHandler}>빼기</button>
            </div>
            
        </>
    );
};

export default App;
