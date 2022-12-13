// src/redux/dodules/counter.js

// Action Value
const ADD_NUMBER = "ADD_NUMBER";
const MINUS_NUMBER = "MINUS_NUMBER"
// Action Creator
export const addNumber = (payload) => {
  return {
    type: ADD_NUMBER,
    payload
  }
}
export const deleteNumber = (payload) => {
  return {
    type: MINUS_NUMBER,
    payload
  }
}

// initial State
const initialState = {
  number: 0,
}
// Reducer
const counter = (state=initialState, action) => {
  switch (action.type){
    case ADD_NUMBER:{
      return {
        number: state.number+action.payload,
      }
    }
    case MINUS_NUMBER:{
      return {
        number: state.number-action.payload,
      }
    }
    default:
      return state;
  }
}
// export default reducer
export default counter