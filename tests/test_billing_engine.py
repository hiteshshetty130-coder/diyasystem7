import unittest 
from billing_engine import billing_data
from unittest.mock import Mock
import pandas as pd

#all the tests the mock dataframe is created and then assert cases are implemented for that mock file
class TestbillingEngine(unittest.TestCase):
    #test_bill_without_overage
    def test_without_overage(self):
        subs_data=Mock(spec=pd.DataFrame)
        subs_d=pd.DataFrame([{"Subscription_id":"S001","usage_limit_gb":10,"status":"ACTIVE","total_usage_gb":8,"monthly_fee":100}])
        subs_data.copy.return_value=subs_d

        result=billing_data(subs_data.copy())
        self.assertEqual(result.loc[0,"overage_gb"],0)

    #test_bill_with_overage
    def test_with_overage(self):
        subs_data=Mock(spec=pd.DataFrame)
        subs_d=pd.DataFrame([{"Subscription_id":"S002","usage_limit_gb":10,"status":"ACTIVE","total_usage_gb":15,"monthly_fee":100}])        
        subs_data.copy.return_value=subs_d
        
        result=billing_data(subs_data.copy())
        self.assertEqual(result.loc[0,"overage_gb"],5)
    
    #test_suspended_subscription_billing
    def test_suspended_subscription(self):
        subs_data=Mock(spec=pd.DataFrame)
        subs_d=pd.DataFrame([{"Subscription_id":"S002","usage_limit_gb":10,"status":"SUSPENDED","total_usage_gb":15,"monthly_fee":100}])
        subs_data.copy.return_value=subs_d

        result=billing_data(subs_data.copy())                                         
        self.assertEqual(result.loc[0,"overage_gb"],0)

    #test_cancelled_subscription_billing
    def test_cancelled_subscription(self):
        subs_data=Mock(spec=pd.DataFrame)
        subs_d=pd.DataFrame([{"Subscription_id":"S002","usage_limit_gb":10,"status":"CANCELLED","total_usage_gb":15,"monthly_fee":100}])
        subs_data.copy.return_value=subs_d

        result=billing_data(subs_data.copy())
        self.assertEqual(result.loc[0,"overage_gb"],0)
        
if __name__=="__main__":
    unittest.main()