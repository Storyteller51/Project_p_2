def convert(value, from_unit, to_unit):
    
    to_meters = {
        "km": 1000,
        "m": 1,
        "cm": 0.01
    }
 
    if from_unit not in to_meters:
        print (f"Неподдерживаемая единица: {from_unit}")
    if to_unit not in to_meters:
        print (f"Неподдерживаемая единица: {to_unit}")

    meters_converted = value * to_meters[from_unit]
    result = meters_converted / to_meters[to_unit]
    return result

print(convert(100, "km", "m"))    
print(convert(41, "m", "cm"))   