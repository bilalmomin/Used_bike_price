from flask import Flask,request,render_template
import pandas as pd 
import pickle

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

app=Flask(__name__)
model=pickle.load(open('bike_price.pkl','rb'))
print(type(model))
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/home.html")
def return_home():
    return render_template("home.html")

@app.route("/predict", methods = ['GET','POST'])
def predict():
    if request.method == "POST":
        #Bike Model
        Bike_Model=0
        bike_model = request.form["bike_model"]
        if bike_model == 'TVS Star':
	        Bike_Model = 102
        elif bike_model == 'Royal Enfield':
            Bike_Model = 4249
        elif bike_model == 'TVS Apache':
            Bike_Model = 1061
        elif bike_model == 'Yamaha FZ V 2.0':
            Bike_Model = 93
        elif bike_model == 'Yamaha FZs':
            Bike_Model = 131
        elif bike_model == 'Honda CB Hornet':
            Bike_Model = 705
        elif bike_model == 'Hero Splendor':
            Bike_Model = 430
        elif bike_model == 'Yamaha YZF-R15 V 2.0':
            Bike_Model = 776
        elif bike_model == 'Yamaha FZ25':
            Bike_Model = 46
        elif bike_model == 'Bajaj Pulsar':
            Bike_Model = 4221
        elif bike_model == 'Bajaj Discover':
            Bike_Model = 397
        elif bike_model == 'Suzuki Gixxer':
            Bike_Model = 176
        elif bike_model == 'UM Renegade':
            Bike_Model = 128
        elif bike_model == 'Hero Super':
            Bike_Model = 655
        elif bike_model == 'Honda CBF Stunner':
            Bike_Model = 79
        elif bike_model == 'Bajaj Avenger':
            Bike_Model = 4857
        elif bike_model == 'KTM RC':
            Bike_Model = 839
        elif bike_model == 'Honda CB Unicorn':
            Bike_Model = 126
        elif bike_model == 'KTM Duke':
            Bike_Model = 261
        elif bike_model == 'Honda CBR 150R':
            Bike_Model = 75
        elif bike_model == 'Mahindra Centuro':
            Bike_Model = 32
        elif bike_model == 'Hero Hunk':
            Bike_Model = 660
        elif bike_model == 'Yamaha FZ':
            Bike_Model = 670
        elif bike_model == 'Honda CB Shine':
            Bike_Model = 192
        elif bike_model == 'Benelli TNT':
            Bike_Model = 50
        elif bike_model == 'Honda Dream':
            Bike_Model = 67
        elif bike_model == 'Hero CD':
            Bike_Model = 708
        elif bike_model == 'Kawasaki Ninja':
            Bike_Model = 48
        elif bike_model == 'Bajaj Platina':
            Bike_Model = 735
        elif bike_model == 'Hero Karizma':
            Bike_Model = 99
        elif bike_model == 'Harley-Davidson Street':
            Bike_Model = 724
        elif bike_model == 'Bajaj CT':
            Bike_Model = 107
        elif bike_model == 'Yamaha FZ16':
            Bike_Model = 53
        elif bike_model == 'Bajaj V15':
            Bike_Model = 161
        elif bike_model == 'Honda CBR 250R':
            Bike_Model = 73
        elif bike_model == 'Hyosung GT650R':
            Bike_Model = 12
        elif bike_model == 'Yamaha YZF-R15':
            Bike_Model = 148
        elif bike_model == 'Honda CB ShineSP':
            Bike_Model = 20
        elif bike_model == 'Hero Passion':
            Bike_Model = 2867
        elif bike_model == 'Bajaj Dominar':
            Bike_Model = 729
        elif bike_model == 'Yamaha Fazer':
            Bike_Model = 1291
        elif bike_model == 'Harley-Davidson Iron':
            Bike_Model = 29
        elif bike_model == 'Hero HF':
            Bike_Model = 137
        elif bike_model == 'TVS Sport':
            Bike_Model = 68
        elif bike_model == 'Honda Livo':
            Bike_Model = 42
        elif bike_model == 'Yamaha SZ-RR':
            Bike_Model = 613
        elif bike_model == 'Yamaha Saluto':
            Bike_Model = 11
        elif bike_model == 'Hyosung Aquila':
            Bike_Model = 19
        elif bike_model == 'Bajaj V12':
            Bike_Model = 21
        elif bike_model == 'Honda CB Twister':
            Bike_Model = 40
        elif bike_model == 'Harley-Davidson Fat':
            Bike_Model = 14
        elif bike_model == 'Suzuki Intruder':
            Bike_Model = 41
        elif bike_model == 'Mahindra Mojo':
            Bike_Model = 24
        elif bike_model == 'Hero Ignitor':
            Bike_Model = 39
        elif bike_model == 'Hero Glamour':
            Bike_Model = 56
        elif bike_model == 'Suzuki Slingshot':
            Bike_Model = 617
        elif bike_model == 'Honda CB Trigger':
            Bike_Model = 681
        elif bike_model == 'Hyosung GT250R':
            Bike_Model = 646
        elif bike_model == 'Hero Xtreme':
            Bike_Model = 35
        elif bike_model == 'Yamaha SZR':
            Bike_Model = 34
        elif bike_model == 'Hero CBZ 150cc':
            Bike_Model = 13
        elif bike_model == 'Yamaha FZS':
            Bike_Model = 15
        elif bike_model == 'Hero CBZ Xtreme':
            Bike_Model = 690
        elif bike_model == 'Hero Honda':
            Bike_Model = 25
        elif bike_model == 'TVS Apache V 2.0':
            Bike_Model = 22
        elif bike_model == 'TVS Victor':
            Bike_Model = 622
        elif bike_model == 'Honda CD':
            Bike_Model = 18
        elif bike_model == 'Bajaj ':
            Bike_Model = 26
        else:
            Bike_Model = 608
        
        #Cubic Capacity
        Cubic_Capacity=0
        cc = request.form["cubic_capacity"]
        if cc == '110':
            Cubic_Capacity = 110
        elif cc == '350':
            Cubic_Capacity = 350
        elif cc == '180':
            Cubic_Capacity = 180
        elif cc == '150':
            Cubic_Capacity = 150
        elif cc == '160':
            Cubic_Capacity = 160
        elif cc == '100':
            Cubic_Capacity = 100
        elif cc == '500':
            Cubic_Capacity = 500
        elif cc == '250':
            Cubic_Capacity = 250
        elif cc == '200':
            Cubic_Capacity = 200
        elif cc == '125':
            Cubic_Capacity = 125
        elif cc == '201':
            Cubic_Capacity = 201
        elif cc == '220':
            Cubic_Capacity = 220
        elif cc == '390':
            Cubic_Capacity = 390
        elif cc == '600':
            Cubic_Capacity = 600
        elif cc == '650':
            Cubic_Capacity = 650
        elif cc == '223':
            Cubic_Capacity = 223
        elif cc == '410':
            Cubic_Capacity = 410
        elif cc == '135':
            Cubic_Capacity = 135
        elif cc == '300':
            Cubic_Capacity = 300
        elif cc == '750':
            Cubic_Capacity = 750
        elif cc == '400':
            Cubic_Capacity = 400
        elif cc == '883':
            Cubic_Capacity = 883
        elif cc == '899':
            Cubic_Capacity = 899
        elif cc == '535':
            Cubic_Capacity = 535
        elif cc == '113':
            Cubic_Capacity = 113
        elif cc == '310':
            Cubic_Capacity = 310
        elif cc == '149':
            Cubic_Capacity = 149
        elif cc == '202':
            Cubic_Capacity = 202
        else:
            Cubic_Capacity = 107

        #Year
        
        Year=request.form['year']
        

        #Location
        Location=0
        place=request.form['location']
        if place == 'Gujarat':
        	Location= 1166
        elif place == 'Delhi':
            Location= 7345
        elif place == 'Karnataka':
            Location= 2781
        elif place == 'Maharashtra':
            Location= 4584
        elif place == 'Orissa':
            Location= 68
        elif place == 'Haryana':
            Location= 1921
        elif place == 'Uttar Pradesh':
            Location= 6713
        elif place == 'Kerala':
            Location= 654
        elif place == 'Bihar':
            Location= 71
        elif place == 'Rajasthan':
            Location= 2306
        elif place == 'Tamil Nadu':
            Location= 1692
        elif place == 'Other':
            Location= 2054
        elif place == 'Punjab':
            Location= 833
        elif place == 'Andhra Pradesh':
            Location= 58
        elif place == 'West Bengal':
            Location= 809
        elif place == 'Himachal Pradesh':
            Location= 16
        elif place == 'Madhya Pradesh':
            Location= 736
        elif place == 'Chhattisgarh':
            Location= 22
        elif place == 'Chandigarh ':
            Location= 47
        elif place == 'Jharkhand':
            Location= 30
        elif place == 'Uttaranchal':
            Location= 60
        elif place == 'Jammu & Kashmir':
            Location= 13
        elif place == 'Assam':
            Location= 46
        elif place == 'Sikkim':
            Location= 3
        elif place == 'Goa':
            Location= 6
        elif place == 'Pondicherry ':
            Location= 9
        elif place == 'Tripura':
            Location= 12
        elif place == 'Arunachal Pradesh':
            Location= 1
        else:
            Location= 2

        #Running
        
        Running=request.form.get('distance')
        
        
        #Owner
        Second_owner=0
        Third_owner=0
        Fourth_owner_or_more=0
        
        owner=request.form['owner']
        if owner=='Second owner':
            Second_owner=1
        elif owner=='Third owner':
            Third_owner=1
        elif owner=='Fourth Owner Or More':
            Fourth_owner_or_more=1

        
        input_variables = pd.DataFrame([[Cubic_Capacity,Year,Running,Second_owner,Third_owner,Fourth_owner_or_more,Bike_Model,Location]],
        columns=['Cubic_Capacity','Year','Running','Second_owner','Third_owner','Fourth_owner_or_more','Bike_Model','Location'],
        dtype=float)
        

        #prediction=model.predict([[Cubic_Capacity,year,running,Second_owner,Third_owner,Fourth_owner_or_more,Bike_Model,location]])
        prediction=model.predict(input_variables)
        output=round(prediction[0])

        return render_template('home.html',prediction_text="Your Bike price is Rs. {}".format(output))


    return render_template("home.html")
        
if __name__ == "__main__":
    app.run(debug=True)