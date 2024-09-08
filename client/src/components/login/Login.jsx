import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css"; // Create this file for styling

const Login = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Ideally, you would validate and send formData to the backend
    console.log("Login Data:", formData);
    // Redirect to dashboard or the home page after successful login
    navigate("/dashboard"); // Adjust the route as needed
  };

  return (
    <div className="login-container">
      <h2>Login to Your Account</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Password:</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="primary-btn">
          Login
        </button>
      </form>
      <div className="login-options">
        <p>Don't have an account? <a href="/register">Register</a></p>
      </div>
    </div>
  );
};

export default Login;
