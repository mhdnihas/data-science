import numpy as np

items_purchased = np.array([5, 8, 3, 10, 6])
total_amount_spent = np.array([50.0, 80.0, 30.0, 100.0, 60.0])
time_spent = np.array([15, 25, 10, 30, 20])

covariance_metrix=np.cov((items_purchased,total_amount_spent,time_spent))
print("covariance between purchased and total amound spent:",covariance_metrix[0,1])
print("\ncoveriance between total amount spent and time spent:\n",covariance_metrix[1,2])

correlation_metrix=np.corrcoef((items_purchased,total_amount_spent,time_spent))
print("correlation\n",correlation_metrix)