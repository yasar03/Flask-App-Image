# from flask import Flask, render_template, request, jsonify
# import pandas as pd
# import sqlite3
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# DATABASE = 'game_data.db'
# ADMIN_PASSWORD = 'admin123'  # You can change this password as needed

# def init_db():
#     conn = sqlite3.connect(DATABASE)
#     c = conn.cursor()
#     c.execute('''
#     CREATE TABLE IF NOT EXISTS games (
#         Unnamed INTEGER,
#         AppID INTEGER PRIMARY KEY,
#         Name TEXT,
#         ReleaseDate TEXT,
#         RequiredAge INTEGER,
#         Price REAL,
#         DLCount INTEGER,
#         AboutGame TEXT,
#         SupportedLanguages TEXT,
#         Windows BOOLEAN,
#         Mac BOOLEAN,
#         Linux BOOLEAN,
#         Positive INTEGER,
#         Negative INTEGER,
#         ScoreRank INTEGER,
#         Developers TEXT,
#         Publishers TEXT,
#         Categories TEXT,
#         Genres TEXT,
#         Tags TEXT
#     )
#     ''')
#     conn.commit()
#     conn.close()

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     user_type = data.get('user_type')
#     password = data.get('password', '')

#     if user_type == 'admin' and password != ADMIN_PASSWORD:
#         return jsonify({'success': False, 'message': 'Invalid password'}), 401
#     return jsonify({'success': True})

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part in the request'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No file selected'}), 400

#     if file:
#         df = pd.read_csv(file)
#         df.columns = [column.replace(' ', '') for column in df.columns]
#         init_db()
#         conn = sqlite3.connect(DATABASE)
#         df.to_sql('games', conn, if_exists='replace', index=False)
#         conn.close()
#         return jsonify({'message': 'File successfully uploaded'}), 200

# @app.route('/query', methods=['GET'])
# def query_data():
#     filters = request.args.to_dict()
#     query = "SELECT * FROM games WHERE "

#     conditions = []
#     parameters = []
#     for key, value in filters.items():
#         if key in ['AppID','ReleaseDate', 'RequiredAge', 'Price', 'DLCount', 'Positive', 'Negative', 'ScoreRank']:
#             conditions.append(f"{key} = ?")
#             parameters.append(value)
#         else:
#             conditions.append(f"{key} LIKE ?")
#             parameters.append(f"%{value}%")

#     query += " AND ".join(conditions)
#     conn = sqlite3.connect(DATABASE)
#     df = pd.read_sql_query(query, conn, params=parameters)
#     conn.close()
#     return df.to_json(orient='records')

# @app.route('/columns', methods=['GET'])
# def get_columns():
#     conn = sqlite3.connect(DATABASE)
#     c = conn.cursor()
#     c.execute("PRAGMA table_info(games)")
#     columns = [col[1] for col in c.fetchall()]
#     conn.close()
#     return jsonify(columns)

# if __name__ == '__main__':
#     init_db()
#     app.run(host='0.0.0.0', port=5000, debug=True)

# from flask import Flask, render_template, request, jsonify, session
# import pandas as pd
# import sqlite3
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)
# app.secret_key = 'your_secret_key_here'  # Set a secret key for session management

# DATABASE = 'game_data.db'
# ADMIN_PASSWORD = 'admin123'  # You can change this password as needed

# def init_db():
#     conn = sqlite3.connect(DATABASE)
#     c = conn.cursor()
#     c.execute('''
#     CREATE TABLE IF NOT EXISTS games (
#         Unnamed INTEGER,
#         AppID INTEGER PRIMARY KEY,
#         Name TEXT,
#         ReleaseDate TEXT,
#         RequiredAge INTEGER,
#         Price REAL,
#         DLCount INTEGER,
#         AboutGame TEXT,
#         SupportedLanguages TEXT,
#         Windows BOOLEAN,
#         Mac BOOLEAN,
#         Linux BOOLEAN,
#         Positive INTEGER,
#         Negative INTEGER,
#         ScoreRank INTEGER,
#         Developers TEXT,
#         Publishers TEXT,
#         Categories TEXT,
#         Genres TEXT,
#         Tags TEXT
#     )
#     ''')
#     conn.commit()
#     conn.close()

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     user_type = data.get('user_type')
#     password = data.get('password', '')

