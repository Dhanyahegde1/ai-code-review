import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Dashboard() {

  const navigate = useNavigate();

  const [code, setCode] = useState("");
  const [review, setReview] = useState("");

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  const handleSubmit = () => {
    setReview("AI Review will appear here...");
  };

  return (

    <div style={{
      height:"100vh",
      display:"flex",
      flexDirection:"column",
      padding:"20px",
      fontFamily:"Arial"
    }}>

      <h2 style={{textAlign:"center", color:"white", fontFamily:"verdena",fontStyle:"italic", fontSize:"40px"}}>
        Welcome to AI Code Review System
      </h2>

      <div style={{
        flex:1,
        display:"flex",
        gap:"20px",
        marginTop:"20px"
      }}>

        {/* LEFT PANEL */}
        <div style={{
          flex:1,
          display:"flex",
          flexDirection:"column",
          padding:"20px",
          border:"1px solid #5a189a",
          borderRadius:"10px",
          backgroundColor:"#150424",
          color:"white"
        }}>

          <h3 style={{color:"white", fontFamily:"times", fontSize:"20px"}}>Enter Your Code</h3>

          <textarea
            placeholder="Paste your code here..."
            value={code}
            onChange={(e)=>setCode(e.target.value)}
            style={{
              flex:1,
              padding:"10px",
              marginTop:"10px",
              resize:"none",
              backgroundColor:"#130125",
              color:"white",
              border:"1px solid #130125"
            }}
          />

          <br/>

          <button
            onClick={handleSubmit}
            style={{
              padding:"10px",
              background:"#38046c",
              color:"white",
              border:"none",
              borderRadius:"6px",
              cursor:"pointer"
            }}
          >
            Submit Code
          </button>

        </div>

        {/* RIGHT PANEL */}
        <div style={{
          flex:1,
          display:"flex",
          flexDirection:"column",
          padding:"20px",
          border:"1px solid #5a189a",
          borderRadius:"10px",
          backgroundColor:"#150424",
          color:"white"
        }}>

          <h3 style={{color:"white", fontFamily:"times", fontSize:"20px"}}>AI Review Output</h3>

          <div style={{
            flex:1,
            marginTop:"10px",
            backgroundColor:"#130125",
            padding:"15px",
            borderRadius:"5px",
            overflow:"auto"
          }}>
            {review || "Review results will appear here"}
          </div>

        </div>

      </div>

      <div style={{textAlign:"center", marginTop:"15px"}}>
        <button
          onClick={logout}
          style={{
            padding:"10px 20px",
            background:"red",
            color:"white",
            border:"none",
            borderRadius:"6px"
          }}
        >
          Logout
        </button>
      </div>

    </div>

  );
}

export default Dashboard;