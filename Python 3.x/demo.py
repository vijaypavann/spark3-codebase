
class Demo():
    """
    Utility class used to demo the features available
    :param1: int value to initialize
    """
    def __init__(self, param1: int, param2: str):
        self.param1 = param1
        self.param2 = param2
        print(self.__dict__)

if __name__ == "__main__":
    ref = Demo(1, "abc") 