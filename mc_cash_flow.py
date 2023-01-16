from cash_flows import *
from random import random

class MonteCarloCashFlow(CashFlow):
    def __init__(self, amount: float, receivable_in: float, time_frame: str = "Y", chance_of_zero: float = 0) -> None:
        """
        Initializes a MonteCarloCashFlow object with an amount, a time frame, the number of periods until receipt, and a chance of the amount being zero.
        
        Args:
        - amount (float): the amount of the cash flow
        - receivable_in (float): the number of periods until receipt of the cash flow
        - time_frame (str): the time frame of the cash flow. Must be one of "Y", "M", "W", "D"
        - chance_of_zero (float): the chance that the amount of the cash flow will be zero, between 0 and 1
        
        Raises:
        - Exception: if time_frame is not one of "Y", "M", "W", "D"
        - ValueError: if chance_of_zero is not between 0 and 1
        """
        if time_frame not in time_frames:
            raise Exception("Time frame must be Y/M/W/D")
        if chance_of_zero < 0 or chance_of_zero > 1:
            raise ValueError("Chance of zero must be between 0 and 1")
        self.amount = amount
        self.receivable_in = receivable_in
        self.time_frame  = time_frame
        self.chance_of_zero = chance_of_zero
        
    def get_present_value(self, discount_rate: InterestRate) -> float:
        """
        Calculates the present value of the cash flow using the given discount rate, taking into account the chance of the amount being zero.
        
        Args:
        - discount_rate (InterestRate): the discount rate to use for calculating the present value
    
        Returns:
        - float: the present value of the cash flow, taking into account the chance of the amount being zero
        """
        if random() < self.chance_of_zero:
            return 0
        else:
            present_value = self.amount / (1 + discount_rate.rate_in(self.time_frame)) ** (self.receivable_in)
            return present_value

class MonteCarloAnnuity(Annuity):
    def init(self, amount: float, payments: float, time_frame: str = "Y", cash_flow_growth: InterestRate = InterestRate(0), chance_of_zero: float = 0) -> None:
        """
        Initializes a MonteCarloAnnuity object with an amount, number of payments, time frame, cash flow growth rate, and chance of zero for each cash flow.
        
        Args:
        - amount (float): the amount of each payment
        - payments (float): the number of payments
        - time_frame (str): the time frame of the payments. Must be one of "Y", "M", "W", "D"
        - cash_flow_growth (InterestRate): the interest rate at which the cash flows grow
        - chance_of_zero (float): the chance that the amount of each cash flow will be zero, between 0 and 1
        
        Raises:
        - Exception: if time_frame is not one of "Y", "M", "W", "D"
        - ValueError: if chance_of_zero is not between 0 and 1
        """
        if time_frame not in time_frames:
            raise Exception("Time frame must be Y/M/W/D")
        if chance_of_zero < 0 or chance_of_zero > 1:
            raise ValueError("Chance of zero must be between 0 and 1")
        self.amount = amount
        self.payments = payments
        self.time_frame = time_frame
        self.cash_flows = []
        for n in range(1, payments + 1): 
            self.cash_flows.append(MonteCarloCashFlow(self.amount * (1 + cash_flow_growth.rate_in(time_frame)) ** n, n, time_frame, chance_of_zero))

class MonteCarloPerpetuity(MonteCarloAnnuity):
    def init(self, amount: float, time_frame: str = "Y", cash_flow_growth: InterestRate = InterestRate(0), chance_of_zero: float = 0) -> None:
        """
        Initializes a MonteCarloPerpetuity object with an amount, time frame, cash flow growth rate, and chance of zero for each cash flow.
        
        Args:
        - amount (float): the amount of each payment
        - time_frame (str): the time frame of the payments. Must be one of "Y", "M", "W", "D"
        - cash_flow_growth (InterestRate): the interest rate at which the cash flows grow
        - chance_of_zero (float): the chance that the amount of each cash flow will be zero, between 0 and 1
        
        Raises:
        - Exception: if time_frame is not one of "Y", "M", "W", "D"
        - ValueError: if chance_of_zero is not between 0 and 1
        """
        super().init(amount, 1000 * time_frame_conversion[time_frame], time_frame, cash_flow_growth= cash_flow_growth, chance_of_zero = chance_of_zero)
