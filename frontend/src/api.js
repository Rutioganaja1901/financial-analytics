export const fetchStockData = async () => {
  const response = await fetch("http://127.0.0.1:5000/api/stock-analysis");
  if (!response.ok) {
    throw new Error("API failed");
  }
  return response.json();
};
