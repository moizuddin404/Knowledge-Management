import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import SignIn from "./pages/SignIn";
import Home from "./pages/Home";
import ProtectedRoute from "./components/ProtectedRoute";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<SignIn />} />

        <Route element={<ProtectedRoute />}>
        <Route path="/home" element={<Home />} />
        </Route>
        
      </Routes>
    </Router>
  );
};

export default App;
