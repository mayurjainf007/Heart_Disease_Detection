import { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Line } from 'react-chartjs-2';
import axios from "axios";

export default function Dashboard() {
    const [patientData, setPatientData] = useState([]);
    
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get("http://localhost:5000/patient_predictions");
                setPatientData(response.data);
            } catch (error) {
                console.error("Error fetching data", error);
            }
        };
        fetchData();
    }, []);

    const data = {
        labels: patientData.map((d, i) => i),
        datasets: [{
            label: "Heart Disease Probability",
            data: patientData.map(d => d.prediction),
            borderColor: "blue",
            fill: false
        }]
    };

    return (
        <Card>
            <CardContent>
                <h2>Real-time Heart Disease Predictions</h2>
                <Line data={data} />
            </CardContent>
        </Card>
    );
}
