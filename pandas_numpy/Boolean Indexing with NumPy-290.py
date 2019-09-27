## 2. Reading CSV files with NumPy Continued ##

import numpy as np

taxi_raw = np.genfromtxt('nyc_taxis.csv', delimiter=',')
taxi = taxi_raw[1:]
print(taxi)

## 3. Boolean Arrays ##

a = np.array([1, 2, 3, 4, 5])
b = np.array(["blue", "blue", "red", "blue"])
c = np.array([80.0, 103.4, 96.9, 200.3])

a_bool = (np.array(a) <3)
b_bool = (np.array(b) == "blue")
c_bool = (np.array(c) > 100)

## 4. Boolean Indexing with 1D ndarrays ##

pickup_month = taxi[:,1]

january_bool = pickup_month == 1
january = pickup_month[january_bool]
january_rides = january.shape[0]


february_bool = pickup_month == 2
february = pickup_month[february_bool]
february_rides = february.shape[0]
#print(february_rides)

march_bool = pickup_month == 3
march = pickup_month[march_bool]
march_rides = march.shape[0]


## 5. Boolean Indexing with 2D ndarrays ##

tip_amount = taxi[:,12]
tip_bool = (tip_amount > 50)
top_tips = (taxi[:,5:14])[tip_bool]

## 6. Assigning Values in ndarrays ##

# this creates a copy of our taxi ndarray
taxi_modified = taxi.copy()
taxi_modified[28214,5] = 1
taxi_modified[:,0] = 16
taxi_modified[1800:1802,7] = np.mean(taxi_modified[:,7])

## 8. Assignment Using Boolean Arrays Continued ##

# create a new column filled with `0`.
zeros = np.zeros([taxi_modified.shape[0], 1])
taxi_modified = np.concatenate([taxi, zeros], axis=1)
print(taxi_modified)
taxi_modified[taxi_modified[:,5] == 2, 15] = 1
taxi_modified[taxi_modified[:,5] == 3, 15] = 1
taxi_modified[taxi_modified[:,5] == 5, 15] = 1

## 9. Challenge: Which is the most popular airport? ##

drop_off = taxi[:,6]

jfk_bool = (drop_off == 2)
jfk = taxi[jfk_bool]
jfk_count = len(jfk)

lag_bool = (drop_off == 3)
laguardia = taxi[lag_bool]
laguardia_count = len(laguardia)

new_bool = (drop_off == 5)
newark = taxi[new_bool]
newark_count = len(newark)


## 10. Challenge: Calculating Statistics for Trips on Clean Data ##

trip_mph = taxi[:,7] / (taxi[:,8] / 3600)
trip_mph_bool = trip_mph < 100
cleaned_taxi = taxi[trip_mph_bool]

mean_distance = cleaned_taxi[:,7].mean()
mean_length = cleaned_taxi[:,8].mean()
mean_total_amount = cleaned_taxi[:,13].mean()
mean_mph = trip_mph[trip_mph_bool].mean()
