import React from "react";
import { Link } from "react-router-dom";
import "./header.css";

const Head = () => {
  return (
    <>
      <section className="head">
        <div className="container flexSB">
          <div className="logo">
            <h1>LEARNING HUB</h1>
            <span>AI-powered learning paths</span>
          </div>

          <div className="social">
            <i className="fab fa-facebook-f icon"></i>
            <i className="fab fa-instagram icon"></i>
            <i className="fab fa-twitter icon"></i>
            <i className="fab fa-youtube icon"></i>

            <Link to="/login" className="login-btn">
              <button className="icon-btn">Login</button>
            </Link>
          </div>
        </div>
      </section>
    </>
  );
};

export default Head;
