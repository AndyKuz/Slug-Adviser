import React, { useState } from 'react';
import allAPClasses from './APCLassList';
import SearchBar from './Searchbar';
import { Button } from 'react-bootstrap';
import { useSharedState } from '../../SharedContext';

const APClassTracker = () => {
  const {sharedState, updateSharedState } = useSharedState();
  const [classesTaken, setClassesTaken] = useState([]);
  const [selectedClasses, setSelectedClasses] = useState([]);
  const [selectedScore, setSelectedScore] = useState('');

  const [scores3, setScores3] = useState([]);
  const [scores4, setScores4] = useState([]);
  const [scores5, setScores5] = useState([]);

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
    let updatedScores3 = [...scores3, ...newClasses];
    let updatedScores4 = [...scores4, ...newClasses];
    let updatedScores5 = [...scores5, ...newClasses];
  
    switch (selectedScore) {
      case '3':
        setScores3(updatedScores3);
        updateSharedState({ APScores3: updatedScores3 });
        break;
      case '4':
        setScores4(updatedScores4);
        updateSharedState({ APScores4: updatedScores4 });
        break;
      case '5':
        setScores5(updatedScores5);
        updateSharedState({ APScores5: updatedScores5 });
        break;
      default:
        break;
    }
  };
  

  const deletescor3 = (index) => {
    const updatedClasses = [...scores3];
    updatedClasses.splice(index, 1);
    setScores3(updatedClasses);
    updateSharedState({ APScores3: updatedClasses });
  };
  
  const deletescor4 = (index) => {
    const updatedClasses = [...scores4];
    updatedClasses.splice(index, 1);
    setScores4(updatedClasses);
    updateSharedState({ APScores4: updatedClasses });
  };
  
  const deletescor5 = (index) => {
    const updatedClasses = [...scores5];
    updatedClasses.splice(index, 1);
    setScores5(updatedClasses);
    updateSharedState({ APScores5: updatedClasses });
  };
  

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
        <Button onClick={addClasses}>Add Classes</Button>
      </div>
      <div>
        <h3>Classes with Score 3:</h3>
        <ul>
          {scores3.map((course, index) => (
            <li key={index}>
              {course.className}
              <Button onClick={() => deletescor3(index)}>Delete</Button>
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Classes with Score 4:</h3>
        <ul>
          {scores4.map((course, index) => (
            <li key={index}>
              {course.className}
              <Button onClick={() => deletescor4(index)}>Delete</Button>
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h3>Classes with Score 5:</h3>
        <ul>
          {scores5.map((course, index) => (
            <li key={index}>
              {course.className}
              <Button onClick={() => deletescor5(index)}>Delete</Button>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default APClassTracker;
