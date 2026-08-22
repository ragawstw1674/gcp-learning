import os

from flask import Flask, jsonify
from google.cloud import bigquery

app = Flask(__name__)

BILLING_PROJECT_ID = os.getenv("BILLING_PROJECT_ID")
DATA_PROJECT_ID = os.getenv("DATA_PROJECT_ID")
DATASET_NAME = os.getenv("DATASET_NAME")
TABLE_NAME = os.getenv("TABLE_NAME")

client = bigquery.Client(project=BILLING_PROJECT_ID)

@app.route("/", methods=["GET"])
def query():
    table_name = f"{DATA_PROJECT_ID}.{DATASET_NAME}.{TABLE_NAME}"
    QUERY = f'SELECT name FROM `{table_name}`'
    query_job = client.query(QUERY)
    rows = query_job.result()

    return jsonify({
        "names": [row.name for row in rows]
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )