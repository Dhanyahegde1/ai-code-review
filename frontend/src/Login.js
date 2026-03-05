import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

//login component
function Login() {

  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");
  const [error,setError] = useState("");

  //navigation hook
  const navigate = useNavigate();
  //handle login func
  const handleLogin = async (e) => {
     //prevent page reload
    e.preventDefault();

    try {
      //login req
      const res = await axios.post(
        "http://127.0.0.1:8000/auth/login",
        {
          email: email,
          password: password
        }
      );
      // stores jwt token
      localStorage.setItem("token", res.data.access_token);

      navigate("/dashboard");

    } catch (err) {

      setError("Invalid credentials");

    }

  };

  return (
    //componet ui
    <div className="auth-container">

      <h2>Login</h2>

      <form onSubmit={handleLogin}>

        <input
          type="email"
          placeholder="Email"
          onChange={(e)=>setEmail(e.target.value)}
        />

        <br/><br/>

        <input
          type="password"
          placeholder="Password"
          onChange={(e)=>setPassword(e.target.value)}
        />

        <br/><br/>

        <button type="submit">Login</button>

      </form>

      <p style={{color:"red"}}>{error}</p>

      <br/>

      <button onClick={()=>navigate("/register")}>
        Create an Account
      </button>

    </div>
  );
}
//component export
export default Login;