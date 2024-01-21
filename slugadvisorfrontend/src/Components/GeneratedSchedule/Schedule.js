import React from 'react';
import Table from 'react-bootstrap/Table';

const PlanTable = ({ planData }) => {
  return (
    <Table striped>
      <thead>
        <tr>
          <th>Year</th>
          {planData[0]?.quarters.map((quarterData, quarterIndex) => (
            <th key={`quarter-header-${quarterIndex}`}>{quarterData.quarter}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {planData.map((yearData, yearIndex) => (
          <tr key={`year-row-${yearIndex}`}>
            <td>{yearData.year}</td>
            {yearData.quarters.map((quarterData, quarterIndex) => (
              <td key={`quarter-cell-${yearIndex}-${quarterIndex}`}>
                <ul>
                  {quarterData.courses.map((courses, coursesIndex) => (
                    <li key={`goal-item-${yearIndex}-${quarterIndex}-${coursesIndex}`}>{courses}</li>
                  ))}
                </ul>
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </Table>
  );
};

export default PlanTable;
