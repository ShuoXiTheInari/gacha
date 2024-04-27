
def expaction(p,n,P_x,type):
    if type == "mi":
        E = sum([i*p*(1-p)**(i-1) for i in range(1,n)]) + P_x*n*(1-p)**(n-1) + (1-P_x)*(1-p)**(n-1)*(sum([(i)*p*(1-p)**(i-2) for i in range(n+1,2*n-1)]) + 2*n*(1-p)**(2*n-2))
    
    elif type == "single":
        E = sum([i*p*(1-p)**(i-1) for i in range(1,n)]) + n*(1-p)**(n-1)
    
    elif type == "none":
        E = 1/p
    E= round(E,3)
    return E
def max_p_worst(p,n,P_x,type):
    if type=="mi":
        p_worst =(1-P_x)*((1-p)**(2*n-2))
        p_worst = round(p_worst,3)

    elif type == "single":
        p_worst = (1-p)**(n-1)
        p_worst = round(p_worst,3)
    else:
        p_worst="-"   
    return p_worst