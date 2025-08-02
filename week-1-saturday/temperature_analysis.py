import numpy as np

temp_data=[18.5, 19, 20, 25.0, 2, 30, 13.9]
temp_data_in_fahrenheit=[]
temp_data_via_numpy=np.array(temp_data)



lengthOfArray=len(temp_data)

#### This function calculates the temperature in fahrenheit and provides the list #####
def printTempInFahrenheit():
   for i in range(0,lengthOfArray):
      fahrenheit_temp=round(temp_data[i] * 9/5 + 32, 1)
      temp_data_in_fahrenheit.append(fahrenheit_temp)


#### This function calculates the average temperature of the week #####
def calculateTemp():
   avg_temp=round(np.mean(temp_data_via_numpy),1)

   print(f"Average temperature for the week is {avg_temp}")

#### This function calculates the indices of highest and lowest temperature recorded and also prints the highest and lowest temperatures recorded over the week ######

def identifyTempIndicesAbove20():
   indices = np.where(temp_data_via_numpy > 20)[0]
   highest_temp = np.max(temp_data_via_numpy)
   lowest_temp = np.min(temp_data_via_numpy)
   print (f"Highest temperature recorded is : {highest_temp} and lowest temperature recorded is : {lowest_temp}")
   print (f"Indices where temperatures are recorded higher or equals to 20 degrees are: {indices}")


if __name__ == "__main__":
   calculateTemp()
   printTempInFahrenheit()
   print(f"Fahrenheit temperature list: {temp_data_in_fahrenheit}")
   identifyTempIndicesAbove20()
   
   