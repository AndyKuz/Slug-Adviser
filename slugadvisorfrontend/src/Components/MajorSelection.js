import React, { useState } from 'react';
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import Dropdown from 'react-bootstrap/Dropdown';
import DropdownButton from 'react-bootstrap/DropdownButton';
import { useSharedState } from '../SharedContext';

// ... (other imports)

const MajorAndYearDropdowns = () => {
  const [selectedMajor, setSelectedMajor] = useState('Select Major');
  const [selectedYear, setSelectedYear] = useState('Select Year');
  const { sharedState, updateSharedState } = useSharedState();

  const majors = ['Computer Science', 'Computer Engineering'];
  const years = ['Freshman', 'Sophomore', 'Junior', 'Senior'];

  const handleMajorSelect = (major) => {
    setSelectedMajor(major);
    updateSharedState({ ...sharedState, Major: major });
  };

  const handleYearSelect = (year) => {
    setSelectedYear(year);
    updateSharedState({ ...sharedState, CurrentYear: year });
  };

  return (
    <ButtonGroup>
      <DropdownButton
        as={ButtonGroup}
        id="dropdown-major"
        variant="primary"
        title={selectedMajor}
        onSelect={handleMajorSelect} // Use direct function reference
      >
        {majors.map((major) => (
          <Dropdown.Item key={major} eventKey={major}>
            {major}
          </Dropdown.Item>
        ))}
      </DropdownButton>

      <DropdownButton
        as={ButtonGroup}
        id="dropdown-year"
        variant="secondary"
        title={selectedYear}
        onSelect={handleYearSelect} // Use direct function reference
      >
        {years.map((year) => (
          <Dropdown.Item key={year} eventKey={year}>
            {year}
          </Dropdown.Item>
        ))}
      </DropdownButton>
    </ButtonGroup>
  );
};

export default MajorAndYearDropdowns;
