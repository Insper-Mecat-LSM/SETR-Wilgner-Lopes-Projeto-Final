import { useEffect, useState } from 'react';
import axios from 'axios';

export function AutomationStatus(){
  const [status, setStatus] = useState(null);
  useEffect(() => {
    const fetchData = () => {
      axios.get('http://127.0.0.1:8000/automation/latest')
      .then(response => {
        setStatus(response.data.state);
      })
      .catch(error => {
        console.error('Error fetching automation status:', error);
      });
    };

      // Fetch data immediately on mount
    fetchData();

    // Set interval to fetch data every second
    const interval = setInterval(fetchData, 1000);

    // Cleanup interval on unmount
    return () => clearInterval(interval);
    
  }, []);
  if(status != null){
  if(status[0] == 'W'){setStatus("Habilitado / Sentido AntiHorário");}
  if(status[0] == 'M'){setStatus("Habilitado / Sentido Horário");}}
  console.log(status);

  return (
    <div className="p-4 w-full">
      <h2 className="text-2xl font-bold mb-4 text-white">Automation Status</h2>
      <div className="text-lg text-white">
        Current Status: <span className="font-semibold text-white">{status}</span>
      </div>
    </div>
  );
}

export default AutomationStatus;
