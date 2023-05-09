from pyBKT.models import Model
import pandas as pd
from typing import Union
import matplotlib.pyplot as plt
import numpy as np

"""
skills = [
    "Strings",
    "Variables and Operations",
    "If-Else",
    "Boolean Expressions",
]
"""
skills = ["allSkills"]


def main(multilearn=False, multigs=False, forgets=False, group=all, type="both"):
    # Initialize the model with an optional seed
    model = Model(seed=42, num_fits=1)

    # Fetch Assistments and CognitiveTutor data (optional - if you have your own dataset, that's fine too!)
    # model.fetch_dataset('https://raw.githubusercontent.com/CAHLR/pyBKT-examples/master/data/ct.csv', '.')
    # model.fetch_dataset('https://raw.githubusercontent.com/CAHLR/pyBKT-examples/master/data/as.csv', '.')

    # load data from csv

    def data_file():
        file = pd.read_csv("data/-1/everything.csv")

        if group == "all" and type == "both":
            print("I used the whole dataset")
            return file

        if group == "all" and type == "Challenges":
            print("I used the whole dataset, and type is Challenges")
            return file[file["type"] == "Challenges"]

        if group == "all" and type == "Coding":
            print("I used the whole dataset, and type is Coding")

            return file[file["type"] == "Coding"]

        if group == "OBJ2000" and type == "both":
            print("i used OBJ2000 and type is both ")
            return file[file["class"] == "OBJ2000"]

        if group == "OBJ2000" and type == "Challenges":
            print("i used OBJ2000 and type is Challenges ")
            return file[(file["class"] == "OBJ2000") & (file["type"] == "Challenges")]

        if group == "OBJ2000" and type == "Coding":
            print("i used OBJ2000 and type is Coding ")
            return file[(file["class"] == "OBJ2000") & (file["type"] == "Coding")]

        if group == "OBJ2100" and type == "both":
            print("I used OBJ2100 and type is both")
            return file[file["class"] == "OBJ2100"]

        if group == "OBJ2100" and type == "Challenges":
            print("I used OBJ2100 and type is Challenges")
            return file[(file["class"] == "OBJ2100") & (file["type"] == "Challenges")]

        if group == "OBJ2100" and type == "Coding":
            print("I used OBJ2100 and type is Coding")
            return file[(file["class"] == "OBJ2100") & (file["type"] == "Coding")]

    # Train a simple BKT model on one skill in the CT dataset
    # Note that calling fit deletes any previous trained BKT model!
    # model.fit(data_path = 'ct.csv', skills = "Plot imperfect radical")

    model.fit(
        data=data_file(),
        multilearn=multilearn,
        multigs=multigs,
        forgets=forgets,
    )

    preds_df = model.predict(
        data=data_file(),
    )

    model.params().to_csv(
        "Group_{}__type_{}__skills_{}__multigs_{}__multilearn_{}__forgets_{}_params.csv".format(
            group, type, skills, multigs, multilearn, forgets
        )
    )

    training_auc = model.evaluate(data=data_file(), metric="auc")
    training_rmse = model.evaluate(data=data_file(), metric="rmse")

    crossvalidated_ = model.crossvalidate(
        data=data_file(), multigs=multigs, forgets=forgets, multilearn=multilearn
    )

    print("--------------Training AUC & RMSE --------------")

    print(
        "Training AUC Group_{}__type_{}__multigs_{}__multilearn_{}__forgets_{}".format(
            group, type, multigs, multilearn, forgets
        ),
        training_auc,
    )
    print(
        "Training RMSE Group_{}__type_{}__multigs_{}__multilearn_{}__forgets_{}".format(
            group, type, multigs, multilearn, forgets
        ),
        training_rmse,
    )

    print(
        "Training CrossValidated Group_{}__type_{}__multigs_{}__multilearn_{}__forgets_{}".format(
            group, type, multigs, multilearn, forgets
        ),
        crossvalidated_,
    )
    print("-------------------------------------------------------")

    filtered_preds_df = preds_df[preds_df["correct_predictions"] != 0.5]

    filtered_preds_df[
        [
            "user_id",
            "correct",
            "correct_predictions",
            "state_predictions",
            "skill_name",
            "class",
            "type",
        ]
    ].to_csv(
        "Group_{}__type_{}__skills_{}__multigs_{}__multilearn_{}__forgets_{}.csv".format(
            group, type, skills, multigs, multilearn, forgets
        ),
        index=False,
    )
    print("--------------Predictions & Predictions --------------")
    print(
        "Printed Predictions",
        "Group_{}__type_{}__multigs_{}__multilearn_{}__forgets_{}.csv".format(
            group, type, multigs, multilearn, forgets
        ),
    )

    print(
        "Printed Params",
        "Group_{}__type_{}__skills_{}__multigs_{}__multilearn_{}__forgets_{}_params.csv".format(
            group, type, skills, multigs, multilearn, forgets
        ),
    )
    print("-------------------------------------------------------")


if __name__ == "__main__":
    main(
        forgets=False,
        group="OBJ2100",
        type="both",
        multigs="type",
        multilearn="type",
    )


# groupd: all, OBJ2000, OBJ2100
# type: both, Challenges, Coding
# multigs: class, type, activityId, user_id
# multilearn: class, type, activityId, user_id


# Forgets= True eller False. True -> Kan vi overparameterization
# multigs (KT-IDEM) = activityId -> guess og slipp per oppgave. Da trenger man ikke å skille på Challenge og coding.
# multilearn -> user_id, fordi da individualiserer vi per student
# type both
# group all

# multigs -> user_id. gs classes for hver student.
# multilearn -> user_id. learning rate classes for hver student.
# group -> !all
# type -> !both
