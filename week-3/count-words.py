class FileMethods:
    def __init__(self,file_path):
         self.file_path=file_path
    
    def read_file(self):
        file=open(self.file_path,"r") # Opens the file in a read mode
        
        content = file.read() # Reading the file
        words=content.split() # This splits file into an array of individual words
        total_words=len(words)
        print(f"Total words contained in file is : {total_words}")
    
    
   

file=FileMethods("demo.txt")

def main():
        file.read_file()
  



if __name__=="__main__":
        main()