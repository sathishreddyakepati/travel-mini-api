from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Travel Mini API 🚀"
    }

@app.route("/bookings")
def bookings():

    data = pd.read_csv("bookings.csv")

    return {
        "bookings": data.to_dict(orient="records")
    }

@app.route("/drivers")
def drivers():

    data = pd.read_csv("drivers.csv")

    return {
        "drivers": data.to_dict(orient="records")
    }

@app.route("/booking/<customer>")
def booking(customer):

    data = pd.read_csv("bookings.csv")

    filtered = data[data["customer"] == customer]

    return {
        "booking": filtered.to_dict(orient="records")
    }
@app.route("/full-bookings")
def full_bookings():

    bookings = pd.read_csv("bookings.csv")

    drivers = pd.read_csv("drivers.csv")

    merged = pd.merge(
        bookings,
        drivers,
        left_on="driver_id",
        right_on="id"
    )
    merged = merged[
    [
        "customer",
        "location",
        "payment",
        "driver_name",
        "vehicle"
    ]
]

    return {
        "full_bookings": merged.to_dict(orient="records")
    }
@app.route("/pending-bookings")
def pending_bookings():

    bookings = pd.read_csv("bookings.csv")
    filtered_bookings = bookings[bookings["payment"]== "Pending"]


    return {
        "pending_bookings": filtered_bookings.to_dict(orient="records")
    }

app.run(debug=True)
