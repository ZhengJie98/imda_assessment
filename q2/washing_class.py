class washing_type:

    def __init__(self, name, cost, time):
        self.name = name
        self.cost = cost
        self.time = time

    def get_name(self):
        return self.name
    
    def get_cost(self):
        return self.cost
    
    def get_time(self):
        return self.time

quick_wash = washing_type("Quick Wash (10 minutes - $2)", 2,10)
mild_wash = washing_type("Mild Wash (30 minutes - $2.50)", 2.5, 30)
medium_wash= washing_type("Medium Wash (45 minutes - $4.20)",4.2,45)
heavy_wash= washing_type("Heavy Wash (1 hour - $6)",6,60)
washing_list = [quick_wash,mild_wash,medium_wash,heavy_wash]

# print(washing_list[3].get_cost())