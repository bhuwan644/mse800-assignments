class FileMethods:
    def __init__(self,file_path):
         self.file_path=file_path
    
    def read_file(self):
        print("Reading a file...................")
        file=open(self.file_path,"r") # Opens the file in a read mode
        print("Here is your file")
        print(file)
    
    
    def write_file(self):
        print("Writing into file")
        file=open(self.file_path,"a") # Opens the file in append mode
        inputted_text=input("Write the text you want to append :")
        file.write(f"{inputted_text}\n")
        print("Congrats, your data has been added into the file")
        file.close()
    


file=FileMethods("demo.txt")

def main():
    print("This is the main function")
    method_inserted_by_user=input("Please choose the method, Do you want to read the file or write into it? Press R if you want to read, else press W to write:  ")
    if(method_inserted_by_user.lower()=="r"):
        file.read_file()
    else:
        file.write_file()



if __name__=="__main__":
        main()