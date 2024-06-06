import AutomationStatus from "./components/AutomationStatus";
import SensorChart from "./components/SensorData";

export function App() {

  return (
   <div className="bg-black w-screen h-screen">
    <h1 className="text-white text-2xl font-black p-4 w-full">Dashboard Real Time</h1>
    <div>
      <SensorChart />
    </div>
    <div>
      <AutomationStatus />
    </div>
   </div>
  )
}