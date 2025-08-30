class Vehicles:
    def __init__(self,name,id,mileage):
        self.name=name
        self.id=id
        self.mileage=mileage
        
        
     
    

class Car(Vehicles):
    def print_car_details(self):
        print(f"Cars detail is :{self.name}\n{self.id}\n{self.mileage}")
        
        
class Truck(Vehicles):
    def print_truck_details(self):
        print(f"Truck detail is :{self.name}\n{self.id}\n{self.mileage}")
        
    
        









def main():
      print("main function running")
      car1=Car(name="mercedez",id=1,mileage=10)
      car1.print_car_details()
      car2=Car(name="ferrari",id=2,mileage=8)
      car2.print_car_details()
      truck=Truck(name="toyota",id=1,mileage=10)
      truck.print_truck_details()
      



if __name__=="__main__":
        main()