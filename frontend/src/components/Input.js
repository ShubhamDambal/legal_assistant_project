import React from "react";
import "./Input.css";

const Input = () => {
  return (
    <>
      <div class="back">
        <p>Enter your Queries here</p>
        <form>
          <input type="text" id="mail" placeholder="Email Address"></input>
          <button id="but">Submit</button>
        </form>
      </div>
    </>
  );
};

export default Input;
