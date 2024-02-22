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
@app.route("/energy")
def clacu():
    return render_template("energy.html")
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
        
        # Create an empty list to store the appliance values
        appliances = [0,0,0,0,0,0,0,0,0,0,0,0]

        # Retrieve input values from the form
        for i in range(1, 4):  # Loop through categories
            category = f"appliance{i}"
            for j in range(1, 5):  # Loop through appliances within each category
                appliance = f"{category}{j}"
                value = int(request.form.get(appliance, 0))  # Get the value from the form
                appliances.append(value)
                    
        # Assign the input values to variables

        # Now you can perform calculations using these variables 
        def handle_input(input_value,appliances):
            if i == 0:
                ans=800
                if (appliances[i]>0):
                    ans+=(appliances[i]-1)*600/3
                return ans
            elif i == 1:
                ans=3000
                if (appliances[i]>0):
                    ans+=(appliances[i]-1)*3000/3
                return ans
            elif i == 2:
                ans=1800
                if (appliances[i]>0):
                    ans+=(appliances[i]-1)*1800/3
                return ans
            elif i == 3:
                ans=500
                if (appliances[i]>0):
                    ans+=(appliances[i]-1)*500/3
                return ans
            elif i == 4:
                ans=600
                if (appliances[i]>0):
                    ans+=(appliances[i]-1)*600/3
                return ans
            elif i == 5:
                ans=900
                if (appliances[i]>0):
                    ans+=(appliances[i]-1)*900/3
                return ans
            elif i == 6:
                ans=900
                if (appliances[i]>0):
                    ans+=(appliances[i]-1)*900/3
                return ans
            elif i == 7:
                ans=7680
                if (appliances[i]>0):
                    ans+=(appliances[i]-1)*7680/3
                return ans
            elif i == 8:
                ans=4000
                if (appliances[i]>0):
                    ans+=(appliances[i]-1)*4000/3
                return ans        
            elif i == 9:
                ans=4000
                if (appliances[i]>0):
                    ans+=(appliances[i]-1)*4000/3
                return ans
            elif i == 10:
                ans=750
                if (appliances[i]>0): 
                    ans+=(appliances[i]-1)*750/2
                return ans                        
            elif i == 11:
                ans=750
                if (appliances[i]>0):
                    ans+=(appliances[i]-1)*750/2
                return ans      
        Sub_1=0
        Sub_2=0
        Sub_3=0
        for i in range(12):
            x=handle_input(i,appliances)
            if(i<4):
                Sub_1 +=x
            elif(i>=4 and i<8):
                Sub_2 +=x
            else:
                Sub_3 +=x
        sd = scalemodel.transform([[241.2317, Sub_1, Sub_2, Sub_3]])
        p1 = mainmodel.predict(sd)
        an = scalemodel.inverse_transform(sd)
        energy=an[0,0]
        energy =((p1)*1000)/60 - Sub_1 - Sub_2 - Sub_3
        carbonfootprints= 852.3*(energy/1000)
        daybill= 18*(energy/1000)
        return render_template("dailybill.html",cf=carbonfootprints,bill=daybill)
    except Exception as e:
        print(e)  # Print the error for debugging purposes
        return redirect(url_for('error'))
@app.route('/error')
def error():
    return render_template('error.html')
@app.route("/monthly_Bill", methods=['POST'])
def monthly_Bill():
    volt = 240
    appliances = []
    # Retrieve input values from the form
    for i in range(1, 4):
        category = f"{i}appliance"
        for j in range(1, 5):
            appliance = f"{category}{j}"
            value = int(request.form.get(appliance, 0))
            appliances.append(value)
                    
        # Assign the input values to variables
    Microwave, Oven, Dishwasher, Mixer = appliances[:4]
    electricwaterheater, washing, tumble, refrigerator = appliances[4:8]
    light, airconditioner, fan, television = appliances[8:]
    def handle_input(input_value,appliances):
        if i == 0:
            Microwave=800
            if (appliances[i]>1):
                Microwave+=(appliances[i]-1)*600/3
        elif i == 1:
            Oven=3000
            if (appliances[i]>1):
                Oven+=(appliances[i]-1)*3000/3
        elif i == 2:
            Dishwasher=1800
            if (appliances[i]>1):
                Dishwasher+=(appliances[i]-1)*1800/3
        elif i == 3:
            Mixer=500
            if (appliances[i]>1):
                Mixer+=(appliances[i]-1)*500/3
        elif i == 4:
            light=600
            if (appliances[i]>1):
                light+=(appliances[i]-1)*600/3
        elif i == 5:
            washing=900
            if (appliances[i]>1):
                washing+=(appliances[i]-1)*900/3
        elif i == 6:
            tumble=900
            if (appliances[i]>1):
                tumble+=(appliances[i]-1)*900/3
        elif i == 7:
            refrigerator=7680
            if (appliances[i]>1):
                refrigerator+=(appliances[i]-1)*7680/3
        elif i == 8:
            electricwaterheater=4000
            if (appliances[i]>1):
                electricwaterheater+=(appliances[i]-1)*4000/3        
        elif i == 9:
            airconditioner=4000
            if (appliances[i]>1):
                airconditioner+=(appliances[i]-1)*4000/3
        elif i == 10:
            fan=75
            if (appliances[i]>1):
                fan+=(appliances[i]-1)*750/2                        
        elif i == 11:
            televison=75
            if (appliances[i]>1):
                television+=(appliances[i]-1)*75/2      
    for i in (0,10):
        handle_input(i,appliances)
    
    Sub_1 = Microwave+Oven+Dishwasher+Mixer
    Sub_2 = light+washing+tumble+refrigerator
    Sub_3 = electricwaterheater+airconditioner+fan+television
    sd = scalemodel.transform([[241.2317, Sub_1, Sub_2, Sub_3]])
    p1 = mainmodel.predict(sd)
    sd[0, 0] = p1
    ans = scalemodel.inverse_transform(sd)
    energy=ans[0,0]
    #energy =(((ans[0, 0])*1000)/60) - Sub_1 - Sub_2 -Sub_3
    carbonfootprints= round((852.3*(energy/1000))* 28)
    daybill= round((18*(energy/1000))*28)
    return render_template("monthly_bill.html",cf=carbonfootprints,bill=daybill)    
    
    # volt = 240
    # if request.method == 'POST':
    #      Microwave = int(request.form['1appliance1']) * 800
    #      Oven = int(request.form['1appliance2']) * 3000
    #      Dishwasher = int(request.form['1appliance3']) * 1800
    #      Mixer = int(request.form['1appliance4']) * 500
    #      Sub_1 = Microwave+Oven+Dishwasher+Mixer
    #      light = int(request.form['2appliance1']) * 230
    #      washing= int(request.form['2appliance2']) * 900
    #      tumble = int(request.form['2appliance3']) * 900
    
    #      refrigerator = int(request.form['2appliance4']) * 7680
    #      Sub_2 = light+washing+tumble+refrigerator
    #      electricwaterheater = int(request.form['3appliance1']) * 4000
    #      airconditioner= int(request.form['3appliance2']) * 25000
    #      Sub_3 = electricwaterheater+airconditioner
    #      sd = scalemodel.transform([[0, volt, 241.2317, Sub_1, Sub_2, Sub_3]])
    #      p1 = mainmodel.predict([[sd[0, 1], sd[0, 3], sd[0, 4], sd[0, 5]]])
    #      sd[0, 0] = p1
    #      ans = scalemodel.inverse_transform(sd)
    # return "The total energy usage in one is : {}".format(ans[0, 0])
#new Features in website 
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
