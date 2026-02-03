import unittest 
from usage_aggregator import aggregation
from unittest.mock import Mock
import pandas as pd

#all the tests the mock dataframe is created and then assert cases are implemented for that mock file
class TestbillingEngine(unittest.TestCase):
    #test_multiple_usage_records
    def test_multiple_records(self):
        subs_data=Mock(spec=pd.DataFrame)
        usage_data=Mock(spec=pd.DataFrame)
        subs_d=pd.DataFrame([{"subscription_id":"S001","usage_limit_gb":200,"status":"ACTIVE","monthly_fee":100}])
        usage_d=pd.DataFrame([{"subscription_id":"S001","usage_date":"2024-03-01","data_used_gb":20},
                              {"subscription_id":"S001","usage_date":"2024-03-04","data_used_gb":30},
                              {"subscription_id":"S001","usage_date":"2024-03-05","data_used_gb":70}])    
        subs_data.copy.return_value=subs_d    
        usage_data.copy.return_value=usage_d

        result=aggregation(subs_data.copy(),usage_data.copy())
        self.assertEqual(result.loc[0,"total_usage_gb"],120)

    #test_invalid_usage_dates
    def test_invalid_dates(self):
        subs_data=Mock(spec=pd.DataFrame)
        usage_data=Mock(spec=pd.DataFrame)
        subs_d=pd.DataFrame([{"subscription_id":"S001","usage_limit_gb":200,"status":"ACTIVE","monthly_fee":100}])
        usage_d=pd.DataFrame([{"subscription_id":"S001","usage_date":"2024-03-01","data_used_gb":20},
                              {"subscription_id":"S001","usage_date":"invalid-date","data_used_gb":30},
                              {"subscription_id":"S001","usage_date":"2024-03-04","data_used_gb":70}])    
        subs_data.copy.return_value=subs_d    
        usage_data.copy.return_value=usage_d

        result=aggregation(subs_data.copy(),usage_data.copy())
        self.assertEqual(result.loc[0,"total_usage_gb"],90)
    
    #test_no_usage_records
    def test_no_records(self):
        subs_data=Mock(spec=pd.DataFrame)
        usage_data=Mock(spec=pd.DataFrame)
        subs_d=pd.DataFrame([{"subscription_id":"S001","usage_limit_gb":200,"status":"ACTIVE","monthly_fee":100}])
        usage_d=pd.DataFrame(columns=["subscription_id","usage_date","data_used_gb"])    
        subs_data.copy.return_value=subs_d    
        usage_data.copy.return_value=usage_d

        result=aggregation(subs_data.copy(),usage_data.copy())
        self.assertEqual(result.loc[0,"total_usage_gb"],0)

if __name__=="__main__":
    unittest.main()
