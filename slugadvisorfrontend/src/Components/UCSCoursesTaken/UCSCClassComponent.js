import React, { useState } from 'react';
import allUCSCClasses from './UCSCCLassList';
import SearchBar from './Searchbar';
import { Button, ListGroup } from 'react-bootstrap';
import { useSharedState } from '../../SharedContext';

const UCSCCourseTracker = () => {
  const [classesTaken, setClassesTaken] = useState([]);
  const [selectedClasses, setSelectedClasses] = useState([]);
  const {sharedState, updateSharedState } = useSharedState();

  const handleSearchChange = (selectedItems) => {
    setSelectedClasses(selectedItems);
  };

  const addClasses = () => {
    if (selectedClasses.length === 0) {
      return; // Don't add if no classes selected or no score chosen
    }

    const newClasses = selectedClasses.map((className) => ({
      className,
    }));

    setClassesTaken([...classesTaken, ...newClasses]);
    updateSharedState({CoursesTaken: [...classesTaken, ...newClasses]});
    setSelectedClasses([]);
  };

  const deleteClass = (index) => {
    const updatedClasses = [...classesTaken];
    updatedClasses.splice(index, 1);
    setClassesTaken(updatedClasses);
    updateSharedState({CoursesTaken: updatedClasses});
  };

  return (
    <div>
      <h2>UCSC Courses</h2>
      <SearchBar items={allUCSCClasses} onChange={handleSearchChange} />
      <div>
        <Button onClick={addClasses}>Add Classes</Button>
      </div>
      <div>
        <h3>Classes Taken:</h3>
        <ListGroup>
          {classesTaken.map((course, index) => (
            <ListGroup.Item key={index}>
              {course.className}
              <Button variant="danger" onClick={() => deleteClass(index)}>
                Delete
              </Button>
            </ListGroup.Item>
          ))}
        </ListGroup>
      </div>
    </div>
  );
};

export default UCSCCourseTracker;
