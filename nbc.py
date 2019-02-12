import json

testdata =\
'[\
{"Outlook":"Sunny","Temperature":"Hot","Humidity":"High","Wind":"Weak","PlayTennis":"No"},\
{"Outlook":"Sunny","Temperature":"Hot","Humidity":"High","Wind":"Strong","PlayTennis":"No"},\
{"Outlook":"Overcast","Temperature":"Hot","Humidity":"High","Wind":"Weak","PlayTennis":"Yes"},\
{"Outlook":"Rain","Temperature":"Mild","Humidity":"High","Wind":"Weak","PlayTennis":"Yes"},\
{"Outlook":"Rain","Temperature":"Cool","Humidity":"Normal","Wind":"Weak","PlayTennis":"Yes"},\
{"Outlook":"Rain","Temperature":"Cool","Humidity":"Normal","Wind":"Strong","PlayTennis":"No"},\
{"Outlook":"Overcast","Temperature":"Cool","Humidity":"Normal","Wind":"Strong","PlayTennis":"Yes"},\
{"Outlook":"Sunny","Temperature":"Mild","Humidity":"High","Wind":"Weak","PlayTennis":"No"},\
{"Outlook":"Sunny","Temperature":"Cool","Humidity":"Normal","Wind":"Weak","PlayTennis":"Yes"},\
{"Outlook":"Rain","Temperature":"Mild","Humidity":"Normal","Wind":"Weak","PlayTennis":"Yes"},\
{"Outlook":"Sunny","Temperature":"Mild","Humidity":"Normal","Wind":"Strong","PlayTennis":"Yes"},\
{"Outlook":"Overcast","Temperature":"Mild","Humidity":"High","Wind":"Strong","PlayTennis":"Yes"},\
{"Outlook":"Overcast","Temperature":"Hot","Humidity":"Normal","Wind":"Weak","PlayTennis":"Yes"},\
{"Outlook":"Rain","Temperature":"Mild","Humidity":"High","Wind":"Strong","PlayTennis":"No"}]'

data = json.loads(testdata);
pOfPT_yes = 0; # Count for P(PlayTennis) = Yes
pOfPT_no = 0; # Count for P(PlayTennis) = No
Outlook_attr = dict()
Temperature_attr = dict()
Humidity_attr = dict()
Wind_attr = dict()
attr_counter = 0

for i in range(len(data)):
    # Count of target Attribute values:
    if (data[i]['PlayTennis'] == "Yes"):
        pOfPT_yes = pOfPT_yes + 1
    if (data[i]['PlayTennis'] == "No"):
        pOfPT_no = pOfPT_no + 1

def countOutlook():
    ## Count of Outlook attr for Yes:

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Outlook']=="Sunny"):
            if(data[i]['PlayTennis'] == "Yes"):
                attr_counter = attr_counter + 1
    Outlook_attr['SunnyYes'] = attr_counter/pOfPT_yes

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Outlook']=="Overcast"):
            if(data[i]['PlayTennis'] == "Yes"):
                attr_counter = attr_counter + 1
    Outlook_attr['OvercastYes'] = attr_counter/pOfPT_yes

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Outlook']=="Rain"):
            if(data[i]['PlayTennis'] == "Yes"):
                attr_counter = attr_counter + 1
    Outlook_attr['RainYes'] = attr_counter/pOfPT_yes

    ## Count of Outlook attr for No:

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Outlook']=="Sunny"):
            if(data[i]['PlayTennis'] == "No"):
                attr_counter = attr_counter + 1
    Outlook_attr['SunnyNo'] = attr_counter/pOfPT_no

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Outlook']=="Overcast"):
            if(data[i]['PlayTennis'] == "No"):
                attr_counter = attr_counter + 1
    Outlook_attr['OvercastNo'] = attr_counter/pOfPT_no

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Outlook']=="Rain"):
            if(data[i]['PlayTennis'] == "No"):
                attr_counter = attr_counter + 1
    Outlook_attr['RainNo'] = attr_counter/pOfPT_no

