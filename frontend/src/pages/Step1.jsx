// src/pages/Step1.jsx
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import ViewStep1 from "../views/viewStep1";

/**
 * Username input 
 */

export default function Step1() {
  const [username, setUsername] = useState("");
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const safeUsername = username.trim();
    
    if (!/^[a-zA-Z0-9_]+$/.test(safeUsername)) {
            alert("Please enter a valid username (letters, numbers, and underscores only).");
            return;
    }
    
    // TODO: logic for connecting to backend
    setTimeout(() => {       
        navigate(`/step2?username=${encodeURIComponent(username)}`);
    }, 1000);
  };

  return (
    <ViewStep1
        username={username}
        onChange={(e) => setUsername(e.target.value)}
        onSubmit={handleSubmit}
    />
  );
}
