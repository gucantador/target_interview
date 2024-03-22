def inverter_string(string):
    invertido = ''
    for i in range(1, len(string) + 1):
        invertido += string[-i]
    print(invertido)
    return invertido

inverter_string('teste')