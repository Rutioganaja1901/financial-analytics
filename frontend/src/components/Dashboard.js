import { useEffect, useState } from 'react';
import { fetchStockData } from '../api';
import StockChart from './StockChart';


export default function Dashboard() {
const [data, setData] = useState(null);


useEffect(() => {
fetchStockData().then(setData);
}, []);


if (!data) return <p>Loading...</p>;


return (
<div>
<h2>Stock Analytics Dashboard</h2>
<p>Volatility: {data.volatility}</p>
<p>Profit / Loss: ₹{data.profit_loss}</p>
<p>Risk Level: {data.risk_level}</p>
<StockChart data={data} />
</div>
);
}