from datetime import datetime as dt
import pandas as pd
print("started functions")
###############

data=pd.read_csv('C:/Users/user/Documents/project/dummy dataset/dummy.csv')
# revenue generated by each carepartner
data["Revenue_generated"]=(data.total_fare-data.care_partner_earnings)


# creating month,year,date columns
data['Month']=pd.to_datetime(data['job_est_time'],utc=True).dt.month
data['Year']=pd.to_datetime(data['job_est_time'],utc=True).dt.year
data['Date']=pd.to_datetime(data['job_est_time'],utc=True).dt.date

#creating m&y column
data['m&y']=data['Month'].map(str)+','+data['Year'].map(str)

#creating 'new_date' column
date = []
for i in data["job_est_time"]:
    strDate = str(i)
    x = pd.to_datetime(strDate)
    date.append(dt.strftime(x, '%Y-%m-%d'))

data['new_date'] = date
data.sort_values(by='new_date', inplace=True)
data.reset_index(drop=True, inplace=True)

data.dropna(axis=0,subset=['driver_name'],inplace=True)

def get_data():
    return data

print("end functions")


###############
