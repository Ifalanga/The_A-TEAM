import React from "react";
import Heading from "../../common/heading/Heading";
import { Link } from "react-router-dom";
import "./Hero.css";

const Hero = () => {
  return (
    <>
      <section className="hero">
        <div className="container">
          <div className="row">
            <Heading subtitle="WELCOME TO LEARNING HUB" title="Best AI-powered learning paths" />
            <p>
              The AI-Powered Personalized Learning Paths project aims to create a
              smart, adaptive learning system that customizes educational content to
              each user based on their progress, preferences, and learning goals.
            </p>
            <div className="button">
              <Link to="/register" className="primary-btn">
                GET STARTED NOW <i className="fa fa-long-arrow-alt-right"></i>
              </Link>
              <button>
                VIEW COURSE <i className="fa fa-long-arrow-alt-right"></i>
              </button>
            </div>
          </div>
        </div>
      </section>
      <div className="margin"></div>
    </>
  );
};

export default Hero;