#     if user_type == 'admin' and password != ADMIN_PASSWORD:
#         return jsonify({'success': False, 'message': 'Invalid password'}), 401

#     session['logged_in'] = True
#     session['user_type'] = user_type
#     return jsonify({'success': True})

# @app.route('/logout', methods=['POST'])
# def logout():
#     session.clear()
#     return jsonify({'success': True})

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'logged_in' not in session or not session['logged_in']:
#         return jsonify({'error': 'Unauthorized access'}), 401

#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part in the request'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No file selected'}), 400

#     if file:
#         df = pd.read_csv(file)
#         df.columns = [column.replace(' ', '') for column in df.columns]
#         init_db()
#         conn = sqlite3.connect(DATABASE)
#         df.to_sql('games', conn, if_exists='replace', index=False)
#         conn.close()
#         return jsonify({'message': 'File successfully uploaded'}), 200

# @app.route('/query', methods=['GET'])
# def query_data():
#     if 'logged_in' not in session or not session['logged_in']:
#         return jsonify({'error': 'Unauthorized access'}), 401

#     filters = request.args.to_dict()
#     query_type = filters.pop('query_type', 'select')
#     agg_column = filters.pop('agg_column', None)
#     agg_function = filters.pop('agg_function', None)

#     if query_type == 'select':
#         query = "SELECT * FROM games WHERE "

#         conditions = []
#         parameters = []
#         for key, value in filters.items():
#             if key in ['AppID', 'ReleaseDate', 'RequiredAge', 'Price', 'DLCount', 'Positive', 'Negative', 'ScoreRank']:
#                 conditions.append(f"{key} = ?")
#                 parameters.append(value)
#             else:
#                 conditions.append(f"{key} LIKE ?")
#                 parameters.append(f"%{value}%")

#         query += " AND ".join(conditions)
#         conn = sqlite3.connect(DATABASE)
#         df = pd.read_sql_query(query, conn, params=parameters)
#         conn.close()
#         return df.to_json(orient='records')

#     elif query_type == 'aggregate' and agg_column and agg_function:
#         if agg_function.lower() == 'mean':
#             agg_function = 'AVG'
#         query = f"SELECT {agg_function.upper()}({agg_column}) as result FROM games WHERE "

#         conditions = []
#         parameters = []
#         for key, value in filters.items():
#             if key in ['AppID', 'ReleaseDate', 'RequiredAge', 'Price', 'DLCount', 'Positive', 'Negative', 'ScoreRank']:
#                 conditions.append(f"{key} = ?")
#                 parameters.append(value)
#             else:
#                 conditions.append(f"{key} LIKE ?")
#                 parameters.append(f"%{value}%")

#         query += " AND ".join(conditions) if conditions else "1=1"  # Ensure there is a valid SQL query
#         conn = sqlite3.connect(DATABASE)
#         result = pd.read_sql_query(query, conn, params=parameters)
#         conn.close()
#         return result.to_json(orient='records')

#     return jsonify({'error': 'Invalid query type or missing parameters'}), 400

# @app.route('/columns', methods=['GET'])
# def get_columns():
#     conn = sqlite3.connect(DATABASE)
#     c = conn.cursor()
#     c.execute("PRAGMA table_info(games)")
#     columns = [col[1] for col in c.fetchall()]
#     conn.close()
#     return jsonify(columns)


# if __name__ == '__main__':
#     init_db()
#     app.run(host='0.0.0.0', port=5000, debug=True)


from flask import Flask, render_template, request, jsonify, session
import pandas as pd
import sqlite3
from flask_cors import CORS
import requests
from io import StringIO
import logging
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key_here'  # Set a secret key for session management

