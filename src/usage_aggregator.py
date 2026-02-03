import pandas as pd
import logging

logging.basicConfig(level = logging.INFO, filename = "logs/billing.log",filemode = "w")

#calculates usage aggregation multiple usage records with same id are combined into one
def aggregation(subscription_u_data,usage_u_data):
    try:
        #convert to datetime and check for invalid dates using coerce and handle gracefuuly
        usage_u_data["usage_date"] = pd.to_datetime(usage_u_data["usage_date"], errors = "coerce")
        invalid_dates = usage_u_data[usage_u_data["usage_date"].isna()]
        for rows in invalid_dates.iterrows():
            logging.warning(f"Invalid dates skipped!!:\n{rows}")

        #extract only march 2024 data's
        usage_u_data = usage_u_data[usage_u_data["usage_date"].between("2024-03-01", "2024-03-31")]
        usage_u_data = usage_u_data.groupby("subscription_id")["data_used_gb"].sum().reset_index()
        usage_u_data = usage_u_data.rename(columns={"data_used_gb":"total_usage_gb"})
       
       #merge both data frame into one 
        merge_data = subscription_u_data.merge(usage_u_data,on="subscription_id",how="left")
        merge_data["total_usage_gb"]=merge_data["total_usage_gb"].fillna(0)

        return merge_data

    except Exception as e:
        logging.error("unexcepted error!!",e)
        return pd.DataFrame()

