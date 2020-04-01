import module1 as m1
import module2 as m2

def mainfun():
    print("Hello from main!")

if __name__ == "__main__":
    print("Main")
    m1.test("a", 3.0)
    m2.test("a", 3.0)
