time_frames = ["Y", "M", "W", "D"]

class cash_flow:
    def __init__(self, amount: float, receivable_in: float, time_frame = "Y") -> None:
        if time_frame not in time_frames:
            raise Exception("Time frame must be Y/M/W/D")
        self.amount = amount
        self.receivable_in = receivable_in
        self.time_frame  = time_frame
        
    def get_present_value(self, discount_rate: float) -> float:
        present_value = self.amount / (1 + discount_rate) ** (self.receivable_in)
        return present_value
    
    
class annuity:
    def __init__(self, amount: float, payments: float, time_frame = "Y") -> None:
        if time_frame not in time_frames:
            raise Exception("Time frame must be Y/M/W/D")
        self.amount = amount
        self.payments = payments
        self.time_frame = time_frame
        self.cash_flows = []
        for n in range(1, payments + 1): 
            self.cash_flows.append(cash_flow(self.amount, n, time_frame))

class interest_rate:
    time_frame_conversion = {"Y": 1, "M" :12, "W": 52.18, "D": 365.25}
    def __init__(self, rate: float, time_frame = "Y") -> None:
        if time_frame not in time_frames:
            raise Exception("Time frame must be Y/M/W/D")
        self.rate = rate
        self.time_frame = time_frame
        
    def rate_in(self, target_time_frame: str):
        if target_time_frame not in time_frames:
            raise Exception("Time frame must be Y/M/W/D")
        target_rate = (1 + self.rate) ** (self.time_frame_conversion[self.time_frame]/self.time_frame_conversion[target_time_frame]) - 1
        return target_rate
            