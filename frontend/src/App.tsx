import "devextreme/dist/css/dx.light.css";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./HomePage/HomePage";
import Schedule from "./Schedule/Schedule";

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/schedule" element={<Schedule />} />
      </Routes>
    </Router>
  );
};

export default App;
