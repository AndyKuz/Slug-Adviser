import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';
import morningclass from '../images/morningclass.jpeg';
import nightclass from '../images/nightclass.jpeg';
import graduate from '../images/graduate.jpeg';
import calander from '../images/calander.png'
import React, { useState } from 'react';
import { useSharedState } from '../SharedContext';

function UserPreferences() {
  const [night, setNight] = useState(false);
  const [morning, setMorning] = useState(false);
  const [minhoursperweek, setMinHours] = useState(0);
  const [maxhoursperweek, setMaxHours] = useState(0);
  const [MinCredits, setMinCredits] = useState(0);
  const [MaxCredits, setMaxCredits] = useState(0);
  const { sharedState, updateSharedState } = useSharedState();


  const handleMinHoursInputChange = (event) => {
    const newhours = event.target.value;
    setMinHours(newhours);
    updateSharedState({MinHoursPerWeek: newhours });
  };
  const handleMaxHoursInputChange = (event) => {
    const newhours = event.target.value;
    setMaxHours(newhours);
    updateSharedState({MaxHoursPerWeek: newhours });
  };
  
  const handleMinCreditInputChange = (event) => {
    const newCredits = event.target.value;
    setMinCredits(newCredits);
    updateSharedState({ MinCredits: newCredits });
  };

  const handleMaxCreditInputChange = (event) => {
    const newCredits = event.target.value;
    setMaxCredits(newCredits);
    updateSharedState({ MaxCredits: newCredits });
  };
  

  // Function to handle form submission
  const handleSubmit = (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Access the value stored in the variable graduationYears
    // You can now use the value stored in graduationYears as needed
  };

  return (
    <div>
    <div className="d-flex justify-content-around">
      <Card style={{ width: '18rem' }}>
        <Card.Img variant="top" src={morningclass} />
        <Card.Body>
          <Card.Title>Early Bird</Card.Title>
          <Card.Text>You prefer Morning Classes</Card.Text>
          <Button onClick={() => setMorning(true)} variant="primary">
            This is me!
          </Button>
        </Card.Body>
      </Card>

      <Card style={{ width: '18rem' }}>
        <Card.Img variant="top" src={nightclass} />
        <Card.Body>
          <Card.Title>Night Owl</Card.Title>
          <Card.Text>You Prefer Evening or Night Classes</Card.Text>
          <Button onClick={() => setNight(true)} variant="primary">
            This is Me!
          </Button>
        </Card.Body>
      </Card>
      <Card style={{ width: '18rem' }}>
        <Card.Img variant="top" src={calander} />
        <Card.Body>
          <Card.Title>Credit Per Quarter</Card.Title>
          <Card.Text>
            <Form onSubmit={handleSubmit}>
              <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                <Form.Label>How Many Credits Would you Like to do per Quarter?</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Minumum 12 Credits"
                  //value={MinCredits}
                  onChange={handleMinCreditInputChange}
                />
                <br />
                 <Form.Control 
                  type="text" 
                  placeholder="Maxcredits" 
                  //value={MaxCredits}
                  onChange={handleMaxCreditInputChange}/>
              </Form.Group>
              <Button variant="primary">Enter</Button>
            </Form>
          </Card.Text>
          
        </Card.Body>
      </Card>
      <Card style={{ width: '18rem' }}>
        <Card.Img variant="top" src={graduate} />
        <Card.Body>
          <Card.Title>Hours Per Week</Card.Title>
          <Card.Text>
            <Form onSubmit={handleSubmit}>
              <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                <Form.Label>How Many Hours a Week Do you want to Work</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="Minimum hours per Week"
                  onChange={handleMinHoursInputChange}
                />
                <Form.Control
                  type="text"
                  placeholder="Maximum Hours per Week"
                  onChange={handleMaxHoursInputChange}
                />
              </Form.Group>
              <Button variant="primary">Enter</Button>
            </Form>
          </Card.Text>
          
        </Card.Body>
      </Card>
    </div>
    
    </div>
  );
}

export default UserPreferences;
