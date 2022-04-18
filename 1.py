van_tor_price = 250
van_ott_price = 280
van_mon_price = 240
van_edm_price = 150
van_cal_price = 180

van_tor_travel_time = 3.5
van_ott_travel_time = 4
van_mon_travel_time = 4
van_edm_travel_time = 1.5
van_cal_travel_time = 1

ott_eur_price = 1350
mon_eur_price = 1300
edm_eur_price = 1290
cal_eur_price = 1400
tor_eur_price = 990

ott_layover = 3.5
mon_layover = 2
edm_layover = 5
cal_layover = 2.5
tor_layover = 1.5

ott_eur_travel_time = 9
mon_eur_travel_time = 8
edm_eur_travel_time = 10
cal_eur_travel_time = 10
tor_eur_travel_time = 9.5

## Using math operators in Python, find out which flight will give Dot the best value per hour of travel time.

## value = price_paid / travel_time

connectionLocations = ["tor", "ott", "mon", "edm", "cal"]
bestValueLocationVal = ""
bestValueLocationName = ""

for location in connectionLocations:
  value = (eval("van_"+ location + "_price") + eval(location + "_eur_price")) / (eval("van_" + location + "_travel_time") + eval(location + "_layover") + eval(location + "_eur_travel_time"))
  if bestValueLocationVal == "":
    bestValueLocationVal = value
    bestValueLocationName = location
  elif value < bestValueLocationVal:
    bestValueLocationVal = value
    bestValueLocationName = location

print(bestValueLocationName)    