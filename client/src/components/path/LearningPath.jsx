import React from "react";
import { Bar } from "react-chartjs-2";
import { motion } from "framer-motion";
import "chart.js/auto";
import "./LearningPath.css"; // Custom CSS

const LearningPath = () => {
  // Sample data for the graph (current skills vs. required skills)
  const data = {
    labels: ["JavaScript", "React", "Node.js", "CSS", "Algorithms", "Data Structures"],
    datasets: [
      {
        label: "Current Skill Level",
        data: [4, 3, 2, 3, 1, 2],
        backgroundColor: "rgba(75, 192, 192, 0.6)",
      },
      {
        label: "Required Skill Level",
        data: [8, 7, 6, 7, 6, 7],
        backgroundColor: "rgba(153, 102, 255, 0.6)",
      },
    ],
  };

  const options = {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  };

  return (
    <div className="learning-path-container">
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
        className="learning-path-intro"
      >
        <h2>Your Personalized Learning Path</h2>
        <p>
          Based on your current skills and desired job role, we've created a
          tailored learning path to help you level up!
        </p>
      </motion.div>

      <div className="learning-path-chart">
        <h3>Skills Breakdown</h3>
        <Bar data={data} options={options} />
      </div>

      {/* Journey Map */}
      <div className="learning-path-journey">
        <h3>Next Steps in Your Journey</h3>
        <div className="journey-map">
          <div className="step-container">
            <div className="step-content">
              <span className="step-icon">📘</span>
              <p>1. Learn advanced JavaScript concepts</p>
            </div>
            <div className="line"></div>
          </div>

          <div className="step-container">
            <div className="step-content">
              <span className="step-icon">⚛️</span>
              <p>2. Master React with hooks and state management</p>
            </div>
            <div className="line"></div>
          </div>

          <div className="step-container">
            <div className="step-content">
              <span className="step-icon">💻</span>
              <p>3. Build backend skills with Node.js, Express, MongoDB</p>
            </div>
            <div className="line"></div>
          </div>

          <div className="step-container">
            <div className="step-content">
              <span className="step-icon">🧠</span>
              <p>4. Dive deeper into algorithms and data structures</p>
            </div>
            <div className="line"></div>
          </div>

          <div className="step-container">
            <div className="step-content">
              <span className="step-icon">🚀</span>
              <p>5. Build real-world projects to showcase your skills</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LearningPath;
