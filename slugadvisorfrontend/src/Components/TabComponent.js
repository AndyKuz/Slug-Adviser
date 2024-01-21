import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import AccordionComponent from './AccordionComponent';
import { Button } from 'react-bootstrap';
import { useSharedState } from '../SharedContext';
import Schedule from './GeneratedSchedule/Schedule';
import jsondata from './GeneratedSchedule/SampleClasses.json';
import MajorAndYearDropdowns from './MajorSelection';
import { useState, useEffect } from 'react';

function TabComponent() {
  const { sharedState, updateSharedState } = useSharedState();
  const [planData, setPlanData] = useState(null);
  const [error, setError] = useState(null);
  const handleSaveData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/saveData', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(sharedState),
      });

      if (response.ok) {
        console.log('Data successfully sent to the backend.');
        const responseJson = await response.json()
        setPlanData(responseJson);
      } else {
        console.error('Failed to send data to the backend.');
      }
    } catch (error) {
      console.error('Error while sending data:', error);
    }
  };

  // useEffect(() => {
  // //   const fetchData = async () => {
  // //     try {
  // //       const response = await fetch('http://127.0.0.1:5000/plan-data'); // Adjust the endpoint
  // //       if (response.ok) {
  // //         const data = await response.json();
  // //         setPlanData(data);
  // //       } else {
  // //         setError('Failed to fetch data');
  // //       }
  // //     } catch (error) {
  // //       setError('Error while fetching data');
  // //     }
  // //   };

  // //   fetchData();
  // // }, []);

  const borderStyle = {
    padding: '30px',
    backgroundColor: 'white'
  };

  return (
    <div>
      <Tabs
        defaultActiveKey="profile"
        id="uncontrolled-tab-example"
        className="mb-3"
        style={{ backgroundColor: 'white', color: 'black'}}
      >
        <Tab eventKey="Course Planner" title="Course Planner" style={{ color: 'black' }}>
          <AccordionComponent />
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', margin: '20px 10px' }}>
            <MajorAndYearDropdowns />
            <Button onClick={handleSaveData} style={{ backgroundColor: 'white', color: 'black' }}>
              Generate Schedule
            </Button>
          </div>
        </Tab>
        <Tab eventKey="Schedule" title="GeneratedSchedule" style={{ color: 'black' }}>
          <Schedule planData={planData} />
        </Tab>
      </Tabs>
      <div style={{ marginTop: '20px' }}></div>
    </div>
  );
}

export default TabComponent;
