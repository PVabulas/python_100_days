import requests
from datetime import datetime
from time import sleep

MY_LAT = 51.478370  # Your latitude
MY_LONG = -0.086990  # Your longitude


def check_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        iss_near = True
    else:
        iss_near = False

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    # If the ISS is close to my current position
    # and it is currently dark
    if not (sunrise <= time_now.hour <= sunset):
        is_dark = True
    else:
        is_dark = False
    # Then send me an email to tell me to look up.
    if iss_near and iss_near == True:
        print("Look up")
    elif iss_near:
        print("Too light to see ISS")
    elif is_dark:
        print("Go to sleep")
    else:
        print("Nothing happening")


# BONUS: run the code every 60 seconds.


if __name__ == "__main__":
    for i in range(2):
        check_iss()
        sleep(20)
