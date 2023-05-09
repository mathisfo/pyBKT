import json
import csv

# JSON data as provided
json_data = """{
  "value": {
    "('Variables and Operations', 'prior', 'default')": 0.5623267431,
    "('Variables and Operations', 'learns', 'OBJ2000')": 0.1085140374,
    "('Variables and Operations', 'learns', 'OBJ2100')": 0.1592094543,
    "('Variables and Operations', 'guesses', 'OBJ2000')": 0.0157571638,
    "('Variables and Operations', 'guesses', 'OBJ2100')": 0.02437141,
    "('Variables and Operations', 'slips', 'OBJ2000')": 0.4771202024,
    "('Variables and Operations', 'slips', 'OBJ2100')": 0.4211608787,
    "('Variables and Operations', 'forgets', 'OBJ2000')": 0.2044752679,
    "('Variables and Operations', 'forgets', 'OBJ2100')": 0.1744176715,
    "('Strings', 'prior', 'default')": 0.7220707326,
    "('Strings', 'learns', 'OBJ2000')": 0.0267281821,
    "('Strings', 'learns', 'OBJ2100')": 0.0511557305,
    "('Strings', 'guesses', 'OBJ2000')": 0.0566079089,
    "('Strings', 'guesses', 'OBJ2100')": 0.0951446238,
    "('Strings', 'slips', 'OBJ2000')": 0.6037587214,
    "('Strings', 'slips', 'OBJ2100')": 0.4963397382,
    "('Strings', 'forgets', 'OBJ2000')": 0.0922062092,
    "('Strings', 'forgets', 'OBJ2100')": 0.0718698049,
    "('Arrays', 'prior', 'default')": 0.265877806,
    "('Arrays', 'learns', 'OBJ2000')": 0.0021200728,
    "('Arrays', 'learns', 'OBJ2100')": 0.0041744772,
    "('Arrays', 'guesses', 'OBJ2000')": 0.2420966511,
    "('Arrays', 'guesses', 'OBJ2100')": 0.219497865,
    "('Arrays', 'slips', 'OBJ2000')": 0.5079444605,
    "('Arrays', 'slips', 'OBJ2100')": 0.3121683278,
    "('Arrays', 'forgets', 'OBJ2000')": 0.1387131176,
    "('Arrays', 'forgets', 'OBJ2100')": 0.0588004,
    "('If-Else', 'prior', 'default')": 0.8621840881,
    "('If-Else', 'learns', 'OBJ2000')": 0.0243005405,
    "('If-Else', 'learns', 'OBJ2100')": 0.0512405609,
    "('If-Else', 'guesses', 'OBJ2000')": 0.0357735359,
    "('If-Else', 'guesses', 'OBJ2100')": 0.0581680689,
    "('If-Else', 'slips', 'OBJ2000')": 0.3246576094,
    "('If-Else', 'slips', 'OBJ2100')": 0.4230023698,
    "('If-Else', 'forgets', 'OBJ2000')": 0.1280477687,
    "('If-Else', 'forgets', 'OBJ2100')": 0.1212599026,
    "('While Loops', 'prior', 'default')": 0.5892445854,
    "('While Loops', 'learns', 'OBJ2000')": 0.1285506379,
    "('While Loops', 'learns', 'OBJ2100')": 0.1835594872,
    "('While Loops', 'guesses', 'OBJ2000')": 0.005984165,
    "('While Loops', 'guesses', 'OBJ2100')": 0.0107759365,
    "('While Loops', 'slips', 'OBJ2000')": 0.3478856519,
    "('While Loops', 'slips', 'OBJ2100')": 0.3247089986,
    "('While Loops', 'forgets', 'OBJ2000')": 0.3062807771,
    "('While Loops', 'forgets', 'OBJ2100')": 0.3296926224,
    "('ArrayLists', 'prior', 'default')": 0.8364693447,
    "('ArrayLists', 'learns', 'OBJ2000')": 0.1359320829,
    "('ArrayLists', 'learns', 'OBJ2100')": 0.1386840945,
    "('ArrayLists', 'guesses', 'OBJ2000')": 0.3700243589,
    "('ArrayLists', 'guesses', 'OBJ2100')": 0.2708133008,
    "('ArrayLists', 'slips', 'OBJ2000')": 0.7689019351,
    "('ArrayLists', 'slips', 'OBJ2100')": 0.7753681494,
    "('ArrayLists', 'forgets', 'OBJ2000')": 0.6388814519,
    "('ArrayLists', 'forgets', 'OBJ2100')": 0.6270296656,
    "('Inheritance', 'prior', 'default')": 0.325,
    "('Inheritance', 'learns', 'OBJ2000')": 0.0833333333,
    "('Inheritance', 'learns', 'OBJ2100')": 0.173390481,
    "('Inheritance', 'guesses', 'OBJ2000')": 8.856696664e-106,
    "('Inheritance', 'guesses', 'OBJ2100')": 7.897160753e-79,
    "('Inheritance', 'slips', 'OBJ2000')": 0.0,
    "('Inheritance', 'slips', 'OBJ2100')": 0.2293256994,
    "('Inheritance', 'forgets', 'OBJ2000')": 2.247834425e-27,
    "('Inheritance', 'forgets', 'OBJ2100')": 0.0985510668,
    "('Objects and Classes', 'prior', 'default')": 0.3003570403,
    "('Objects and Classes', 'learns', 'OBJ2000')": 0.1235308031,
    "('Objects and Classes', 'learns', 'OBJ2100')": 0.1020042861,
    "('Objects and Classes', 'guesses', 'OBJ2000')": 0.0716077033,
    "('Objects and Classes', 'guesses', 'OBJ2100')": 0.0621250646,
    "('Objects and Classes', 'slips', 'OBJ2000')": 0.1311516429,
    "('Objects and Classes', 'slips', 'OBJ2100')": 0.1831572688,
    "('Objects and Classes', 'forgets', 'OBJ2000')": 0.3999999296,
    "('Objects and Classes', 'forgets', 'OBJ2100')": 0.4179434541,
    "('Two-Dimensional Arrays', 'prior', 'default')": 0.2521443789,
    "('Two-Dimensional Arrays', 'learns', 'OBJ2000')": 0.055446285,
    "('Two-Dimensional Arrays', 'learns', 'OBJ2100')": 0.0766534214,
    "('Two-Dimensional Arrays', 'guesses', 'OBJ2000')": 0.1352257142,
    "('Two-Dimensional Arrays', 'guesses', 'OBJ2100')": 0.1254890636,
    "('Two-Dimensional Arrays', 'slips', 'OBJ2000')": 0.0897060541,
    "('Two-Dimensional Arrays', 'slips', 'OBJ2100')": 0.1269051663,
    "('Two-Dimensional Arrays', 'forgets', 'OBJ2000')": 0.3599371286,
    "('Two-Dimensional Arrays', 'forgets', 'OBJ2100')": 0.3364997486,
    "('Nested Loops', 'prior', 'default')": 0.7430217402,
    "('Nested Loops', 'learns', 'OBJ2000')": 0.0513275119,
    "('Nested Loops', 'learns', 'OBJ2100')": 0.0391996481,
    "('Nested Loops', 'guesses', 'OBJ2000')": 0.0332960509,
    "('Nested Loops', 'guesses', 'OBJ2100')": 0.0233421131,
    "('Nested Loops', 'slips', 'OBJ2000')": 0.5048277641,
    "('Nested Loops', 'slips', 'OBJ2100')": 0.5201577,
    "('Nested Loops', 'forgets', 'OBJ2000')": 0.1111834136,
    "('Nested Loops', 'forgets', 'OBJ2100')": 0.139727377,
    "('For Loops', 'prior', 'default')": 0.8056334965,
    "('For Loops', 'learns', 'OBJ2000')": 0.2746904228,
    "('For Loops', 'learns', 'OBJ2100')": 0.2739802501,
    "('For Loops', 'guesses', 'OBJ2000')": 0.3664481486,
    "('For Loops', 'guesses', 'OBJ2100')": 0.3716270453,
    "('For Loops', 'slips', 'OBJ2000')": 0.6976901882,
    "('For Loops', 'slips', 'OBJ2100')": 0.558506846,
    "('For Loops', 'forgets', 'OBJ2000')": 0.3831367817,
    "('For Loops', 'forgets', 'OBJ2100')": 0.3833389772,
    "('Boolean Expressions', 'prior', 'default')": 0.6480616724,
    "('Boolean Expressions', 'learns', 'OBJ2000')": 0.0493937843,
    "('Boolean Expressions', 'learns', 'OBJ2100')": 0.0302890272,
    "('Boolean Expressions', 'guesses', 'OBJ2000')": 0.1418376617,
    "('Boolean Expressions', 'guesses', 'OBJ2100')": 0.1092014375,
    "('Boolean Expressions', 'slips', 'OBJ2000')": 0.3205122213,
    "('Boolean Expressions', 'slips', 'OBJ2100')": 0.3487407728,
    "('Boolean Expressions', 'forgets', 'OBJ2000')": 0.0966162085,
    "('Boolean Expressions', 'forgets', 'OBJ2100')": 0.1254932089,
    "('Exception handling', 'prior', 'default')": 0.1420370728,
    "('Exception handling', 'learns', 'OBJ2000')": 0.2761586857,
    "('Exception handling', 'learns', 'OBJ2100')": 0.2761586857,
    "('Exception handling', 'guesses', 'OBJ2000')": 0.0,
    "('Exception handling', 'guesses', 'OBJ2100')": 0.1711883123,
    "('Exception handling', 'slips', 'OBJ2000')": 1.0,
    "('Exception handling', 'slips', 'OBJ2100')": 0.8925203678,
    "('Exception handling', 'forgets', 'OBJ2000')": 0.5540800333,
    "('Exception handling', 'forgets', 'OBJ2100')": 0.5540800333,
    "('File processing', 'prior', 'default')": 0.202437936,
    "('File processing', 'learns', 'OBJ2000')": 0.1080733157,
    "('File processing', 'learns', 'OBJ2100')": 0.1080733157,
    "('File processing', 'guesses', 'OBJ2000')": 0.0,
    "('File processing', 'guesses', 'OBJ2100')": 0.3054682954,
    "('File processing', 'slips', 'OBJ2000')": 1.0,
    "('File processing', 'slips', 'OBJ2100')": 0.7295171434,
    "('File processing', 'forgets', 'OBJ2000')": 0.8815885713,
    "('File processing', 'forgets', 'OBJ2100')": 0.8815885713
  }
}
"""


# Load JSON data
data = json.loads(json_data)

# Extract and process the values
values = []
for key, value in data["value"].items():
    skill, attribute, class_name = eval(key)
    values.append((class_name, skill, attribute, value))

# Sort values by class, skill and attribute
sorted_values = sorted(values, key=lambda x: (x[0], x[1], x[2]))

# Write values to CSV
header_names = ["class", "skill_name", "prior", "learns", "slips", "guesses", "forgets"]

with open("output.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(header_names)

    current_class = None
    current_skill = None
    row = []

    for class_name, skill, attribute, value in sorted_values:
        if class_name != current_class or skill != current_skill:
            if row:
                csv_writer.writerow(row)
            row = [class_name, skill, 0, 0, 0, 0, 0]
            current_class = class_name
            current_skill = skill

        if attribute == "prior":
            row[2] = value
        elif attribute == "learns":
            row[3] = value
        elif attribute == "slips":
            row[4] = value
        elif attribute == "guesses":
            row[5] = value
        elif attribute == "forgets":
            row[6] = value

    csv_writer.writerow(row)
