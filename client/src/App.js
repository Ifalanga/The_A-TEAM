import "./App.css";
import Header from "./components/common/header/Header";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"; 
import About from "./components/about/About.jsx";
import CourseHome from "./components/allcourses/CourseHome";
import Team from "./components/team/Team";
import Contact from "./components/contact/Contact";
import Footer from "./components/common/footer/Footer";
import Home from "./components/home/Home";
import Registration from "./components/registration/Registration";
import LearningPath from "./components/path/LearningPath.jsx";
import Login from "./components/login/Login.jsx";

function App() {
  return (
    <>
      <Router>
        <Header />
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='/about' element={<About />} />
          <Route path='/courses' element={<CourseHome />} />
          <Route path='/team' element={<Team />} />
          <Route path='/contact' element={<Contact />} />
          <Route path='/register' element={<Registration />} />
          <Route path='/path' element={<LearningPath />} />
          <Route path='/login' element={<Login />}/>
        </Routes>
        <Footer />
      </Router>
    </>
  );
}

export default App;