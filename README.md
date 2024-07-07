
---

# Game Data Analysis Web Application

This web application allows users to upload game data CSV files, query the data, and perform aggregate operations. The application is built using Flask, SQLite, and pandas on the backend, with HTML, CSS, and JavaScript for the frontend.

## Features

- User login with roles (admin and guest)
- Upload game data CSV files
- Fetch and upload game data from a public CSV link
- Query data with filters
- Perform aggregate operations on numerical data
- View results in a tabular format

## Setup

### Prerequisites

- Python 3.9
- Flask
- pandas
- requests
- flask-cors

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yasar03/Flask-App-Image.git
    cd Flask-App-Image
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Initialize the database:
    ```bash
    python -c "from app import init_db; init_db()"
    ```

### Configuration

Set your secret key and admin password in the `app.py` file:
    ```python
    app.secret_key = 'your_secret_key_here'
    ADMIN_PASSWORD = 'admin123'
    ```

### Running the Application

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://localhost:5000`.

### Deployment

The application is deployed and can be accessed at: [https://flask-app-image.onrender.com/](https://flask-app-image.onrender.com/)

## Usage

### Login

- Select your user type (admin or guest).
- If you are an admin, enter the admin password.

![This is a login page image](images/login.png)

### Upload CSV

- To upload a CSV file from your system:
    - Select the CSV file.
    - Click on the "Upload CSV from system" button.
- To upload a CSV file from a public link:
    - Enter the CSV link.
    - Click on the "Fetch CSV" button.

Sample CSV file link: [Sample CSV](https://docs.google.com/spreadsheets/d/e/2PACX-1vTAJTNsWIenb3UrPMjh5KmtJ9VA4U4YuMIFvmPPqi1npcVW12Btu0zZ7tgsdRm25zsEXsN2rcLfee9b/pub?gid=1065064397&single=true&output=csv)

![To fetch or upload CSV](images/fetchCSV.png)

### Query Data

1. Select the column you want to query.
2. If filtering:
    - Enter the filter value.
    - If column is of string type then substring matching is allowed if it is numeric or date type then only exact value match is allowed
    - If a numeric type column is selected then only filter operator dropdown will appear. Select the filter operator (Equal to, Greater than, Less than, Greater than or equal to, Less than or equal to).
    - Click on the "Filtered Query" button.
3. If aggregating(Only for numeric type column):
    - Select the aggregate function (Sum, Max, Min, Mean).
    - Click on the "Aggregate Data Query" button.

- List of column names in the dropdown menu to be selected for making query:
![List of column names](images/columnNames.png)

- Filtered query on a string type column:
![query on name](images/stringQuery.png)

- Filtered query on date:
![Alt text](images/dateQuery.png)

- Filtered query on numeric type column with filter operator:
![Alt text](images/numericQuery.png)

- Aggregate data query on numeric type column:
![Alt text](images/aggregate.png)

### Logout

- Clear your session by sending a POST request to `/logout`.

## API Endpoints

### `POST /login`

**Request:**
```json
{
  "user_type": "admin",
  "password": "admin123"
}
```

**Response:**
- Success:
    ```json
    {
      "success": true
    }
    ```
- Failure:
    ```json
    {
      "success": false,
      "message": "Invalid password"
    }
    ```

### `POST /logout`

**Request:**
```json
{
  // No data needed for this request
}
```

**Response:**
```json
{
  "success": true
}
```

### `POST /upload`

**Request:**
- Form Data:
    - `file`: The CSV file to be uploaded.

**Response:**
- Success:
    ```json
    {
      "message": "File successfully uploaded"
    }
    ```
- Failure:
    ```json
    {
      "error": "Error message explaining the failure"
    }
    ```

### `POST /upload_csv_from_link`

**Request:**
```json
{
  "csv_link": "https://example.com/data.csv"
}
```

**Response:**
- Success:
    ```json
    {
      "success": true
    }
    ```
- Failure:
    ```json
    {
      "success": false,
      "error": "Error message explaining the failure"
    }
    ```

### `GET /query`

**Request:**
- Query Parameters:
    - For filtered query:
        ```
        ?query_type=select&filter_column=Price&filter_value=20&filter_operator=gt
        ```
    - For aggregate query:
        ```
        ?query_type=aggregate&agg_column=Price&agg_function=sum
        ```

**Response:**
- Success:
    ```json
    [
      {
        "AppID": 12345,
        "Name": "Game Name",
        "Price": 19.99,
        ...
      },
      ...
    ]
    ```
- Failure:
    ```json
    {
      "error": "Invalid query type or missing parameters"
    }
    ```

### `GET /columns`

**Request:**
```json
{
  // No data needed for this request
}
```

**Response:**
- Success:
    ```json
    [
      "Unnamed",
      "AppID",
      "Name",
      "ReleaseDate",
      "RequiredAge",
      "Price",
      ...
    ]
    ```
- Failure:
    ```json
    {
      "success": false,
      "error": "Error message explaining the failure"
    }
    ```

## Frontend

The frontend is implemented in HTML, CSS, and JavaScript. It includes forms for login, CSV upload, and data querying. The results are displayed in a table format.

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

---
