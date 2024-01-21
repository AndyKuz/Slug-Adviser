import React, { useState } from 'react';
import Form from 'react-bootstrap/Form';

function CheckExample({ items, onChange }) {
  const [selectedScores, setSelectedScores] = useState({});

  const handleScoreChange = (item, score) => {
    setSelectedScores({
      ...selectedScores,
      [item]: score,
    });
    onChange({
      ...selectedScores,
      [item]: score,
    });
  };

  return (
    <Form>
      {items.map((item, index) => (
        <div key={`checkbox-${index}`} className="mb-3">
          <Form.Check
            type="checkbox"
            id={`checkbox-${index}`}
            label={item}
          />
          <Form.Group controlId={`scoreDropdown-${index}`}>
            <Form.Label>Score:</Form.Label>
            <Form.Control
              as="select"
              value={selectedScores[item] || ''}
              onChange={(e) => handleScoreChange(item, e.target.value)}
            >
              <option value="">Select Score</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
            </Form.Control>
          </Form.Group>
        </div>
      ))}
    </Form>
  );
}

export default CheckExample;
