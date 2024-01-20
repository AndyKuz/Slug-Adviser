import React, { useState } from 'react';
import CheckExample from './CheckBox'; // Assuming the CheckExample component is in a separate file
import allAPClasses from './APCLassList';
import SearchBar from './Searchbar';

const APClassTracker = () => {
  const [classesTaken, setClassesTaken] = useState([]);
  const [selectedClasses, setSelectedClasses] = useState([]);
  const [selectedScore, setSelectedScore] = useState('');

  const handleSearchChange = (selectedItems) => {
    setSelectedClasses(selectedItems);
  };

  const handleScoreChange = (e) => {
    setSelectedScore(e.target.value);
  };

  const addClasses = () => {
    if (selectedClasses.length === 0 || !selectedScore) {
      return; // Don't add if no classes selected or no score chosen
    }

    const newClasses = selectedClasses.map((className) => ({
      className,
      score: parseInt(selectedScore, 10),
    }));

    setClassesTaken([...classesTaken, ...newClasses]);
    setSelectedClasses([]);
    setSelectedScore('');

    // Update score lists based on the selected score
    switch (selectedScore) {
      case '3':
        const updatedScores3 = [...scores3, ...newClasses];
        setScores3(updatedScores3);
        console.log('Scores 3:', updatedScores3);
        break;
      case '4':
        const updatedScores4 = [...scores4, ...newClasses];
        setScores4(updatedScores4);
        console.log('Scores 4:', updatedScores4);
        break;
      case '5':
        const updatedScores5 = [...scores5, ...newClasses];
        setScores5(updatedScores5);
        console.log('Scores 5:', updatedScores5);
        break;
      default:
        break;
    }
  };

  // Assuming you have these state variables
  const [scores3, setScores3] = useState([]);
  const [scores4, setScores4] = useState([]);
  const [scores5, setScores5] = useState([]);
  return (
    <div>
      <h2>AP Class Tracker</h2>
      <SearchBar items={allAPClasses} onChange={handleSearchChange} />
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
        <h3>Classes with Score 3:</h3>
        <ul>
          {scores3.map((course, index) => (
            <li key={index}>{course.className}</li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Classes with Score 4:</h3>
        <ul>
          {scores4.map((course, index) => (
            <li key={index}>{course.className}</li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Classes with Score 5:</h3>
        <ul>
          {scores5.map((course, index) => (
            <li key={index}>{course.className}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default APClassTracker;