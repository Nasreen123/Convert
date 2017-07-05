import sys
import convert.convert


conversion_dictionary = {
"ft": { "in": 12, "cm": 30.48 },
"yd": { "ft": 3, "in": 36, "cm": 91.44, "m": 0.9144},
"m": { "yd": 1760, "m": 1609.344, "km": 1.609344},
"mm": { "in": 0.03937},
"cm": { "in": 0.39370},
"m": { "in": 39.37008, "ft": 3.28084, "yd": 1093.6133},
"km": { "yd": 1093.6133, "m": 0.62 }
}


def convert_help():
    help_string = "You can convert to and from the following units: \n"
    for key in conversion_dictionary.keys():
        valkeys = conversion_dictionary[key].keys()
        valkeysstring = " ".join(valkeys)
        help_string = help_string + key + " : " + valkeysstring + "\n"
    help_string += "Your query should take the following format:\n"
    help_string += "convert <amount> <unit> <target-unit>"
    return help_string


def convert_value(input_args):
    amount = input_args[1]
    unit = input_args[2]
    target_unit = input_args[3]

    conversions = conversion_dictionary[unit]
    conversion = conversions[target_unit]

    output = float(amount) * conversion

    return output


def run(input_args):
    if input_args[1] == "help":
        return convert_help()
    else:
        return convert_value(input_args)


input_args = sys.argv
print (run(input_args))
