from flask import Flask,render_template,url_for,request,redirect
app = Flask(__name__)
import requests
import numpy as np
import joblib
mainmodel = joblib.load(r"models\my_model.pkl")
scalemodel = joblib.load(r"models\my_scaler.pkl")
weathermodel = joblib.load(r"models\wea_model.pkl")
weatherscaler = joblib.load(r"models\wea_scaler.pkl")
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/daily",methods=['GET', 'POST'])
def daily():
    return render_template("dailyform.html")
@app.route("/monthly",methods=['GET', 'POST'])
def monthly():
    return render_template("monthlyform.html")
@app.route('/Daily_Bill', methods=['POST'])
def Daily_Bill():
    try:
            # Define the voltage (assuming 240 volts)
        voltage = 240   
               # Initialize variables with appropriate names
        microwave = int(request.form.get('appliance1', 0))
        oven = int(request.form.get('appliance2', 0))
        dishwasher = int(request.form.get('appliance3', 0))
        hand_mixer = int(request.form.get('appliance4', 0))
        electricwaterheater = int(request.form.get('appliance5', 0))
        washing_machine = int(request.form.get('appliance6', 0))
        tumble_drier = int(request.form.get('appliance7', 0))
        refrigerator = int(request.form.get('appliance8', 0))
        light = int(request.form.get('appliance9', 0))
        airconditioner = int(request.form.get('appliance10', 0))
        fan = int(request.form.get('appliance11', 0))
        television = int(request.form.get('appliance12', 0))
        print(microwave)
        print(dishwasher) 
        def handle_input(input_value, microwave, oven, dishwasher, hand_mixer, electricwaterheater, washing_machine, tumble_drier, refrigerator, light, airconditioner, fan, television):
            if input_value == 0:
                ans = 800
                if microwave > 0:
                    ans += (microwave - 1) * 600 / 3
                else:
                    ans=0
                return ans
            elif input_value == 1:
                ans = 3000
                if oven > 0:
                    ans += (oven - 1) * 3000 / 3
                else:
                    ans=0
                return ans
            elif input_value == 2:
                ans = 1800
                if dishwasher > 0:
                    ans += (dishwasher - 1) * 1800 / 3
                else:
                    ans=0
                return ans
            elif input_value == 3:
                ans = 500
                if hand_mixer > 0:
                    ans += (hand_mixer - 1) * 500 / 3
                else:
                    ans=0
                return ans
            elif input_value == 4:
                ans = 600
                if electricwaterheater > 0:
                    ans += (electricwaterheater - 1) * 600 / 3
                else:
                    ans=0
                return ans
            elif input_value == 5:
                ans = 900
                if washing_machine > 0:
                    ans += (washing_machine - 1) * 900 / 3
                else:
                    ans=0
                return ans
            elif input_value == 6:
                ans = 900
                if tumble_drier > 0:
                    ans += (tumble_drier - 1) * 900 / 3
                else:
                    ans=0
                return ans
            elif input_value == 7:
                ans = 7680
                if refrigerator > 0:
                    ans += (refrigerator - 1) * 7680 / 3
                else:
                    ans=0
                return ans
            elif input_value == 8:
                ans = 4000
                if light > 0:
                    ans += (light - 1) * 4000 / 3
                else:
                    ans=0
                return ans
            elif input_value == 9:
                ans = 4000
                if airconditioner > 0:
                    ans += (airconditioner - 1) * 4000 / 3
                else:
                    ans=0
                return ans
            elif input_value == 10:
                ans = 750
                if fan > 0:
                    ans += (fan - 1) * 750 / 2
                else:
                    ans=0
                return ans
            elif input_value == 11:
                ans = 750
                if television > 0:
                    ans += (television - 1) * 750 / 2
                else:
                    ans=0
                return ans      
        Sub_1=0
        Sub_2=0
        Sub_3=0
        sumlist=[]
        for i in range(12):
            x=handle_input(i,microwave, oven, dishwasher, hand_mixer, electricwaterheater, washing_machine, tumble_drier, refrigerator, light, airconditioner, fan, television)
            sumlist.append(x)
        print(sumlist[0])
        print(sumlist[1])
        print(sumlist[2])
        print(sumlist[3])
        if all(value == 0 for value in sumlist):
            return render_template('wronginput.html')
        Sub_1=sumlist[0]+sumlist[1]+sumlist[2]+sumlist[3]
        Sub_2=sumlist[4]+sumlist[5]+sumlist[6]+sumlist[7]
        Sub_3=sumlist[8]+sumlist[9]+sumlist[10]+sumlist[11]
        print(Sub_1)
        print(Sub_2)
        print(Sub_3)
        sd = scalemodel.transform([[241.2317, Sub_1, Sub_2, Sub_3]])
        p1 = mainmodel.predict(sd)
        an = scalemodel.inverse_transform(sd)
        energy=an[0,0]
        energy =((p1)*1000)/60 - Sub_1 - Sub_2 - Sub_3
        carbonfootprints= 852.3*(energy/1000)
        daybill= 18*(energy/1000)
        return render_template("dailybill.html",cf=carbonfootprints[0],bill=daybill[0])
    except Exception as e:
        print(e)  # Print the error for debugging purposes
        return redirect(url_for('error'))
