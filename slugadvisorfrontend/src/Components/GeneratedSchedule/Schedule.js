import React from 'react';
import Table from 'react-bootstrap/Table';
import CourseToast from './CourseToast';

const PlanTable = ({ planData }) => {
  if (!planData) {
    return <p>Loading...</p>; // Display a loading state while data is being fetched
  }

  if (planData.error) {
    return <p>Error loading data. Please try again.</p>; // Display an error message if there's an issue with the data
  }

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
                {/* Handle major courses */}
                {quarterData.major_courses.map((course, coursesIndex) => (
                  <CourseToast
                    key={`major-course-${yearIndex}-${quarterIndex}-${coursesIndex}`}
                    name={course.dptmnt}
                    dptmntNum={course.dptmnt_num}
                    title={`${course.course_title}\n Credits: ${course.num_credits}`}
                  />
                ))}
                {/* Handle placeholder courses */}
                {quarterData.placeholder_courses.map((course, coursesIndex) => (
                  <CourseToast
                    key={`placeholder-course-${yearIndex}-${quarterIndex}-${coursesIndex}`}
                    name={course.dptmnt}
                    dptmntNum={course.dptmnt_num}
                    title={`${course.course_title}\nCredits: ${course.num_credits}`}
                  />
                ))}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </Table>
  );
};

export default PlanTable;
