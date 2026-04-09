def convert_minutes(total_minutes):
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours} hrs {minutes} minutes"

print(convert_minutes(130))
print(convert_minutes(110))