def calculate_tax(income):
    if income < 2_400_000:
        return income*0.13
    
    elif income < 5_000_000:
        return(
             2_400_00*0.13 + 
            (income - 2_400_000) * 0.15
            )
    

    for start, addition, taxrate in tiers:
        return addition+(income-start) * taxrate
    return      

    return income * 0.13
