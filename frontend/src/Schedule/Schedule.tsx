import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { useEffect } from "react";

const Schedule: React.FC = () => {
  useEffect(() => {
    // Set body height to 100vh when the component mounts
    document.body.style.height = "100vh";
  }, []);
  return <h1>Schedule</h1>;
};

export default Schedule;
