// SharedContext.js
import { createContext, useContext, useState } from 'react';

const SharedContext = createContext();

export const SharedProvider = ({ children }) => {
  const [sharedState, setSharedState] = useState({
    night: false,
    morning: false,
    MinHoursPerWeek: 4,
    MaxHoursPerWeek: 15,
    MinCredits: 12,
    MaxCredits: 21,
    CoursesTaken:[],
    Major: "",
    CurrentYear: ""
  });

  const updateSharedState = (newState) => {
    setSharedState((prev) => ({ ...prev, ...newState }));
  };

  return (
    <SharedContext.Provider value={{ sharedState, updateSharedState }}>
      {children}
    </SharedContext.Provider>
  );
};

export const useSharedState = () => {
  const context = useContext(SharedContext);
  if (!context) {
    throw new Error('useSharedState must be used within a SharedProvider');
  }
  return context;
};
