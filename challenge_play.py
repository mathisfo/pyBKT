from pyBKT.models import Model
import pandas as pd
import numpy as np
import csv

forgets = True


def main():
    # Initialize the model with an optional seed
    model = Model(seed=42, num_fits=1)

    # Fetch Assistments and CognitiveTutor data (optional - if you have your own dataset, that's fine too!)
    # model.fetch_dataset('https://raw.githubusercontent.com/CAHLR/pyBKT-examples/master/data/ct.csv', '.')
    # model.fetch_dataset('https://raw.githubusercontent.com/CAHLR/pyBKT-examples/master/data/as.csv', '.')

    # load data from csv
    df = pd.read_csv("data/-1/challenges.csv")

    # Train a simple BKT model on one skill in the CT dataset
    # Note that calling fit deletes any previous trained BKT model!
    # model.fit(data_path = 'ct.csv', skills = "Plot imperfect radical")

    model.fit(
        data_path="data/-1/challenges.csv",
        multigs="class",
        multilearn="class",
        forgets=False,
    )

    preds_df = model.predict(data=df)

    model.params().to_json("challenge_multigs_multilearn_forget_False_params.json")

    training_auc = model.evaluate(data_path="data/-1/challenges.csv", metric="auc")
    training_rmse = model.evaluate(data_path="data/-1/challenges.csv", metric="rmse")

    print("Training AUC", training_auc)
    print("Training RMSE ", training_rmse)

    preds_df[
        [
            "user_id",
            "correct",
            "correct_predictions",
            "state_predictions",
            "skill_name",
            "class",
        ]
    ].to_csv("challenge_multigs_multilearn_forget_False.csv", index=False)


if __name__ == "__main__":
    main()
