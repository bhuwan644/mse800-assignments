from abc import ABC, abstractmethod

# Abstract Shape
class Shape(ABC):
    def __init__(self, shape_type: str):
        self.shape_type = shape_type

    @abstractmethod
    def draw(self):
        pass


# Concrete Subclasses
class Circle(Shape):
    def __init__(self):
        super().__init__("circle")

    def draw(self):
        return "Drawing a Circle"


class Square(Shape):
    def __init__(self):
        super().__init__("square")

    def draw(self):
        return "Drawing a Square"


class Triangle(Shape):
    def __init__(self):
        super().__init__("triangle")

    def draw(self):
        return "Drawing a Trianle"


# Factory that chooses the right subclass
class ShapeFactory:
    valid_shapes = {
        "circle": Circle,
        "square": Square,
        "triangle": Triangle
    }

    @classmethod
    def create_shape(cls, shape_type: str):
        shape_type = shape_type.lower()
        if shape_type in cls.valid_shapes:
            return cls.valid_shapes[shape_type]()  # instantiate proper subclass
        else:
            raise ValueError(f"Unknown shape {shape_type} provided")


def main():
    input_shape = input("Enter a shape: ")
    shape = ShapeFactory.create_shape(input_shape)
    print(shape.draw())


if __name__ == "__main__":
    main()
