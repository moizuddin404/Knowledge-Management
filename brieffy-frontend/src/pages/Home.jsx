// The dashboard page where users can add/view/edit knowledge cards.

import React from "react";
import Navbar from "../components/Navbar";
import Logout from "../components/LogoutButton";

const Home = () => {
  return (
    <div>
      <Navbar />
      <h1>Welcome to Brieffy</h1>
      <Logout></Logout>
    </div>
  );
};

export default Home;
