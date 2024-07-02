import streamlit as st
import random
import requests
import json
import time

st.session_state.is_trending = True
URL = "https://3fphf6jrfg.execute-api.ap-south-1.amazonaws.com/DEV/Trucks"#since it is a public api , removed it

brake_status_lst =["Good","Bad","Average"]
transmission_status_Lst =["Operational","Failure"]
def generate_truck_data(num_trucks):
    trucks = []
    for Num in range(num_trucks):
        Speed =float(random.randrange(10,150))
        truck = {
            "truck_id": f"Truck_id{Num}",
            "vehicle_speed":Speed,
            "odometer_reading": float(random.randrange(10000,90000)),
            "fuel_consumption":float(random.randrange(1,100)),
            "gps_location": {
                "latitude": random.uniform(-90, 90),
                "longitude": random.uniform(-180, 180),
                "speed": Speed,
                "altitude": float(random.randrange(1,100))
            },
            "engine_diagnostics": {
                "engine_rpm": float(random.randrange(1000,5000)),
                "fuel_level": float(random.randrange(1,100)),
                "temperature": float(random.randrange(1,100)),
                "oil_pressure": float(random.randrange(1,100)),
                "battery_voltage": float(random.randrange(10,14))
            },
            "vehicle_health_and_maintenance": {
                "brake_status": random.choice(brake_status_lst),
                "transmission_status": random.choice(transmission_status_Lst),
                "tire_pressure":{
                    "front_left": float(random.randrange(10,40)),
                    "front_right":float(random.randrange(10,40)), 
                    "rear_left": float(random.randrange(10,40)),
                    "rear_right": float(random.randrange(10,40))
                }
            },
             "environmental_conditions": {
                "humidity": float(random.randrange(1,100)),
                "temperature": float(random.randrange(1,100)),
                "atmospheric_pressure": float(random.randrange(1,100))
            }
        }
        trucks.append(truck)
    data = json.dumps({"trucks": trucks})
    headers = {"Content-Type":"application/json"}
    requests.request("POST",URL,headers = headers,data = data)



while st.session_state.is_trending:
    Sql = generate_truck_data(3)
        #print("Fetching data every one tw")
    time.sleep(60) 

with st.container():
    n = st.text_input("Enter the no of Truck data to be generated")

    if st.button("Generate Truck Data"):
        generate_truck_data(int(n))