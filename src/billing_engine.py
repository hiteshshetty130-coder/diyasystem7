import pandas as pd
import logging
import os
os.makedirs("logs", exist_ok=True)

logging.basicConfig(level = logging.INFO, filename = "logs/billing.log",filemode = "w")

#function to calculate overage according to the business rules
def gb_calculation(data):
    try:
        status=str(data["status"])
        usage=int(data["total_usage_gb"])
        usage_limit=int(data["usage_limit_gb"])

        if status=="CANCELLED":
            return 0
        elif status=="SUSPENDED":
            return 0
        else:
            if usage<=usage_limit:
                return 0
            elif usage>usage_limit:
                return round(usage-usage_limit)
            
    except Exception as e:
        logging.error(f"Overage calculation failed!!, Error = {e}")
        return 0
    
#function to calculate total bill according to the business rules
def total_bill_calculations(data):
    try:
        status=str(data["status"])
        monthly_bill=data["monthly_fee"]
        if status=="CANCELLED":
            return 0
        elif status=="SUSPENDED":
            return monthly_bill
        
        overage_charge=data["overage_gb"]*10
        return monthly_bill+overage_charge

    except Exception as e:
        logging.error(f"Overage calculation failed!!, Error = {e}")
        return 0
    

#calculates overage and total bill using apply function
def billing_data(df):
    try:
        df["overage_gb"]=df.apply(gb_calculation,axis=1)
        df["total_bill"]=df.apply(total_bill_calculations,axis=1)
        return df

    except Exception as e:
        logging.exception("Unexpected Error!!",e)
        return pd.DataFrame()




