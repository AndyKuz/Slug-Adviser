import React, { useState } from 'react';
import CheckExample from './CheckBox'; // Assuming the CheckExample component is in a separate file
import allAPClasses from './APCLassList';
import SearchBar from './Searchbar';

const APClassTracker = () => {
  const [classesTaken, setClassesTaken] = useState([]);
  const [selectedScores, setSelectedScores] = useState({});
  const [selectedScore, setSelectedScore] = useState({});
  const [selectedClasses, setSelectedClasses] = useState([]);

  const handleScoreChange = (selectedScores) =>{
    setSelectedScore(selectedScores);
  }

  const handleSearchChange = (selectedItems) => {
    setSelectedClasses(selectedItems);
  };

  const addClasses = () => {
    const newClasses = selectedClasses.map((className) => ({
      className,
      score: selectedScores[className],
    }));

    setClassesTaken([...classesTaken, ...newClasses]);
    setSelectedClasses([]);
    setSelectedScores({});
  };

  const getClassesByScore = (score) => {
    return classesTaken.filter((course) => course.score === score);
  };

  const scores3 = getClassesByScore(3);
  const scores4 = getClassesByScore(4);
  const scores5 = getClassesByScore(5);

  return (
    <div>
      <h2>AP Class Tracker</h2>
      <SearchBar items = {allAPClasses} onChange={handleSearchChange}></SearchBar>
      <div>
        <label>Score:</label>
        <select value={selectedScore} onChange={handleScoreChange}>
          <option value="">Select Score</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
        </select>
      </div>
      <div>
        <button onClick={addClasses}>Add Classes</button>
      </div>
      <div>
        <h3>Classes Taken:</h3>
        <ul>
          {classesTaken.map((course, index) => (
            <li key={index}>{`${course.className} - Score: ${course.score}`}</li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Classes with Score 3:</h3>
        <ul>
          {scores3.map((course, index) => (
            <li key={index}>{`${course.className} - Score: ${course.score}`}</li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Classes with Score 4:</h3>
        <ul>
          {scores4.map((course, index) => (
            <li key={index}>{`${course.className} - Score: ${course.score}`}</li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Classes with Score 5:</h3>
        <ul>
          {scores5.map((course, index) => (
            <li key={index}>{`${course.className} - Score: ${course.score}`}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default APClassTracker;
