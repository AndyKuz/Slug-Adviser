// App.js
import React from 'react';
import TabComponent from './Components/TabComponent';
import 'bootstrap/dist/css/bootstrap.min.css';
import { SharedProvider } from './SharedContext';

function App() {
  return (
    <div className="App">
      <SharedProvider>
      <TabComponent/>
      </SharedProvider>
    </div>
  );
}

export default App;

