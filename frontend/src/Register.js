import React,{useState} from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

//register component
function Register(){

  const [username,setUsername] = useState("");
  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");
  //navigation hook
  const navigate = useNavigate();
  //handle register function
  const handleRegister = async(e)=>{
    //prevent page reload
    e.preventDefault();

    try{
    //send registeration req
      await axios.post(
        "http://127.0.0.1:8000/auth/register",
        {
          username:username,
          email:email,
          password:password
        }
      );

      alert("User created successfully");
      //redirect to login page
      navigate("/");

    }
    catch(err){

      alert("Email already exists");

    }

  };
  //UI component
  return(

    <div className="auth-container">
      <h2>Register</h2>

      <form onSubmit={handleRegister}>

        <input
          placeholder="Username"
          onChange={(e)=>setUsername(e.target.value)}
        />

        <br/><br/>

        <input
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

        <button type="submit">Register</button>

      </form>

    </div>

  );

}
//export component
export default Register;