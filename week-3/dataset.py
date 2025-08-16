
import pandas as pd
dataset_path='credit-dataset/crx.data'



class DatasetManipulation:
    def __init__(self,file_path):
         self.file_path=file_path
         
    def convert_to_parquet(self):
        data=pd.read_csv(self.file_path,usecols=[1,2,7,13,14], header=None)
        parqueted_data=data.to_parquet(self.file_path + '.parquet', engine='pyarrow')
        print(f"Data has been converted and saved as Parquet format")
       
    def calculation(self):
        print("Calculation going on:")
        # Reading parquet file
        df = pd.read_parquet("credit-dataset/crx.data.parquet")

        # For all numeric columns
        summary = pd.DataFrame({
            "min": df.min(numeric_only=True),
            "max": df.max(numeric_only=True),
            "avg": round(df.mean(numeric_only=True),2)
        })

        # Absolute values of all numeric columns
       
        print("Summary:\n", summary)
               
        

def main():
    file = DatasetManipulation(dataset_path)
    file.convert_to_parquet() 
    file.calculation()  
    

if __name__=="__main__":
        main()