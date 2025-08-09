class StringManipulator:
    def __init__(self,text):
        self.text=text
        
    def word_count(self):
        number_of_words=len(self.text.split())
        return number_of_words
        
        
def main():
    input_sentence=input("Please enter the sentence:")
    sentence=StringManipulator(input_sentence)
    total_words=sentence.word_count()
    print(f"Total number of words in the provided sentence is: {total_words}")
    
   
if __name__=="__main__":
    main()