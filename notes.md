# Travel Mini API NOtes
## Project Goal
Create a mini backend API using:
- Flask
- pandas
- CSV files

this project simulates Coral-like multi-source querying concepts.

---

# Technologies used

| Tool | Purpose|
|---|---|
| Flask | backend API |
| pandas | CSV/data handling |
| CSV | data source|
|python | programming language|

---

# Project Structure

```text
travel-mini-api/
│
├── app.py
├── bookings.csv
├── drivers.csv
└── NOTES.md
```

---

# bookings.csv

Stores booking information.

Example:

```csv
id,customer,location,payment,driver_id
1,Ravi,Chennai,Paid,101
2,Ajay,Bangalore,Pending,102
3,Sneha,Hyderabad,Paid,101
```

---

# drivers.csv

Stores driver details.

Example:

```csv
id,driver_name,vehicle
101,Suresh,Innova
102,Ramesh,Ertiga
```

---

# Flask Basics

## Create Flask App

```python
app = Flask(__name__)
```

Creates backend application.

---

# Routes

## Home Route

```python
@app.route("/")
```

URL:
```text
/
```

Returns:
```json
{
  "message": "Travel Mini API 🚀"
}
```

---

# Bookings Route

```python
@app.route("/bookings")
```

URL:
```text
/bookings
```

Purpose:
- read bookings.csv
- return all bookings

---

# Drivers Route

```python
@app.route("/drivers")
```

URL:
```text
/drivers
```

Purpose:
- read drivers.csv
- return all drivers

---

# Dynamic Route

```python
@app.route("/booking/<customer>")
```

Example URLs:

```text
/booking/Ravi
/booking/Ajay
```

Purpose:
- filter bookings using customer name

---

# Pandas Basics

## Read CSV

```python
pd.read_csv("bookings.csv")
```

Purpose:
- load CSV into pandas dataframe

---

# Convert To JSON Format

```python
data.to_dict(orient="records")
```

Purpose:
- convert dataframe into list of dictionaries
- Flask can return it as JSON

Example Output:

```json
[
  {
    "id": 1,
    "customer": "Ravi"
  }
]
```

---

# Filtering Data

```python
filtered = data[data["payment"] == "Pending"]
```

Purpose:
- select rows matching condition

Similar SQL Query:

```sql
SELECT * FROM bookings WHERE payment = 'Pending';
```

---

# JOIN / Merge Concept

## Pandas Merge

```python
pd.merge(
    bookings,
    drivers,
    left_on="driver_id",
    right_on="id"
)
```

Purpose:
- combine bookings and drivers data

---

# left_on

```python
left_on="driver_id"
```

Means:
- use driver_id column from LEFT table

LEFT table:
```python
bookings
```

---

# right_on

```python
right_on="id"
```

Means:
- use id column from RIGHT table

RIGHT table:
```python
drivers
```

---

# Merge Meaning

Match:

```text
bookings.driver_id = drivers.id
```

Similar SQL Query:

```sql
SELECT bookings.customer, drivers.driver_name
FROM bookings
JOIN drivers
ON bookings.driver_id = drivers.id;
```

---

# Order Of Returned Data

After merge:
- LEFT table columns appear first
- RIGHT table columns appear later

---

# Important Learning

This project demonstrates:
- backend APIs
- CSV handling
- filtering
- dynamic routes
- cross-source joins
- structured JSON responses

---

# Relation To Coral

Coral combines:
- databases
- CSVs
- APIs
- multiple sources

using SQL-style querying.

This project manually simulates those concepts.