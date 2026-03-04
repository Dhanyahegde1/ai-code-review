import React from "react";
import { useNavigate } from "react-router-dom";//react router hook

//dashboard component
function Dashboard(){
  //naviagtion hook
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };
  //returns  JSX UI layout
  return(

    <div style={{textAlign:"center",marginTop:"100px"}}>

      <h2>Dashboard</h2>

      <p>Welcome to AI Code Review System</p>
       <br></br>
    <p>enter your code to check:</p>
    <input type ="combo box" placeholder="enter your code here" name="combo">
    </input>
    <br></br>
    <br></br>
    <button type="submit" value= "submit">submit</button>
    <br></br>
      <button onClick={logout}>
        Logout
      </button>

    </div>

  );

}
//component export
export default Dashboard;