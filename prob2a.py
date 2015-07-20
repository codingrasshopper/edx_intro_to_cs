




def main():
    balance = 4842.00
    monthlyPaymentRate = 0.04
    annualInterestRate = 0.2
    TAP = 0.0
    i=1
    # min_monthly_payment = balance * monthlyPaymentRate
    #unpaid_balance = balance - min_monthly_payment
    #interest = (annualInterestRate/12.0) * unpaid_balance
    
 
   
    prev_balance = balance
    for i in range (1,13):
        #prev_balance = outstanding_balance
        
        print "Month",i
        min_monthly_payment = prev_balance * monthlyPaymentRate
        print "Minimum monthly payment:" , round(min_monthly_payment,2)  
        unpaid_balance = prev_balance - min_monthly_payment
        interest = (annualInterestRate/12.0) * unpaid_balance
        #print "interest", interest
        outstanding_balance = unpaid_balance +interest
        TAP = TAP + min_monthly_payment
        RB = outstanding_balance
        prev_balance = outstanding_balance
        print "Remaining balance:", round(RB,2)
        i= i+1
        
    print "Total amount paid", round(TAP,2)
    print "Remaining balance", round(RB,2)
        
    
    
    
    
    
if __name__ =="__main__":
    main()