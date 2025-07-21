test_cal= {}

months= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']

for month in months:
    test_cal[month]= []

for month, days in test_cal.items(): 
    if month in ('April', 'June' , 'September' , 'November') :
        for i in range (30):
            days.append(False)
    else:
        for i in range (31):
            days.append(False)

