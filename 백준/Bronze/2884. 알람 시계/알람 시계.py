hour,min = map(int,input().split())
total_min = hour*60+min
new_totalmin=total_min-45
if(new_totalmin<0):
    new_totalmin+=24*60
hour = new_totalmin//60
min = new_totalmin%60
print(hour,min)