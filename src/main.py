import logging
from loader import subscription_loader,usage_loader
from usage_aggregator import aggregation
from billing_engine import billing_data
from status_engine import status_calculations
from reporter import genearete_output,generate_billing_summary

#main function loads all the retuned data from the diffrent files and creates a pipeline 

logging.basicConfig(level = logging.INFO, filename = "logs/billing.log",filemode = "w")

def main():
    logging.info("Billing Pipeline Starting.......")
    #loader file function calls
    subscription_df=subscription_loader("data/subscriptions.csv")
    usage_df=usage_loader("data/usage.csv")

    #aggregation file function call
    aggregation_df=aggregation(subscription_df,usage_df)

    #billing file function call
    billed_df=billing_data(aggregation_df)
    status_df=status_calculations(billed_df)

    #report generation file function call
    genearete_output(status_df)
    generate_billing_summary(status_df)

    logging.info("Billing Pipeline Ended......")

if __name__=="__main__":
    main()