@app.route('/error')
def error():
    return render_template('error.html')
@app.route("/monthly_Bill", methods=['POST'])
def monthly_Bill():
    try:
            # Define the voltage (assuming 240 volts)
        voltage = 240   
               # Initialize variables with appropriate names
        microwave = int(request.form.get('appliance1', 0))
        oven = int(request.form.get('appliance2', 0))
        dishwasher = int(request.form.get('appliance3', 0))
        hand_mixer = int(request.form.get('appliance4', 0))
        electricwaterheater = int(request.form.get('appliance5', 0))
        washing_machine = int(request.form.get('appliance6', 0))
        tumble_drier = int(request.form.get('appliance7', 0))
        refrigerator = int(request.form.get('appliance8', 0))
        light = int(request.form.get('appliance9', 0))
        airconditioner = int(request.form.get('appliance10', 0))
        fan = int(request.form.get('appliance11', 0))
        television = int(request.form.get('appliance12', 0))
        print(microwave)
        print(dishwasher) 
        def handle_input(input_value, microwave, oven, dishwasher, hand_mixer, electricwaterheater, washing_machine, tumble_drier, refrigerator, light, airconditioner, fan, television):
            if input_value == 0:
                ans = 800
                if microwave > 0:
                    ans += (microwave - 1) * 600 / 3
                else:
                    ans=0
                return ans
            elif input_value == 1:
                ans = 3000
                if oven > 0:
                    ans += (oven - 1) * 3000 / 3
                else:
                    ans=0
                return ans
            elif input_value == 2:
                ans = 1800
                if dishwasher > 0:
                    ans += (dishwasher - 1) * 1800 / 3
                else:
                    ans=0
                return ans
            elif input_value == 3:
                ans = 500
                if hand_mixer > 0:
                    ans += (hand_mixer - 1) * 500 / 3
                else:
                    ans=0
                return ans
            elif input_value == 4:
                ans = 600
                if electricwaterheater > 0:
                    ans += (electricwaterheater - 1) * 600 / 3
                else:
                    ans=0
                return ans
            elif input_value == 5:
                ans = 900
                if washing_machine > 0:
                    ans += (washing_machine - 1) * 900 / 3
                else:
                    ans=0
                return ans
            elif input_value == 6:
                ans = 900
                if tumble_drier > 0:
                    ans += (tumble_drier - 1) * 900 / 3
                else:
                    ans=0
                return ans
            elif input_value == 7:
                ans = 7680
                if refrigerator > 0:
                    ans += (refrigerator - 1) * 7680 / 3
                else:
                    ans=0
                return ans
            elif input_value == 8:
                ans = 4000
                if light > 0:
                    ans += (light - 1) * 4000 / 3
                else:
                    ans=0
                return ans
            elif input_value == 9:
                ans = 4000
                if airconditioner > 0:
                    ans += (airconditioner - 1) * 4000 / 3
                else:
                    ans=0
                return ans
            elif input_value == 10:
                ans = 750
                if fan > 0:
                    ans += (fan - 1) * 750 / 2
                else:
                    ans=0
                return ans
            elif input_value == 11:
                ans = 750
                if television > 0:
                    ans += (television - 1) * 750 / 2
                else:
                    ans=0
                return ans      
        Sub_1=0
        Sub_2=0
        Sub_3=0
        sumlist=[]
        for i in range(12):
            x=handle_input(i,microwave, oven, dishwasher, hand_mixer, electricwaterheater, washing_machine, tumble_drier, refrigerator, light, airconditioner, fan, television)
            sumlist.append(x)
        if all(value == 0 for value in sumlist):
            return render_template('wronginput.html')
        Sub_1=sumlist[0]+sumlist[1]+sumlist[2]+sumlist[3]
        Sub_2=sumlist[4]+sumlist[5]+sumlist[6]+sumlist[7]
        Sub_3=sumlist[8]+sumlist[9]+sumlist[10]+sumlist[11]
        sd = scalemodel.transform([[241.2317, Sub_1, Sub_2, Sub_3]])
        p1 = mainmodel.predict(sd)
        sd[0, 0] = p1
        ans = scalemodel.inverse_transform(sd)
        energy=ans[0,0]
        energy =(((ans[0, 0])*1000)/60) - Sub_1 - Sub_2 -Sub_3
        carbonfootprints= round((852.3*(energy/1000))* 28)
        daybill= round((18*(energy/1000))*28)
        return render_template("monthly_bill.html",cf=carbonfootprints,bill=daybill)    
    except Exception as e:
        print(e)  # Print the error for debugging purposes
        return redirect(url_for('error'))
