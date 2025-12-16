import { Line } from 'react-chartjs-2';
import {
Chart as ChartJS,
CategoryScale,
LinearScale,
PointElement,
LineElement
} from 'chart.js';


ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement);


export default function StockChart({ data }) {
const chartData = {
labels: data.dates,
datasets: [
{ label: 'Close Price', data: data.close_prices },
{ label: 'MA 5', data: data.ma_5 },
{ label: 'MA 10', data: data.ma_10 }
]
};


return <Line data={chartData} />;
}