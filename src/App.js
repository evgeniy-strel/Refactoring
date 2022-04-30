import React from "react";
import { Route, Routes } from "react-router-dom";
import "./style.css";
import Header from "./components/Header/Header";
import MainPage from "./components/MainPage/MainPage";
import FirstStep from "./components/SubmissionsApplications/FirstStep/FirstStep";
import SecondStep from "./components/SubmissionsApplications/SecondStep/SecondStep";
import ThirdStep from "./components/SubmissionsApplications/ThirdStep/ThirdStep";
import Gratitude from "./components/SubmissionsApplications/Gratitude/Gratitude";

function App() {
  return (
    <div className="wrapper">
      <Header />
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/first_step" element={<FirstStep />} />
        <Route path="/second_step" element={<SecondStep />} />
        <Route path="/third_step" element={<ThirdStep />} />
        <Route path="/gratitude" element={<Gratitude />} />
      </Routes>
    </div>
  );
}

export default App;
