import os

from flask import Flask, jsonify
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy

app = Flask(__name__)

def create_db_pool():
    instance_connection_name = os.environ["INSTANCE_CONNECTION_NAME"]
    db_iam_user = os.environ["DB_IAM_USER"]
    db_name = os.environ["DB_NAME"]

    ip_type = (
        IPTypes.PRIVATE
        if os.environ.get("PRIVATE_IP")
        else IPTypes.PUBLIC
    )

    connector = Connector(refresh_strategy="LAZY")

    def getconn():
        return connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_iam_user,
            db=db_name,
            enable_iam_auth=True,
            ip_type=ip_type,
        )

    return sqlalchemy.create_engine(
        "postgresql+pg8000://",
        creator=getconn,
    )


pool = create_db_pool()


@app.route("/", methods=["GET"])
def health():
    with pool.connect() as db_conn:
        result = db_conn.execute(
            sqlalchemy.text("SELECT NOW()")
        ).fetchone()

    return jsonify({
        "status": "ok",
        "current_time": str(result[0])
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )