class BuyACar:
    # attributes 
    new: bool
    model: str  # year --> dict[year, list[str]]
    gas: bool  # if False, then electric
    budget: int

    def __init__(self, new: bool, model: str, gas: bool, budget: int): 
        self.new = new
        self.model = model
        self.gas = gas
        self.budegt = budget
    
    def cost(self) -> int: 
        cost: int = 10,000  # base starting price
        while cost > self.budget:
            if self.new: 
                cost += 20,000
            
            if self.gas: 
                cost += 0.0
            else: 
                cost += 20,000
            
            index: int = 0 
            for key in self.model: 
                if 

        if cost > self.budget: 