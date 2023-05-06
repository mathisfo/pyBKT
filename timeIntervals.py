# Question 3: Does binned response time have an effect on the learn rate?
# Does it improve the RMSE of the model compared to the normal template_id
# based multilearn/guess?
import matplotlib.pyplot as plt
from pyBKT.models import Model
import pandas as pd
import numpy as np

def main():   
    model = Model(seed=42, num_fits=1)


    as_df = pd.read_csv("data/-1/AllChallengesDurationCategory.csv")
    learn_maps = {
        0: "less than 10s",
        1: "less than 20s",
        2: "less than 30s",
        3: "less than 40s",
        4: "less than 50s",
    }
    as_df["resp_t"] = (as_df["duration"]).map(learn_maps).fillna("other")
    model.fit(data=as_df, multilearn="resp_t")
    params_df = model.params().reset_index()
    plt.figure(figsize=(12, 6))
    params_df[params_df["param"] == "learns"].groupby("class")["value"].plot.kde(
        bw_method=0.2
    )
    plt.xlim((0, 1))
    plt.legend()
    plt.title("Frequency of Learn Rate Parameters with Response Time")
    plt.xlabel("Learn Rate")

    simple_rmse = model.crossvalidate(data=as_df)
    resptime_combo_rmse = model.crossvalidate(
        data=as_df, multigs="resp_t", multilearn="resp_t"
    )
    normal_combo_rmse = model.crossvalidate(data=as_df, multigs=True, multilearn=True)
    rmse_diff = (resptime_combo_rmse - normal_combo_rmse)["rmse"].mean()
    print("RMSE Improvement using Resp. Time: %f" % rmse_diff)
    params_df[params_df["param"] == "learns"].groupby("class").mean()[["value"]].rename(
        columns={"value": "mean learn rate"}
    )

if __name__ == "__main__":
    main()