@app.route("/weather")
def cu():
    return render_template("weather.html")

from geopy.geocoders import Nominatim
#Function to fetch weather data from API
# Create a geolocator instance
geolocator = Nominatim(user_agent="weather_app")

# Function to fetch weather data from API
def fetch_weather_data(location_name):
    # Get latitude and longitude based on location name
    location = geolocator.geocode(location_name)
    if location:
        lat = location.latitude
        lon = location.longitude
        
        # API URL with latitude and longitude
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid=877bf7d6e49041739cd8d0799d83a8f4'
        
        # Send a GET request to the API endpoint
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Process the data as needed
            relevant_data = {
                "temp_max": [(item['main']['temp_max'] - 273.15) for item in data['list']],  # Kelvin to Celsius
                "windspeed": [(item['wind']['speed'] * 3.6) for item in data['list']],  # m/s to km/h
                "pressure": [item['main']['pressure'] for item in data['list']],
                "feelslike": [(item['main']['feels_like'] - 273.15) for item in data['list']],  # Kelvin to Celsius
                "visibility": [(item['visibility']/1000) for item in data['list']],  # meters to kilometers
                "humidity": [(item['main']['humidity'] / 100) for item in data['list']],
                "temp_min": [(item['main']['temp_min'] - 273.15) for item in data['list']],  # percentage to fraction
            }
            return relevant_data
        else:
            # Return None if request failed
            print("Error fetching data from OpenWeatherMap API:", response.status_code)
            return None
    else:
        print("Location not found.")
        return None

@app.route("/weatherresult", methods=["GET", "POST"])
def weathers():
    location = request.form.get("location")
    weather_data = fetch_weather_data(location)
     # Initialize an empty list to store the initial elements
    li = []

     # Iterate over the keys in the weather_data dictionary
    for key in weather_data:
        li.append(weather_data[key][0])
            # Print the list containing the initial element
    inp=np.array(li).reshape(1,-1)
    ip=weatherscaler.transform(inp)
    p1=weathermodel.predict(ip)
    p=p1[0]
    return render_template("weatherresult.html",p1=p)
app.run(debug=True)
