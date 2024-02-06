import { SetStateAction, useEffect, useState } from "react";
import "./HomePage.css";

import "devextreme/dist/css/dx.light.css";
import { TextBox } from "devextreme-react/text-box";
import React from "react";
import { useNavigate } from "react-router-dom";

function CollegeYearQuestion() {
  const navigate = useNavigate();

  const [minCredits, setMinCredits] = useState(""); // keeps track of min credits per quarter
  const [maxCredits, setMaxCredits] = useState(""); // keeps track of max credits per quarter

  const [selectedButton, setSelectedButton] = useState(""); // keeps track of college year button clicks
  const [reveal, setReveal] = useState(false); // keepstrack of whether user clicked first question

  // activated when user answers first question
  useEffect(() => {
    if (reveal) {
      document.body.style.height = "200vh"; // doubles webpage height
      const question2Element = document.getElementById("question2");
      if (question2Element) {
        question2Element.scrollIntoView({ behavior: "smooth" }); // scrolls to question2
      }
    }
  }, [reveal]);

  const selectButton = (buttonType: string) => {
    setReveal(true);
    setSelectedButton(buttonType);
  };

  const navigateToSchedule = () => {
    navigate("/Schedule");
  };

  return (
    <>
      <div id="question1">
        <div className="questions-text">What Year Are You?</div>
        <div className="row-eq-height">
          <button
            className={`dflt-button ${
              "Freshman" == selectedButton ? `dflt-button-focus` : null
            }`}
            role="button"
            onClick={() => selectButton("Freshman")}
          >
            Freshman
          </button>
          <button
            className={`dflt-button ${
              "Sophomore" == selectedButton ? `dflt-button-focus` : null
            }`}
            role="button"
            onClick={() => selectButton("Sophomore")}
          >
            Sophomore
          </button>
          <button
            className={`dflt-button ${
              "Junior" == selectedButton ? `dflt-button-focus` : null
            }`}
            role="button"
            onClick={() => selectButton("Junior")}
          >
            Junior
          </button>
          <button
            className={`dflt-button ${
              "Senior" == selectedButton ? `dflt-button-focus` : null
            }`}
            role="button"
            onClick={() => selectButton("Senior")}
          >
            Senior
          </button>
        </div>
      </div>
      {reveal && (
        <>
          <div id="question2">
            <div className="questions-text">
              How Many Credits Would You Like To Take A Quarter?
            </div>
            <div className="row-eq-height">
              <TextBox
                className="dflt-textbox"
                placeholder="minimum (12)"
                maxLength={2}
                value={minCredits}
              ></TextBox>
              <TextBox
                className="dflt-textbox"
                placeholder="maximum (22)"
                maxLength={2}
                value={maxCredits}
              ></TextBox>
            </div>
          </div>
          <div id="question3">
            <div className="questions-text">
              What Classes Have You Taken/Have Taken?
            </div>
          </div>
          <div id="generateSchduleButton">
            <button
              onClick={() => navigateToSchedule()}
              className="dflt-button"
            >
              Generate Schedule
            </button>
          </div>
        </>
      )}
    </>
  );
}

export default CollegeYearQuestion;
