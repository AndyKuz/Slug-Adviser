import Accordion from 'react-bootstrap/Accordion';
import APClassTracker from './APClassSelector/ApClassesComponent';
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
        </Accordion.Body>
      </Accordion.Item>
    </Accordion>
  );
}

export default AccordionComponent;