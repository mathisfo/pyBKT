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
    df = pd.read_csv("data/-1/challenges_OBJ2100.csv")

    # Train a simple BKT model on one skill in the CT dataset
    # Note that calling fit deletes any previous trained BKT model!
    # model.fit(data_path = 'ct.csv', skills = "Plot imperfect radical")

    # model.fit(data_path = 'as.csv', forgets = True, skills = 'Box and Whisker')
    model.fit(data=df, forgets=True)

    preds_df = model.predict(data=df)
    model.params().to_json("Challenges_OBJ2100_forgets_True.json")

    training_auc = model.evaluate(
        data_path="data/-1/challenges_OBJ2100.csv", metric="auc"
    )
    training_rmse = model.evaluate(
        data_path="data/-1/challenges_OBJ2100.csv", metric="rmse"
    )

    print("Training AUC OBJ2100 Challenge: ", training_auc)
    print("Training RMSE OBJ2100 Challenge: ", training_rmse)



    preds_df[
        ["user_id", "correct", "correct_predictions", "state_predictions", "skill_name"]
    ].to_csv("Challenges_OBJ2100_forgets_True.csv", index=False)


if __name__ == "__main__":
    main()
