import React, { useState } from 'react';
import allUCSCClasses from './UCSCCLassList';
import SearchBar from './Searchbar';

const UCSCCourseTracker = () => {
  const [classesTaken, setClassesTaken] = useState([]);
  const [selectedClasses, setSelectedClasses] = useState([]);
  const [selectedScore, setSelectedScore] = useState('');

  const handleSearchChange = (selectedItems) => {
    setSelectedClasses(selectedItems);
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
  };

  return (
    <div>
      <h2>UCSC Courses</h2>
      <SearchBar items={allUCSCClasses} onChange={handleSearchChange} />
      <div>
        <button onClick={addClasses}>Add Classes</button>
      </div>
      <div></div>
    </div>
  );
};

export default UCSCCourseTracker;