def countTemperature():
    ## Count for Temperature attributes for Yes:

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Temperature']=="Hot"):
            if(data[i]['PlayTennis'] == "Yes"):
                attr_counter = attr_counter + 1
    Temperature_attr['HotYes'] = attr_counter/pOfPT_yes

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Temperature']=="Mild"):
            if(data[i]['PlayTennis'] == "Yes"):
                attr_counter = attr_counter + 1
    Temperature_attr['MildYes'] = attr_counter/pOfPT_yes

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Temperature']=="Cool"):
            if(data[i]['PlayTennis'] == "Yes"):
                attr_counter = attr_counter + 1
    Temperature_attr['CoolYes'] = attr_counter/pOfPT_yes

    ## Count of Outlook attr for No:

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Temperature']=="Hot"):
            if(data[i]['PlayTennis'] == "No"):
                attr_counter = attr_counter + 1
    Temperature_attr['HotNo'] = attr_counter/pOfPT_no

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Temperature']=="Mild"):
            if(data[i]['PlayTennis'] == "No"):
                attr_counter = attr_counter + 1
    Temperature_attr['MildNo'] = attr_counter/pOfPT_no

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Temperature']=="Cool"):
            if(data[i]['PlayTennis'] == "No"):
                attr_counter = attr_counter + 1
    Temperature_attr['CoolNo'] = attr_counter/pOfPT_no

def countHumidity():
    ## Count for Yes in Humidity:

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Humidity']=="High"):
            if(data[i]['PlayTennis'] == "Yes"):
                attr_counter = attr_counter + 1
    Humidity_attr['HighYes'] = attr_counter/pOfPT_yes

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Humidity']=="Normal"):
            if(data[i]['PlayTennis'] == "Yes"):
                attr_counter = attr_counter + 1
    Humidity_attr['NormalYes'] = attr_counter/pOfPT_yes

    ## Count for No in Humidity:

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Humidity']=="High"):
            if(data[i]['PlayTennis'] == "No"):
                attr_counter = attr_counter + 1
    Humidity_attr['HighNo'] = attr_counter/pOfPT_no

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Humidity']=="Normal"):
            if(data[i]['PlayTennis'] == "No"):
                attr_counter = attr_counter + 1
    Humidity_attr['NormalNo'] = attr_counter/pOfPT_no

def countWind():
    ## Count for Yes in Wind:

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Wind']=="Strong"):
            if(data[i]['PlayTennis'] == "Yes"):
                attr_counter = attr_counter + 1
    Wind_attr['StrongYes'] = attr_counter/pOfPT_yes

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Wind']=="Weak"):
            if(data[i]['PlayTennis'] == "Yes"):
                attr_counter = attr_counter + 1
    Wind_attr['WeakYes'] = attr_counter/pOfPT_yes

    ## Count for No in Wind:

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Wind']=="Strong"):
            if(data[i]['PlayTennis'] == "No"):
                attr_counter = attr_counter + 1
    Wind_attr['StrongNo'] = attr_counter/pOfPT_no

    attr_counter = 0
    for i in range(len(data)):
        if(data[i]['Wind']=="Weak"):
            if(data[i]['PlayTennis'] == "No"):
                attr_counter = attr_counter + 1
    Wind_attr['WeakNo'] = attr_counter/pOfPT_no


countOutlook()
countTemperature()
countHumidity()
countWind()

#print("Outlook: {}\nTemperature: {}\nHumidity: {}\nWind: {}".format(Outlook_attr,Temperature_attr,Humidity_attr,Wind_attr))

print("====================================================================")

choice = "Y"
while(choice == "Y" or choice == "y"):
    new_outlook = input("Enter Outlook value: ")
    new_temperature = input("Enter Temperature value: ")
    new_humidity = input("Enter Humidity value: ")
    new_wind = input("Enter Wind value: ")

    finalYesVal = Outlook_attr[new_outlook+'Yes']*Temperature_attr[new_temperature+'Yes']*\
                  Humidity_attr[new_humidity+'Yes']*Wind_attr[new_wind+'Yes']*(pOfPT_yes/len(data))
    finalNoVal = Outlook_attr[new_outlook+'No']*Temperature_attr[new_temperature+'No']*\
                 Humidity_attr[new_humidity+'No']*Wind_attr[new_wind+'No']*(pOfPT_no/len(data))

    if (finalYesVal<finalNoVal):
        data.append({"Outlook":new_outlook,"Temperature":new_temperature,"Humidity":new_humidity,"Wind":new_wind,"PlayTennis":"No"})
    else:
        data.append({"Outlook":new_outlook,"Temperature":new_temperature,"Humidity":new_humidity,"Wind":new_wind,"PlayTennis":"Yes"})

    print(data[len(data)-1])

    choice=input("Do you want to continue entering input?: ")
    if(choice == "N" or choice == "n"):
        break;
