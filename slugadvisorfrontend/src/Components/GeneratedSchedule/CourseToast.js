import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Toast from 'react-bootstrap/Toast';

const CourseToast = ({ dptmntNum, name, title }) => {
  const [show, setShow] = useState(false);

  const toggleShow = () => setShow(!show);

  return (
    <>
    {title &&
      <Button onClick={toggleShow} className="mb-2">
        {name} {dptmntNum}
      </Button>
    }
    {title &&
      <Toast   show={show}
        onClose={toggleShow}
        style={{
          position: 'fixed',
          zIndex: 1000, // Ensure it appears above other elements
          background:'white',
          marginRight: '10 px',
          marginLeft: '10 px' 
        }}>
        <Toast.Body style={{
              maxHeight: '300px', // Adjust as needed
              overflowY: 'auto',
              background: 'white',
            }}>{title}</Toast.Body>
      </Toast>
    }
    </>
  );
};

export default CourseToast;
