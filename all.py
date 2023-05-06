from pyBKT.models import Model
import pandas as pd
import numpy as np
import csv


def main():
    # Initialize the model with an optional seed
    model = Model(seed=42, num_fits=1)

    # Fetch Assistments and CognitiveTutor data (optional - if you have your own dataset, that's fine too!)
    # model.fetch_dataset('https://raw.githubusercontent.com/CAHLR/pyBKT-examples/master/data/ct.csv', '.')
    # model.fetch_dataset('https://raw.githubusercontent.com/CAHLR/pyBKT-examples/master/data/as.csv', '.')

    # load data from csv
    df = pd.read_csv("data/-1/everything.csv")

    # Train a simple BKT model on one skill in the CT dataset
    # Note that calling fit deletes any previous trained BKT model!
    # model.fit(data_path = 'ct.csv', skills = "Plot imperfect radical")

    model.fit(
        data_path="data/-1/everything.csv",
        multigs="type",
        multilearn="class",
        forgets=True,
    )

    preds_df = model.predict(data=df)

    model.params().to_json("all_multigs_multilearn_forget_True_params.json")

    training_auc = model.evaluate(data_path="data/-1/everything.csv", metric="auc")
    training_rmse = model.evaluate(data_path="data/-1/everything.csv", metric="rmse")

    print("Training AUC all multigs multilearn forget true", training_auc)
    print("Training RMSE all multigs multilearn forget true", training_rmse)

    preds_df[
        [
            "user_id",
            "correct",
            "correct_predictions",
            "state_predictions",
            "skill_name",
            "class",
            "type",
        ]
    ].to_csv("all_multigs_multilearn_forget_true.csv", index=False)


if __name__ == "__main__":
    main()
