import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import AccordionComponent from './AccordionComponent';
import { Button } from 'react-bootstrap';
import { useSharedState } from '../SharedContext';
import Schedule from './GeneratedSchedule/Schedule';
import jsondata from "./GeneratedSchedule/SampleClasses.json";
import MajorAndYearDropdowns from './MajorSelection';


function TabComponent() {
  const { sharedState, updateSharedState } = useSharedState();
  const handleSaveData = async () => {
    try {
      const response = await fetch('http://your-backend-api.com/saveData', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(sharedState),
      });

      if (response.ok) {
        console.log('Data successfully sent to the backend.');
      } else {
        console.error('Failed to send data to the backend.');
      }
    } catch (error) {
      console.error('Error while sending data:', error);
    }
  };
  return (
    <div>
    <Tabs
      defaultActiveKey="profile"
      id="uncontrolled-tab-example"
      className="mb-3"
    >
     <Tab eventKey="Course Planner" title="Course Planner">
      Choose based on what things you have done
        <AccordionComponent/>
        <div style={{ margin: '20px 0' }}>
        <MajorAndYearDropdowns/>

        <Button onClick={handleSaveData}>Generate Schedule</Button>
        </div>
      </Tab>
      <Tab eventKey="Advisor" title="Advisor">
        ChatGpt 
      </Tab>
      <Tab eventKey="Schedule" title="GeneratedSchedule">
        <Schedule planData={jsondata.planData}/>
      </Tab>
    </Tabs>
    <div style={{ marginTop: '20px' }}>
        <h3>Shared State Information</h3>
        <pre>{JSON.stringify(sharedState, null, 2)}</pre>
    </div>
    
    </div>
  );
}

export default TabComponent;
