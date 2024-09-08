import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";  // Import Axios
import "./Registration.css"; // This file will contain the styling

const Registration = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: "",   // Changed to 'username' to match backend model
    fullname: "",   // Added 'fullname'
    email: "",
    interest: "",
    level: "Beginner", // Default level
    password: "",
  });

  const [error, setError] = useState("");  // Error state

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/user", {
        username: formData.username,  // Matches backend field
        fullname: formData.fullname,  // Matches backend field
        email: formData.email,
        password: formData.password,
        interest: formData.interest,
        level: formData.level,
      });

      if (response.status === 200) {
        console.log("User registered successfully");
        navigate("/courses"); // Navigate to courses after successful registration
      }
    } catch (error) {
      console.error("There was an error registering the user:", error);
      setError("Failed to register. Please try again.");  // Set error message
    }
  };

  return (
    <div className="registration-container">
      <h2>Register to Personalize Your Learning Path</h2>
      {error && <p className="error-message">{error}</p>}  {/* Display error if exists */}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Username:</label>
          <input type="text" name="username" value={formData.username} onChange={handleChange} required />
        </div>
        <div className="form-group">
          <label>Full-name:</label>
          <input type="text" name="fullname" value={formData.fullname} onChange={handleChange} required />
        </div>
        <div className="form-group">
          <label>Email:</label>
          <input type="email" name="email" value={formData.email} onChange={handleChange} required />
        </div>
        <div className="form-group">
          <label>Interest/career path:</label>
          <input type="text" name="interest" value={formData.interest} onChange={handleChange} required />
        </div>
        <div className="form-group">
          <label>Level of Skill:</label>
          <select name="level" value={formData.level} onChange={handleChange} required>
            <option value="Beginner">Beginner</option>
            <option value="Intermediate">Intermediate</option>
            <option value="Advanced">Advanced</option>
          </select>
        </div>
        <div className="form-group">
          <label>Password:</label>
          <input type="password" name="password" value={formData.password} onChange={handleChange} required />
        </div>
        <button type="submit" className="primary-btn">Get Started</button>
      </form>
    </div>
  );
};

export default Registration;
