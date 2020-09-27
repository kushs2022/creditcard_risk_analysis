import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_excel('creditcard.xlsx')
print(dataset.head())
pd.set_option('display.max_columns', None)
print(dataset.head(5))
index = dataset.index
number_of_applications = len(index)
print(number_of_applications)
approved_applications = dataset.loc[dataset.tdecision == 'Approve', 'tdecision'].count()
print(approved_applications)
approval_rate = approved_applications/number_of_applications
approval_rate = approval_rate*100 #For percentage value
print(approval_rate)
booked_applications = dataset.loc[dataset.Booking == 'Y', 'Booking'].count()
print(booked_applications)
booking_rate = booked_applications/approved_applications
booking_rate = booking_rate*100 #For percentage value
print(booking_rate)
all_values = {'Number of Applications' : number_of_applications, 'Approved Applications' : approved_applications,'Approval Rate':approval_rate,'Booked Applications': booked_applications,'Booking Rate':booking_rate}
values = pd.DataFrame(all_values,index = [1])
values
