import pandas as pd
import logging

pd.set_option("display.max_columns",12)
logging.basicConfig(level = logging.INFO, filename = "logs/billing.log",filemode = "w")

#first loads existing function and updates the final status according to the rules
def status_eval(data):
    try:
        status=str(data["status"])
        usage=data["total_usage_gb"]
        limit=data["usage_limit_gb"]

        if status=="CANCELLED":
            return "CANCELLED"
        elif usage > 1.5 * limit :
            return "SUSPENDED"
        
        elif status=="SUSPENDED" and usage<=limit:
            return "ACTIVE"
        else:
            return status
    
    except Exception as e:
        logging.error(f"Status Evaluation failed !!, Error = {e}")


#function to calculate final status using apply function
def status_calculations(df):
    try:
        df["final_status"]=df.apply(status_eval,axis=1)
        logging.info(df)
        return df
    
    except Exception as e:
        logging.error("Failed to load and find status!!",e)
        return pd.DataFrame()
    

    