from scipy.stats import norm
a=(1-norm.cdf(float(80.0-70.0)/10.0))*100
b=(1-norm.cdf(float(60.0-70.0)/10.0))*100
c=norm.cdf(float(60.0-70.0)/10.0)*100
print ("%.2f" %a)
print ("%.2f" %b)
print ("%.2f" %c)
