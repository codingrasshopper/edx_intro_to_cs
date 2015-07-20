#Code to find fixed monthly payment that will pay off debt by using bisection method



def main():
    beg_balance = 999999
    annualInterestRate = 0.18
    monthly_int_rate = annualInterestRate/ 12.0
  
    low_bound = beg_balance/12.0
    upper_bound = (beg_balance*((1+monthly_int_rate)**12))/12.0
    
    
    outstanding_balance = beg_balance
    
    while True:
        limit = (low_bound + upper_bound ) /2
        print "limit beg", limit
        print "limit lower, upper", low_bound, upper_bound
        balance = beg_balance
        for i in range(1,13):
                print "Month",i
                unpaid_balance = round(balance - limit , 2)
                interest =  (annualInterestRate/12.0) * unpaid_balance
                outstanding_balance = round(unpaid_balance +interest , 2)
                balance = outstanding_balance
                i = i + 1
                print "unpaid, outstanding", unpaid_balance, outstanding_balance
                
        if outstanding_balance > 0:
                low_bound = limit 
        elif outstanding_balance < 0:
                upper_bound = limit        
    

        
        if    (-0.01 <= outstanding_balance and outstanding_balance <= 0.01):
            break
    
        
        
        
    print "limit",limit


if __name__ =="__main__":
    main()