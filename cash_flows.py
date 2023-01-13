time_frames = ["Y", "M", "W", "D"]
time_frame_conversion = {"Y": 1, "M" :12, "W": 52, "D": 365}

class InterestRate:
    """
    A class that represents an interest rate.
    """
    
    def __init__(self, rate: float, time_frame: str = "Y") -> None:
        """
        Initializes an InterestRate object with a rate and a time frame.
        
        Args:
        - rate (float): the interest rate
        - time_frame (str): the time frame of the interest rate. Must be one of "Y", "M", "W", "D"
        
        Raises:
        - Exception: if time_frame is not one of "Y", "M", "W", "D"
        """
        if time_frame not in time_frames:
            raise Exception("Time frame must be Y/M/W/D")
        self.rate = rate
        self.time_frame = time_frame
        
    def rate_in(self, target_time_frame: str) -> float:
        """
        Converts the interest rate to a different time frame.
        
        Args:
        - target_time_frame (str): the target time frame. Must be one of "Y", "M", "W", "D"
        
        Returns:
        - float: the interest rate in the target time frame
        
        Raises:
        - Exception: if target_time_frame is not one of "Y", "M", "W", "D"
        """
        if target_time_frame not in time_frames:
            raise Exception("Time frame must be Y/M/W/D")
        target_rate = (1 + self.rate) ** (time_frame_conversion[self.time_frame]/time_frame_conversion[target_time_frame]) - 1
        return target_rate
            

class CashFlow:
    """
    A class that represents a cash flow.
    """
    def __init__(self, amount: float, receivable_in: float, time_frame: str = "Y") -> None:
        """
        Initializes a CashFlow object with an amount, a time frame, and the number of periods until receipt.
        
        Args:
        - amount (float): the amount of the cash flow
        - receivable_in (float): the number of periods until receipt of the cash flow
        - time_frame (str): the time frame of the cash flow. Must be one of "Y", "M", "W", "D"
        
        Raises:
        - Exception: if time_frame is not one of "Y", "M", "W", "D"
        """
        if time_frame not in time_frames:
            raise Exception("Time frame must be Y/M/W/D")
        self.amount = amount
        self.receivable_in = receivable_in
        self.time_frame  = time_frame
        
    def get_present_value(self, discount_rate: InterestRate) -> float:
        """
        Calculates the present value of the cash flow using the given discount rate.
        Args:
        - discount_rate (InterestRate): the discount rate to use for calculating the present value
    
        Returns:
        - float: the present value of the cash flow
        """
        present_value = self.amount / (1 + discount_rate.rate_in(self.time_frame)) ** (self.receivable_in)
        return present_value

class Annuity:
    """
    A class that represents an annuity.
    """
    def init(self, amount: float, payments: float, time_frame: str = "Y", cash_flow_growth: InterestRate = InterestRate(0)) -> None:
        """
        Initializes an Annuity object with an amount, number of payments, time frame, and cash flow growth rate.
        Args:
        - amount (float): the amount of each payment
        - payments (float): the number of payments
        - time_frame (str): the time frame of the payments. Must be one of "Y", "M", "W", "D"
        - cash_flow_growth (InterestRate): the interest rate at which the cash flows grow
        
        Raises:
        - Exception: if time_frame is not one of "Y", "M", "W", "D"
        """
        if time_frame not in time_frames:
            raise Exception("Time frame must be Y/M/W/D")
        self.amount = amount
        self.payments = payments
        self.time_frame = time_frame
        self.cash_flows = []
        for n in range(1, payments + 1): 
            self.cash_flows.append(CashFlow(self.amount * (1 + cash_flow_growth.rate_in(time_frame)) ** n, n, time_frame))
            
    def get_present_value(self, discount_rate: InterestRate) -> float:
        """
        Calculates the present value of the annuity using the given discount rate.
        
        Args:
        - discount_rate (InterestRate): the discount rate to use for calculating the present value
        
        Returns:
        - float: the present value of the annuity
        """
        sum_present_value = 0
        for n in self.cash_flows:
            sum_present_value += n.get_present_value(discount_rate)
                
        return round(sum_present_value, 2)
class Perpetuity(Annuity):
    """
    A class that represents a perpetuity.
    """
    def init(self, amount: float, time_frame: str = "Y", cash_flow_growth: InterestRate = InterestRate(0)) -> None:
        """
        Initializes a Perpetuity object with an amount, time frame, and cash flow growth rate
        Args:
        - amount (float): the amount of each payment
        - time_frame (str): the time frame of the payments. Must be one of "Y", "M", "W", "D"
        - cash_flow_growth (InterestRate): the interest rate at which the cash flows grow
        Raises:
        - Exception: if time_frame is not one of "Y", "M", "W", "D"
        """
        super().init(amount, 1000 * time_frame_conversion[time_frame], time_frame, cash_flow_growth= cash_flow_growth)
        
    # Overriding the get_present_value method to mention it is for perpetuity
    def get_present_value(self, discount_rate: InterestRate) -> float:
        """
        Calculates the present value of the perpetuity using the given discount rate.
        
        Args:
        - discount_rate (InterestRate): the discount rate to use for calculating the present value
        
        Returns:
        - float: the present value of the perpetuity
        """
        return super().get_present_value(discount_rate)



def payment_annuity(present_value: float, InterestRate: InterestRate, number_periods: int, time_frame: str="Y") -> float:
    """
    Calculates the payment of an annuity given the present value, rate, and number of periods.
    
    Parameters:
    - present_value: the present value of the annuity
    - InterestRate: the rate used to calculate payments
    - number_periods: the number of periods over which the payments will be made
    - time_frame (str): the time frame of the interest rate. Must be one of "Y", "M", "W", "D"
    Raises:
    - Exception: if time_frame is not one of "Y", "M", "W", "D"
    
    
    Returns: the payment of the annuity
    """
    if time_frame not in time_frames:
            raise Exception("Time frame must be Y/M/W/D")
    payment = (InterestRate.rate_in(time_frame) * present_value) / (1 - (1 + InterestRate.rate_in(time_frame)) ** -number_periods)
    return payment