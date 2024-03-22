from target_5 import inverter_string

def test_inverter_string():
    strings = ['target', 'dev', 'tecnologia', 'dragon ball z']
    
    for string in strings:
        assert inverter_string(string) == string[::-1]