import "./HomePage.css";
import logo from "../Images/logo-ai-brush-removebg-p88bcaj3 (1).png";
import CollegeYearQuestion from "./CollegeYearQuestion";

function HomePage() {
  return (
    <>
      <h1 className="logo-text">Welcome to</h1>
      <div className="image-container">
        <img src={logo} width={649} height={110} alt="logo"></img>
      </div>
      <CollegeYearQuestion />
    </>
  );
}

export default HomePage;
