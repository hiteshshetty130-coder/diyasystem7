import pandas as pd
import logging 
import json

logging.basicConfig(level = logging.INFO, filename = "logs/billing.log",filemode = "w")

#from the final dataframe after all the adjustments are made we convert the dataframe to the csv file 
def genearete_output(df):
    columns=["subscription_id","customer_id","plan",
         "total_usage_gb","overage_gb","total_bill","final_status"]
    df.to_csv("billing_output.csv",columns=columns,index=False)
    logging.info("Output file created successfully with all required columns!!")

#json file which contains all the metrics which was mentioned
def generate_billing_summary(df):
    file="billing_summary.json"

    summary={"total_subscriptions":len(df),
             "active_subscriptions":int((df["final_status"]=="ACTIVE").sum()),
             "suspended_subscriptions":int((df["final_status"]=="SUSPENDED").sum()),
             "cancelled_subscriptions":int((df["final_status"]=="CANCELLED").sum()),
             "Total_revenue":int(df["total_bill"].sum()),
             "Average_bill":df["total_bill"].mean()}
    
    with open(file,"w")as f:
        json.dump(summary,f,indent=4)