DATABASE = 'game_data.db'
ADMIN_PASSWORD = 'admin123'  # You can change this password as needed

# Set up logging
logging.basicConfig(level=logging.DEBUG)

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS games (
        Unnamed INTEGER,
        AppID INTEGER PRIMARY KEY,
        Name TEXT,
        ReleaseDate TEXT,
        RequiredAge INTEGER,
        Price REAL,
        DLCount INTEGER,
        AboutGame TEXT,
        SupportedLanguages TEXT,
        Windows BOOLEAN,
        Mac BOOLEAN,
        Linux BOOLEAN,
        Positive INTEGER,
        Negative INTEGER,
        ScoreRank INTEGER,
        Developers TEXT,
        Publishers TEXT,
        Categories TEXT,
        Genres TEXT,
        Tags TEXT
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user_type = data.get('user_type')
    password = data.get('password', '')

    if user_type == 'admin' and password != ADMIN_PASSWORD:
        return jsonify({'success': False, 'message': 'Invalid password'}), 401

    session['logged_in'] = True
    session['user_type'] = user_type
    return jsonify({'success': True})

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True})


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'logged_in' not in session or not session['logged_in']:
        return jsonify({'error': 'Unauthorized access'}), 401

    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    try:
        # Check if the file is a CSV
        if not file.filename.endswith('.csv'):
            return jsonify({'error': 'File must be a CSV'}), 400

        # Read the CSV file in chunks to handle large files
        chunk_size = 10000  # Adjust chunk size as needed
        reader = pd.read_csv(file, chunksize=chunk_size)

        # Initialize database and connection
        init_db()
        conn = sqlite3.connect(DATABASE)

        # Variable to check if it's the first chunk
        first_chunk = True

        # Iterate over chunks and append to SQLite table
        for chunk in reader:
            chunk.columns = [column.replace(' ', '') for column in chunk.columns]
            if_exists_option = 'replace' if first_chunk else 'append'
            chunk.to_sql('games', conn, if_exists=if_exists_option, index=False)
            first_chunk = False

        conn.close()
        return jsonify({'message': 'File successfully uploaded'}), 200

    except Exception as e:
        return jsonify({'error': f'Error processing file: {str(e)}'}), 500

@app.route('/upload_csv_from_link', methods=['POST'])
def upload_csv_from_link():
    logging.debug('Request received at /upload_csv_from_link')
    data = request.get_json()
    csv_link = data.get('csv_link')
    logging.debug(f'CSV link: {csv_link}')
    
    try:
        response = requests.get(csv_link, stream=True)  # Stream the content
        response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
        logging.debug('CSV file fetched successfully')
        
        # Check if the content type is CSV
        if 'text/csv' not in response.headers.get('content-type', ''):
            return jsonify({'success': False, 'error': 'The provided link does not point to a CSV file.'}), 400
        
        # Read the CSV in chunks
        chunk_size = 10000  # Number of lines per chunk
        df_chunks = []
        
        for chunk in pd.read_csv(StringIO(response.text), delimiter=',', chunksize=chunk_size):
            df_chunks.append(chunk)
        
        # Concatenate all chunks into a single DataFrame
        df = pd.concat(df_chunks, ignore_index=True)
        
        logging.debug('CSV data read into DataFrame')
        df.columns = [column.replace(' ', '') for column in df.columns]
        init_db()
        conn = sqlite3.connect(DATABASE)
        df.to_sql('games', conn, if_exists='replace', index=False)
        conn.close()
        logging.debug('DataFrame written to database')
        
        return jsonify({'success': True}), 200
    
    except requests.exceptions.RequestException as e:
        logging.error(f'Error fetching CSV file: {e}')
        return jsonify({'success': False, 'error': f'Error fetching CSV file: {e}'}), 500
    
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        return jsonify({'success': False, 'error': f'Unexpected error: {e}'}), 500

