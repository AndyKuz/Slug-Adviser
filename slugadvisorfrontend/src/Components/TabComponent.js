import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import AccordionComponent from './AccordionComponent';

function TabComponent() {
  return (
    <Tabs
      defaultActiveKey="profile"
      id="uncontrolled-tab-example"
      className="mb-3"
    >
     <Tab eventKey="Course Planner" title="Course Planner">
      Choose based on what things you have done
        <AccordionComponent/>
      </Tab>
      <Tab eventKey="Advisor" title="Advisor">
        ChatGpt 
      </Tab>
      <Tab eventKey="Schedule" title="GeneratedSchedule">
        ChatGpt 
      </Tab>
      
    </Tabs>
  );
}

export default TabComponent;
