
#Code to find fixed monthly payment that will pay off debt



def main():
    beg_balance = 3329.00
    annualInterestRate = 0.2
    fixed = 10
    
    
    outstanding_balance = beg_balance
    
    while( outstanding_balance > 0):
        fixed = fixed +10
        balance = beg_balance
        for i in range(1,13):
                print "Month",i
                unpaid_balance = balance - fixed
                interest =  (annualInterestRate/12.0) * unpaid_balance
                outstanding_balance = unpaid_balance +interest
                balance = outstanding_balance
                i = i + 1
                print "unpaid, outstanding", unpaid_balance, outstanding_balance
    
        
        
        
        
    print "fixed", fixed


if __name__ =="__main__":
    main()