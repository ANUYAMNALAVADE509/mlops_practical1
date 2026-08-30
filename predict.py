import joblib
import pandas as pd
model = joblib.load("telecom_tower_model.pkl")
new_data=pd.DataFrame({
    "Tower_ID":1005,
    "Temperature_C":[57],
    "Battery_Voltage":[50.91],
    "Power_Consumption_W":[2808],
    "Signal_Strength_Percent":[69],
    "Fan_Speed_RPM":[2838],
    "Humidity_Percent":[36],
    "Traffic_Load":[2612],
    "Tower_Age_Years":[6]
    })
prediction=model.predict(new_data)
if prediction[0]==1:
    print("Hardware Failure predicted")
else:
    print("Tower is Healthy")
        
