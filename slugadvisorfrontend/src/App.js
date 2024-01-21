import React from 'react';
import TabComponent from './Components/TabComponent';
import 'bootstrap/dist/css/bootstrap.min.css';
import { SharedProvider } from './SharedContext';
import logo from './images/logo.png'

function App() {
  const backgroundStyle = {
    backgroundImage: `url(${logo})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    height: '100vh', // Adjust the height as needed
    // Add any other styles you want for your background
  };

  return (
    <div className="App" style={backgroundStyle}>
      <SharedProvider>
        <TabComponent />
      </SharedProvider>
    </div>
  );
}

export default App;

