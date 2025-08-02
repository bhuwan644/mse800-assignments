# Sample rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

# Tasks: 
# Convert the list to a NumPy array and print it.
# Print the total rainfall for the week.
# Print the average rainfall for the week.
# Count how many days had no rain (0 mm).
# Print the days (by index) where the rainfall was more than 5 mm.
import numpy as np



sample_rainfall_array=[0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
sample_rainfall_array_via_numpy=np.array(sample_rainfall_array)

def calculation():
    total_rainfall=round(np.sum(sample_rainfall_array_via_numpy),1)
    average_rainfall=round(np.mean(sample_rainfall_array_via_numpy))
    no_rain_days = np.sum(sample_rainfall_array_via_numpy== 0.0)
    rainfall_more_than_5mm=np.where(sample_rainfall_array_via_numpy>5.0)[0]
    print(f"Converted numpy array is: {sample_rainfall_array_via_numpy}\nTotal rainfall for the week is : {total_rainfall}\nAverage rainfall for the week is : {average_rainfall}\nTotal no rain days:{no_rain_days}\nIndices for the days where rainfall was more than 5mm:{rainfall_more_than_5mm}")






if __name__ == "__main__":
    calculation()