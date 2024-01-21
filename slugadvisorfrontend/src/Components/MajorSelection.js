import React, { useState } from 'react';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import { useSharedState } from '../SharedContext';

const MajorAndYearDropdowns = () => {
  const [selectedMajor, setSelectedMajor] = useState('Select Major');
  const [selectedYear, setSelectedYear] = useState('Select Year');
  const { sharedState, updateSharedState } = useSharedState();

  const majors = ['Computer Science', 'Electrical Engineering', 'Mechanical Engineering']; // Add your majors
  const years = ['Freshman', 'Sophomore', 'Junior', 'Senior']; // Add your years

  const handleMajorSelect = (major) => {
    setSelectedMajor(major);
    updateSharedState({...sharedState, Major: selectedMajor});
  };

  const handleYearSelect = (year) => {
    setSelectedYear(year);
    updateSharedState({...sharedState, CurrentYear: selectedYear});
  };

  return (
    <ButtonGroup>
      <DropdownButton
        as={ButtonGroup}
        id="dropdown-major"
        variant="primary"
        title={selectedMajor}
      >
        {majors.map((major) => (
          <Dropdown.Item
            key={major}
            onSelect={() => handleMajorSelect(major)}
          >
            {major}
          </Dropdown.Item>
        ))}
      </DropdownButton>

      <DropdownButton
        as={ButtonGroup}
        id="dropdown-year"
        variant="secondary"
        title={selectedYear}
      >
        {years.map((year) => (
          <Dropdown.Item
            key={year}
            onSelect={() => handleYearSelect(year)}
          >
            {year}
          </Dropdown.Item>
        ))}
      </DropdownButton>
    </ButtonGroup>
  );
};

export default MajorAndYearDropdowns;
