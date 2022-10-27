import urllib.parse
import requests
import time
import pytz
from tabulate import tabulate

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "cnZVv6MwNs22d1Qx1W3F8R3BpEPiWKJl"

while True:
    print("\033[1;30;47m============================================================ \n")
    orig = input("Starting Location:")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination:")
    if dest == "quit" or dest == "q":
        break
    print("============================================================ \n")
    data = [[orig, dest]]
    print(tabulate(data, headers=["\033[1;36;47m Origin", "\033[1;36;47m Stop"]))
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()

    print("URL:" + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        time_duration = (json_data["route"]["formattedTime"])
        current_time = (time.strftime("%H:%M:%S"))
        ETA = ((json_data["route"]["formattedTime"])) + (time.strftime("%H:%M:%S"))
        print("API Status: " + str(json_status) + "= A successful route call.\n")
        print("\033[1;30;47m============================================================ \n")
        print("Directions from  " + (orig) + " to " + (dest))
        print("Start Time:      ", current_time)
        print("ETA:             ", ETA)
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print()
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Miles:           " + str("{:.2f}".format((json_data["route"]["distance"]))))
        print("============================================================ \n")

        print("One Way Trip Route")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("============================================================ \n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("============================================================ \n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

    orig2 = dest
    print("\033[1;30;47Starting Location", dest)
    if orig2 == "quit" or orig2 == "q":
        break
    dest2 = orig
    print("Destination:", orig)
    if dest2 == "quit" or dest2 == "q":
        break
    print("============================================================ \n")
    data2 = [[orig2, dest2]]
    print(tabulate(data2, headers=["\033[1;36;47 Origin", "\033[1;36;47 Stop"]))
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig2, "to":dest2})
    json_data = requests.get(url).json()

    print("URL:" + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        time_duration = (json_data["route"]["formattedTime"])
        current_time = (time.strftime("%H:%M:%S"))
        ETA = ((json_data["route"]["formattedTime"])) + (time.strftime("%H:%M:%S"))
        print("API Status: " + str(json_status) + "= A successful route call.\n")
        print("\033[1;32;47m============================================================ \n")
        print("Directions from  " + (orig2) + " to " + (dest2))
        print("Start Time:      ", current_time)
        print("ETA:             ", ETA)
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print()
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Miles:           " + str("{:.2f}".format((json_data["route"]["distance"]))))
        print("============================================================ \n")

        print("Two Way Trip Route")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("============================================================ \n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")


