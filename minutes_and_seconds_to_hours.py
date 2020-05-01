def minutes_and_seconds_to_hours(minutes,seconds):
    hours=int(minutes)/60+int(seconds)/3600
    return hours

minutes=input("enter the value: ") 
seconds=input("enter the value: ") 
print(minutes_and_seconds_to_hours(minutes,seconds)+20)  