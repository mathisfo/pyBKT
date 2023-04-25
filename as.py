from pyBKT.models import Model



def main():
    # Initialize the model with an optional seed
    model = Model(seed=42, num_fits=1)

    # Fetch Assistments and CognitiveTutor data (optional - if you have your own dataset, that's fine too!)
    # model.fetch_dataset('https://raw.githubusercontent.com/CAHLR/pyBKT-examples/master/data/ct.csv', '.')
    model.fetch_dataset(
        "https://raw.githubusercontent.com/CAHLR/pyBKT-examples/master/data/as.csv", "."
    )

    # Train a simple BKT model on one skill in the CT dataset
    # Note that calling fit deletes any previous trained BKT model!
    # model.fit(data_path = 'ct.csv', skills = "Plot imperfect radical")

    model.fit(data_path="as.csv", forgets=True, skills="Box and Whisker")

    preds_df = model.predict(data_path="as.csv")

    # View the trained parameters!
    # print(model.params())

    # Save predictions to a CSV file

    preds_df[preds_df["skill_name"] == "Box and Whisker"][
        ["user_id", "correct", "correct_predictions", "state_predictions"]
    ].to_csv("as.csv", index=False)


if __name__ == "__main__":
    main()
