import json
import csv
from collections import defaultdict
import re


def json_to_csv(json_data):
    data = defaultdict(
        lambda: {
            class: "",
            "skill_name": "",
            "prior": 0,
            "learns": 0,
            "guesses": 0,
            "slips": 0,
            "forgets": 0,
        }
    )

    pattern = re.compile(r"\('(.*?)', '(.*?)', .*")

    for key, value in json_data["value"].items():
        match = pattern.match(key)
        if match:
            skill_name, param = match.groups()
            data[skill_name]["skill_name"] = skill_name
            data[skill_name][param.lower()] = value

    headers = ["class","skill_name", "prior", "learns", "guesses", "slips", "forgets"]

    with open("output.csv", "w", newline="") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=headers)
        csv_writer.writeheader()
        for row in data.values():
            csv_writer.writerow(row)


json_data = {
    "value": {
        "('Variables and Operations', 'prior', 'default')": 0.1851058974,
        "('Variables and Operations', 'learns', 'OBJ2000')": 0.0018086041,
        "('Variables and Operations', 'learns', 'OBJ2100')": 0.2097637244,
        "('Variables and Operations', 'guesses', 'OBJ2000')": 0.1159849847,
        "('Variables and Operations', 'guesses', 'OBJ2100')": 0.089270699,
        "('Variables and Operations', 'slips', 'OBJ2000')": 0.3224131161,
        "('Variables and Operations', 'slips', 'OBJ2100')": 0.4514262764,
        "('Variables and Operations', 'forgets', 'OBJ2000')": 0.0020338409,
        "('Variables and Operations', 'forgets', 'OBJ2100')": 0.8533353431,
        "('Strings', 'prior', 'default')": 0.1998716105,
        "('Strings', 'learns', 'OBJ2000')": 0.2557306388,
        "('Strings', 'learns', 'OBJ2100')": 0.211380421,
        "('Strings', 'guesses', 'OBJ2000')": 0.0539690854,
        "('Strings', 'guesses', 'OBJ2100')": 0.0938384204,
        "('Strings', 'slips', 'OBJ2000')": 0.4399639284,
        "('Strings', 'slips', 'OBJ2100')": 0.1114255322,
        "('Strings', 'forgets', 'OBJ2000')": 0.0011525729,
        "('Strings', 'forgets', 'OBJ2100')": 0.7094283771,
        "('If-Else', 'prior', 'default')": 0.718195398,
        "('If-Else', 'learns', 'OBJ2000')": 0.1334024849,
        "('If-Else', 'learns', 'OBJ2100')": 0.1837384602,
        "('If-Else', 'guesses', 'OBJ2000')": 0.0000004255,
        "('If-Else', 'guesses', 'OBJ2100')": 0.2784760897,
        "('If-Else', 'slips', 'OBJ2000')": 0.3005086576,
        "('If-Else', 'slips', 'OBJ2100')": 0.3361074162,
        "('If-Else', 'forgets', 'OBJ2000')": 0.004486542,
        "('If-Else', 'forgets', 'OBJ2100')": 0.8743485527,
        "('Arrays', 'prior', 'default')": 0.5702515128,
        "('Arrays', 'learns', 'OBJ2000')": 1.624005496e-19,
        "('Arrays', 'learns', 'OBJ2100')": 0.0005152469,
        "('Arrays', 'guesses', 'OBJ2000')": 0.0,
        "('Arrays', 'guesses', 'OBJ2100')": 0.0512516255,
        "('Arrays', 'slips', 'OBJ2000')": 5.874491892e-16,
        "('Arrays', 'slips', 'OBJ2100')": 0.2773415623,
        "('Arrays', 'forgets', 'OBJ2000')": 0.5,
        "('Arrays', 'forgets', 'OBJ2100')": 0.0852682877,
        "('While Loops', 'prior', 'default')": 0.9202246489,
        "('While Loops', 'learns', 'OBJ2000')": 0.51972368,
        "('While Loops', 'learns', 'OBJ2100')": 0.0302463588,
        "('While Loops', 'guesses', 'OBJ2000')": 0.1857212054,
        "('While Loops', 'guesses', 'OBJ2100')": 0.2392657313,
        "('While Loops', 'slips', 'OBJ2000')": 0.173673089,
        "('While Loops', 'slips', 'OBJ2100')": 0.8749388996,
        "('While Loops', 'forgets', 'OBJ2000')": 0.4620951369,
        "('While Loops', 'forgets', 'OBJ2100')": 0.9664972332,
        "('Boolean Expressions', 'prior', 'default')": 0.5675605863,
        "('Boolean Expressions', 'learns', 'OBJ2000')": 0.8469561152,
        "('Boolean Expressions', 'learns', 'OBJ2100')": 0.022672052,
        "('Boolean Expressions', 'guesses', 'OBJ2000')": 0.0137743367,
        "('Boolean Expressions', 'guesses', 'OBJ2100')": 0.2371445432,
        "('Boolean Expressions', 'slips', 'OBJ2000')": 0.0031467055,
        "('Boolean Expressions', 'slips', 'OBJ2100')": 0.3455266605,
        "('Boolean Expressions', 'forgets', 'OBJ2000')": 0.3032697725,
        "('Boolean Expressions', 'forgets', 'OBJ2100')": 0.087020054,
        "('Objects and Classes', 'prior', 'default')": 8.573796591e-21,
        "('Objects and Classes', 'learns', 'OBJ2000')": 0.2,
        "('Objects and Classes', 'learns', 'OBJ2100')": 0.6538586819,
        "('Objects and Classes', 'learns', 'OBj2100')": 2.490091932e-30,
        "('Objects and Classes', 'guesses', 'OBJ2000')": 1.368397626e-26,
        "('Objects and Classes', 'guesses', 'OBJ2100')": 9.229266794e-23,
        "('Objects and Classes', 'guesses', 'OBj2100')": 0.3333333333,
        "('Objects and Classes', 'slips', 'OBJ2000')": 5.926792583e-23,
        "('Objects and Classes', 'slips', 'OBJ2100')": 0.6233437832,
        "('Objects and Classes', 'slips', 'OBj2100')": 1.36407015e-213,
        "('Objects and Classes', 'forgets', 'OBJ2000')": 8.329063372e-20,
        "('Objects and Classes', 'forgets', 'OBJ2100')": 0.9999999059,
        "('Objects and Classes', 'forgets', 'OBj2100')": 1.0,
        "('For Loops', 'prior', 'default')": 0.7893854526,
        "('For Loops', 'learns', 'OBJ2000')": 0.5393242445,
        "('For Loops', 'learns', 'OBJ2100')": 0.1123658011,
        "('For Loops', 'guesses', 'OBJ2000')": 0.7387737657,
        "('For Loops', 'guesses', 'OBJ2100')": 0.2841667457,
        "('For Loops', 'slips', 'OBJ2000')": 0.9999736552,
        "('For Loops', 'slips', 'OBJ2100')": 0.0032486029,
        "('For Loops', 'forgets', 'OBJ2000')": 0.999265849,
        "('For Loops', 'forgets', 'OBJ2100')": 0.6238035406,
        "('Nested Loops', 'prior', 'default')": 0.4600662886,
        "('Nested Loops', 'learns', 'OBJ2000')": 0.0002580427,
        "('Nested Loops', 'learns', 'OBJ2100')": 0.0707621659,
        "('Nested Loops', 'guesses', 'OBJ2000')": 0.0010147649,
        "('Nested Loops', 'guesses', 'OBJ2100')": 0.061315102,
        "('Nested Loops', 'slips', 'OBJ2000')": 0.0020748377,
        "('Nested Loops', 'slips', 'OBJ2100')": 0.1574624241,
        "('Nested Loops', 'forgets', 'OBJ2000')": 0.7964671201,
        "('Nested Loops', 'forgets', 'OBJ2100')": 0.5465825588,
        "('Inheritance', 'prior', 'default')": 0.8276611562,
        "('Inheritance', 'learns', 'OBJ2000')": 0.2868841188,
        "('Inheritance', 'learns', 'OBJ2100')": 0.0481860351,
        "('Inheritance', 'guesses', 'OBJ2000')": 0.0,
        "('Inheritance', 'guesses', 'OBJ2100')": 0.6792648392,
        "('Inheritance', 'slips', 'OBJ2000')": 1.0,
        "('Inheritance', 'slips', 'OBJ2100')": 0.999627684,
        "('Inheritance', 'forgets', 'OBJ2000')": 0.7951828843,
        "('Inheritance', 'forgets', 'OBJ2100')": 0.1716569266,
        "('ArrayLists', 'prior', 'default')": 0.2631127523,
        "('ArrayLists', 'learns', 'OBJ2000')": 0.0684830863,
        "('ArrayLists', 'learns', 'OBJ2100')": 0.3217074596,
        "('ArrayLists', 'guesses', 'OBJ2000')": 0.0,
        "('ArrayLists', 'guesses', 'OBJ2100')": 0.0025802109,
        "('ArrayLists', 'slips', 'OBJ2000')": 1.0,
        "('ArrayLists', 'slips', 'OBJ2100')": 0.5310529317,
        "('ArrayLists', 'forgets', 'OBJ2000')": 0.2472654648,
        "('ArrayLists', 'forgets', 'OBJ2100')": 0.1992160403,
        "('Two-Dimensional Arrays', 'prior', 'default')": 0.997988753,
        "('Two-Dimensional Arrays', 'learns', 'OBJ2000')": 2.03823551e-18,
        "('Two-Dimensional Arrays', 'learns', 'OBJ2100')": 0.0002609208,
        "('Two-Dimensional Arrays', 'guesses', 'OBJ2000')": 0.0000221619,
        "('Two-Dimensional Arrays', 'guesses', 'OBJ2100')": 0.0561522009,
        "('Two-Dimensional Arrays', 'slips', 'OBJ2000')": 2.885226032e-34,
        "('Two-Dimensional Arrays', 'slips', 'OBJ2100')": 0.5376635292,
        "('Two-Dimensional Arrays', 'forgets', 'OBJ2000')": 0.5000220786,
        "('Two-Dimensional Arrays', 'forgets', 'OBJ2100')": 0.3747845966,
        "('Exception handling', 'prior', 'default')": 0.3222135126,
        "('Exception handling', 'learns', 'OBJ2000')": 0.1720072454,
        "('Exception handling', 'learns', 'OBJ2100')": 0.00153177,
        "('Exception handling', 'guesses', 'OBJ2000')": 0.0,
        "('Exception handling', 'guesses', 'OBJ2100')": 0.0000699065,
        "('Exception handling', 'slips', 'OBJ2000')": 1.0,
        "('Exception handling', 'slips', 'OBJ2100')": 0.1544383624,
        "('Exception handling', 'forgets', 'OBJ2000')": 0.2118840032,
        "('Exception handling', 'forgets', 'OBJ2100')": 0.9999601248,
        "('File processing', 'prior', 'default')": 0.0577433283,
        "('File processing', 'learns', 'OBJ2000')": 0.1801860979,
        "('File processing', 'learns', 'OBJ2100')": 0.2525616885,
        "('File processing', 'guesses', 'OBJ2000')": 0.0,
        "('File processing', 'guesses', 'OBJ2100')": 0.16550972,
        "('File processing', 'slips', 'OBJ2000')": 1.0,
        "('File processing', 'slips', 'OBJ2100')": 0.0633788992,
        "('File processing', 'forgets', 'OBJ2000')": 0.0736609154,
        "('File processing', 'forgets', 'OBJ2100')": 0.1644990729,
    }
}


json_to_csv(json_data)
