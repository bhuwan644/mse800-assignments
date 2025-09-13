
from abc import ABC


class Shape(ABC):  ## This is the abstract class 
    def __init__(self,shape_type:str):
        self.shape_type=shape_type
    def draw(self):
        return (f"Drawing {self.shape_type}")
    
    
class ShapeFactory:
    valid_shapes={"circle","square","rectangle"}
    @classmethod
    def create_shape(cls,shape_type:str):
        shape_type=shape_type.lower()
        print(f"Shape type for the provided shape is :{shape_type}")
        if shape_type in cls.valid_shapes:
            print("Conditon match")
            return Shape(shape_type)
        else:
            raise ValueError(f"Unknown shape {shape_type}  provided")
        
        
        
def main():
    print("Main function is running")
    
    input_shape=(input("Let us know what do you want to draw:")).lower()
    print(f"input provided: {input_shape}")
    factory1=ShapeFactory()
    result=factory1.create_shape(input_shape)
    print(result.draw())
        
if __name__=="__main__":
        main()
        


