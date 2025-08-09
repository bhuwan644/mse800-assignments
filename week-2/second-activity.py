class StringManupulator:
    # def __init__(self,text):
    #     self.text=text

    def find_character(self,text,char):
        return text.find(char)
    
    def print_length_of_text(self,text):
        return len(text)
    
    def convert_to_uppercase(self,text):
        return text.upper()
    
    
    
# Creating an instance of the string manupulator

name=StringManupulator()

# Call the find character method on the object


def main():
    final_result=name.find_character('roman', 'z')
    length_of_text=name.print_length_of_text('roman valdez')
    uppercase_of_text=name.convert_to_uppercase('roman valdez')
    print(f"Index of character is: {final_result}\nLength of text provided is {length_of_text}\nUppercase of provided text is : {uppercase_of_text}" )
    
    
    
if __name__=="__main__":
    main()