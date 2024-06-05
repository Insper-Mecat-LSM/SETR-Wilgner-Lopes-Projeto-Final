import { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Legend, ResponsiveContainer } from 'recharts';
import axios from 'axios';

interface ISensorDataResponse{
  created_at: string
  value: number
}

export function SensorChart(){
  const [data, setData] = useState<ISensorDataResponse[]>([]);

  useEffect(() => {
    const fetchData = () => {
      axios.get<ISensorDataResponse[]>('http://127.0.0.1:8000/sensor')
        .then(response => {
          const formattedData = response.data.map(item => ({
            created_at: new Date(item.created_at).toLocaleString(),
            value: Number(item.value),
          }));
          setData(formattedData);
        })
        .catch(error => {
          console.error('Error fetching sensor data:', error);
        });
    };
    // Fetch data immediately on mount
    fetchData();

    // Set interval to fetch data every second
    const interval = setInterval(fetchData, 2000);

    // Cleanup interval on unmount
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-2xl font-bold mb-4 text-white">Sensor Data</h2>
      <ResponsiveContainer width="100%" height={500}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="created_at" />
          <YAxis  type="number" domain={[-10, 150]} />
          {/* <Tooltip /> */}
          <Legend />
          <Line type="natural" dataKey="value" stroke="red" dot={false} isAnimationActive={true}/>
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default SensorChart;
