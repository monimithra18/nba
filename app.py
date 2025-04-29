from flask import Flask, request, render_template
import psycopg2
import pandas as pd

app = Flask(__name__)

# Your Neon PostgreSQL URL
DB_URL = "postgresql://neondb_owner:npg_SFQj7Ux2EdBb@ep-morning-mountain-a49enedp-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"

def run_query(sql_query):
    conn = psycopg2.connect(DB_URL)
    df = pd.read_sql_query(sql_query, conn)
    conn.close()
    return df

@app.route('/', methods=['GET', 'POST'])
def index():
    output = None
    if request.method == 'POST':
        query = request.form.get('query')
        try:
            output = run_query(query)
        except Exception as e:
            output = f"Error: {e}"
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
