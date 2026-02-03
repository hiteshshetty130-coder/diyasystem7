import unittest 
from status_engine import status_calculations
from unittest.mock import Mock
import pandas as pd

#all the tests the mock dataframe is created and then assert cases are implemented for that mock file
class Teststatusengine(unittest.TestCase):
    #test_active_to_suspended_transition
    def test_active_suspended(self):
            subs_data=Mock(spec=pd.DataFrame)
            subs_d=pd.DataFrame([{"Subscription_id":"S001","usage_limit_gb":200,"status":"ACTIVE","total_usage_gb":500,"monthly_fee":100}])
            subs_data.copy.return_value=subs_d

            result=status_calculations(subs_data.copy())
            self.assertEqual(result.loc[0,"final_status"],"SUSPENDED")

    #test_suspended_to_active_transition
    def test_suspended_active(self):
        subs_data=Mock(spec=pd.DataFrame)
        subs_d=pd.DataFrame([{"Subscription_id":"S001","usage_limit_gb":200,"status":"SUSPENDED","total_usage_gb":100,"monthly_fee":100}])           
        subs_data.copy.return_value=subs_d

        result=status_calculations(subs_data.copy())
        self.assertEqual(result.loc[0,"final_status"],"ACTIVE")

    #test_cancelled_status_unchanged
    def test_Cancelled(self):
        subs_data=Mock(spec=pd.DataFrame)
        subs_d=pd.DataFrame([{"Subscription_id":"S001","usage_limit_gb":200,"status":"CANCELLED","total_usage_gb":100,"monthly_fee":100}])           
        subs_data.copy.return_value=subs_d

        result=status_calculations(subs_data.copy())
        self.assertEqual(result.loc[0,"final_status"],"CANCELLED")

if __name__=="__main__":
      unittest.main()