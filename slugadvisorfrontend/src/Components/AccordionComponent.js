import Accordion from 'react-bootstrap/Accordion';
import APClassTracker from './APClassSelector/ApClassesComponent';
import UCSCCourseTracker from './UCSCoursesTaken/UCSCClassComponent';
import UserPreferences from './UserPreference';
function AccordionComponent() {
  return (
    <Accordion defaultActiveKey="0">
      <Accordion.Item eventKey="0">
        <Accordion.Header>Incoming Freshman</Accordion.Header>
        <Accordion.Body>
          Pick The AP Classes that you have taken
          <APClassTracker></APClassTracker>
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="1">
        <Accordion.Header>Current Student</Accordion.Header>
        <Accordion.Body>
        Pick the Current Classes you have completed
        <UCSCCourseTracker></UCSCCourseTracker>
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="2">
        <Accordion.Header>Select Your Preferences</Accordion.Header>
        <Accordion.Body>
        <UserPreferences></UserPreferences>
        </Accordion.Body>
      </Accordion.Item>
    </Accordion>
  );
}

export default AccordionComponent;