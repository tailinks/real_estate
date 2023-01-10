def present_value_annuity(payment:float, discount_rate:float, number_periods:int, growing=False, growth_rate=0)->float:
    if not growing:
        present_value = payment * ((1-(1+discount_rate)**-number_periods)/ discount_rate)
    else:
        present_value = (payment/(discount_rate - growth_rate))* (1-((1 + growth_rate)/(1+discount_rate))** number_periods)
    return present_value

def present_value_perpertuity(payment:float, discount_rate:float, growing=False, growth_rate=0)->float:
    if not growing:
        present_value = payment / discount_rate
    else:
        present_value = (payment * (1+growth_rate))/(discount_rate - growth_rate)
        
    return present_value

def payment_annuity(present_value: float, rate:float, number_periods:int)->float:
    payment = (rate * present_value)/ (1- (1 + rate)**(-number_periods))
    return payment

def rate_conversion(base_rate:float, periods:int)->float:
    rate = (1+base_rate)**(1/periods) -1 
    return rate