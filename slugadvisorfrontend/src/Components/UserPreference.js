import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Form from 'react-bootstrap/Form';
import morningclass from '../images/morningclass.jpeg';
import nightclass from '../images/nightclass.jpeg';
import graduate from '../images/graduate.jpeg';
import clock from '../images/clock.jpeg'
import React, { useState } from 'react';

function UserPreferences() {
  const [night, setNight] = useState(false);
  const [morning, setMorning] = useState(false);
  const [Years, setGraduation] = useState(0);
  const [Credits, setCredits] = useState(0);

  const handleYearInputChange = (event) => {
    // Update the state with the new input value
    setGraduation(event.target.value);
  };

  const handleCreditInputChange = (event) => {
    // Update the state with the new input value
    setCredits(event.target.value);
  };

  // Function to handle form submission
  const handleSubmit = (event) => {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Access the value stored in the variable graduationYears
    console.log('Graduation Years:', Years);
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
        <Card.Img variant="top" src={clock} />
        <Card.Body>
          <Card.Title>Credit Hours</Card.Title>
          <Card.Text>
            <Form onSubmit={handleSubmit}>
              <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                <Form.Label>How Many Credits Would you Like to do per Quarter?</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="15"
                  value={Credits}
                  onChange={handleCreditInputChange}
                />
              </Form.Group>
              <Button variant="primary">Enter</Button>
            </Form>
          </Card.Text>
          
        </Card.Body>
      </Card>
      <Card style={{ width: '18rem' }}>
        <Card.Img variant="top" src={graduate} />
        <Card.Body>
          <Card.Title>Years to Graduate</Card.Title>
          <Card.Text>
            <Form onSubmit={handleSubmit}>
              <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                <Form.Label>How Many Years Do You want to Graduate</Form.Label>
                <Form.Control
                  type="text"
                  placeholder="4"
                  value={Years}
                  onChange={handleYearInputChange}
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
