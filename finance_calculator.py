def present_value_annuity(payment: float, discount_rate: float, number_periods: int, growing=False, growth_rate=0) -> float:
    """
    Calculates the present value of an annuity given the payment, discount rate, and number of periods.
    
    Parameters:
    - payment: the fixed payment per period
    - discount_rate: the rate used to discount the future payments
    - number_periods: the number of periods over which the payments will be made
    - growing: a boolean that indicates whether the payments will grow over time (default: False)
    - growth_rate: the rate at which the payments will grow (default: 0)
    
    Returns: the present value of the annuity
    """
    if growing:
        # Case where payments grow over time
        present_value = (payment / (discount_rate - growth_rate)) * (1 - ((1 + growth_rate) / (1 + discount_rate)) ** number_periods)
    else:
        # Case where payments remain constant over time
        present_value = payment * ((1 - (1 + discount_rate) ** -number_periods) / discount_rate)
    return present_value

def present_value_perpertuity(payment: float, discount_rate: float, growing=False, growth_rate=0) -> float:
    """
    Calculates the present value of a perpetuity given the payment and discount rate.
    
    Parameters:
    - payment: the fixed payment per period
    - discount_rate: the rate used to discount the future payments
    - growing: a boolean that indicates whether the payments will grow over time (default: False)
    - growth_rate: the rate at which the payments will grow (default: 0)
    
    Returns: the present value of the perpetuity
    """
    if growing:
        # Case where payments grow over time
        present_value = (payment * (1 + growth_rate)) / (discount_rate - growth_rate)
    else:
        # Case where payments remain constant over time
        present_value = payment / discount_rate
    return present_value

def payment_annuity(present_value: float, rate: float, number_periods: int) -> float:
    """
    Calculates the payment of an annuity given the present value, rate, and number of periods.
    
    Parameters:
    - present_value: the present value of the annuity
    - rate: the rate used to calculate payments
    - number_periods: the number of periods over which the payments will be made
    
    Returns: the payment of the annuity
    """
    payment = (rate * present_value) / (1 - (1 + rate) ** -number_periods)
    return payment

def rate_conversion(base_rate: float, periods: int) -> float:
    """
    Converts an annual interest rate to the interest rate for a different number of compounding periods.
    
    Parameters:
    - base_rate: the annual interest rate
    - periods: the number of compounding periods per year
    
    Returns: the interest rate for the specified number of compounding periods
    """
    rate = (1 + base_rate) ** (1 / periods) - 1
    return rate
