import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Dashboard() {

  const navigate = useNavigate();

  const [code, setCode] = useState("");
  const [review, setReview] = useState("");
  const [loading, setLoading] = useState(false);

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  const handleSubmit = async () => {

  setLoading(true);
  setReview("");

  try {

    const response = await fetch("http://127.0.0.1:8000/review/analyze", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        code: code
      })
    });

    const data = await response.json();

    setReview(JSON.stringify(data, null, 2));

  } catch (error) {

    setReview("Error connecting to AI Review API");

  }

  setLoading(false);
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
          width: "50%",
          flexDirection:"column",
          padding:"20px",
          border:"1px solid #5a189a",
          borderRadius:"10px",
          backgroundColor:"#150424",
          color:"white"
        }}>

          <div style={{
  display:"flex",
  justifyContent:"space-between",
  alignItems:"center"
}}>

  <h3 style={{color:"white", fontFamily:"times", fontSize:"20px"}}>
    Enter Your Code
  </h3>

  <button
    onClick={handleSubmit}
    style={{
      padding:"6px 14px",
      background:"#691fb2",
      color:"white",
      border:"none",
      borderRadius:"6px",
      cursor:"pointer",
      fontSize:"20px"
    }}
  >
    Submit
  </button>

</div>

          <textarea
            placeholder="Paste your code here..."
            value={code}
            onChange={(e)=>setCode(e.target.value)}
            style={{
              flex:1,
              padding:"10px",
              marginTop:"10px",
              width: "100%",
              height: "300px",
              resize:"none",
              backgroundColor:"#130125",
              color:"white",
              border:"1px solid #130125"
            }}
          />

          <br/>

          
        </div>

        {/* RIGHT PANEL */}
        <div style={{
          flex:1,
          display:"flex",
          width: "50%",
          overflow: "auto",
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
  overflowY:"auto",
  overflowX:"hidden",
  whiteSpace:"pre-wrap",
  wordWrap:"break-word"
}}>
            {loading ? (
              <p>Loading AI Review...</p>
          ) : (
            <pre style={{whiteSpace:"pre-wrap", wordBreak:"break-word"}}>
  {review || "Review results will appear here"}
</pre>
          )}
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