def parse_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%m/%d/%Y').date()
        return date_obj.strftime('%Y-%m-%d')  # Convert to YYYY-MM-DD format
    except ValueError:
        return None

@app.route('/query', methods=['GET'])
def query_data():
    if 'logged_in' not in session or not session['logged_in']:
        return jsonify({'error': 'Unauthorized access'}), 401

    filters = request.args.to_dict()
    query_type = filters.pop('query_type', 'select')
    agg_column = filters.pop('agg_column', None)
    agg_function = filters.pop('agg_function', None)

    if query_type == 'select':
        query = "SELECT * FROM games WHERE "

        conditions = []
        parameters = []
        for key, value in filters.items():
            if key in ['AppID', 'Releasedate', 'Requiredage', 'Price', 'DLCcount', 'Positive', 'Negative', 'Scorerank']:
                # if key == 'Releasedate':
                #     formatted_date = parse_date(value)
                #     if formatted_date:
                #         conditions.append("Releasedate = ?")
                #         parameters.append(value)
                #     else:
                #         return jsonify({'error': f'Invalid date format for {key}. Use "MM/DD/YYYY" format.'}), 400
                # else:
                conditions.append(f"{key} = ?")
                parameters.append(value)
            else:
                conditions.append(f"{key} LIKE ?")
                parameters.append(f"%{value}%")

        query += " AND ".join(conditions)
        conn = sqlite3.connect(DATABASE)
        df = pd.read_sql_query(query, conn, params=parameters)
        conn.close()
        return df.to_json(orient='records')

    elif query_type == 'aggregate' and agg_column and agg_function:
        if agg_function.lower() == 'mean':
            agg_function = 'AVG'
        query = f"SELECT {agg_function.upper()}({agg_column}) as result FROM games WHERE "

        conditions = []
        parameters = []
        for key, value in filters.items():
            if key in ['AppID', 'Releasedate', 'Requiredage', 'Price', 'DLCcount', 'Positive', 'Negative', 'Scorerank']:
                if key == 'ReleaseDate':
                    date_obj = parse_date(value)
                    if date_obj:
                        formatted_date = date_obj.strftime('%b %d, %Y')
                        conditions.append(f"{key} = ?")
                        parameters.append(formatted_date)
                    else:
                        continue
                else:
                    conditions.append(f"{key} = ?")
                    parameters.append(value)
            else:
                conditions.append(f"{key} LIKE ?")
                parameters.append(f"%{value}%")

        query += " AND ".join(conditions) if conditions else "1=1"  # Ensure there is a valid SQL query
        conn = sqlite3.connect(DATABASE)
        result = pd.read_sql_query(query, conn, params=parameters)
        conn.close()
        return result.to_json(orient='records')

    return jsonify({'error': 'Invalid query type or missing parameters'}), 400
# @app.route('/columns', methods=['GET'])
# def get_columns():
#     try:
#         conn = sqlite3.connect(DATABASE)
#         c = conn.cursor()
#         c.execute("PRAGMA table_info(games)")
#         columns = [col[1] for col in c.fetchall()]
#         conn.close()
#         logging.debug(f'Columns fetched: {columns}')
#         return jsonify(columns), 200
#     except Exception as e:
#         logging.error(f'Error fetching columns: {e}')
#         return jsonify({'success': False, 'error': f'Error fetching columns: {e}'}), 500

@app.route('/columns', methods=['GET'])
def get_columns():
    try:
        conn = sqlite3.connect(DATABASE)
        query = "PRAGMA table_info(games)"
        result = conn.execute(query).fetchall()
        columns = [row[1] for row in result]  # row[1] contains the column name
        conn.close()
        
        logging.debug(f'Columns fetched: {columns}')
        return jsonify(columns), 200
    except Exception as e:
        logging.error(f'Error fetching columns: {e}')
        return jsonify({'success': False, 'error': f'Error fetching columns: {e}'}), 500


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
