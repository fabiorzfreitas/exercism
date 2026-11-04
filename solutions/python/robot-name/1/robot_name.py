import random

class Robot:
    name_list = []
    name = None

    def __init__(self):
        if self.name == None:
            temp_name = Robot.name_generator(self)
            if temp_name in Robot.name_list:
                self.__init__
            else:
                self.name = temp_name
                Robot.name_list.append(temp_name)
    
    def reset(self):        
        temp_name = Robot.name_generator(self)
        if temp_name in Robot.name_list:
            self.reset()
        else:
            self.name = temp_name
            Robot.name_list.append(temp_name)


    def name_generator(self):
        generated_name = random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=2) + random.choices("0123456789", k=3)
        return ''.join(generated_name)

