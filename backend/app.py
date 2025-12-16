from flask import Flask, jsonify
from flask_cors import CORS

from services.analytics import analyze_stock

app = Flask(__name__)
CORS(app)  # <<< REQUIRED

@app.route("/api/stock-analysis")
def stock_analysis():
    return jsonify(analyze_stock())

if __name__ == "__main__":
    app.run(debug=True)
