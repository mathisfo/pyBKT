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
    df = pd.read_csv("data/extended_coding.csv")

    # Train a simple BKT model on one skill in the CT dataset
    # Note that calling fit deletes any previous trained BKT model!
    # model.fit(data_path = 'ct.csv', skills = "Plot imperfect radical")

    # model.fit(data_path = 'as.csv', forgets = True, skills = 'Box and Whisker')
    model.fit(data=df, forgets=False)

    preds_df = model.predict(data=df)

    # View the trained parameters!
    # print(model.params())

    # model.params().to_json("coding_ext_basic_F_False.json")

    training_auc = model.evaluate(data_path="data/extended_coding.csv", metric="auc")
    training_rmse = model.evaluate(
        data_path="data/extended_coding.csv.csv", metric="rmse"
    )

    print("Training AUC All: ", training_auc)
    print("Training RMSE All: ", training_rmse)

    # Save predictions to a CSV file


"""
    preds_df[preds_df["skill_name"] == "Strings"][
        ["user_id", "correct", "correct_predictions", "state_predictions"]
    ].to_csv("Strings_ext_multigs_forgets_False.csv", index=False)
    """


if __name__ == "__main__":
    main()
