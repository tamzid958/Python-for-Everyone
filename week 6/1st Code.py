def computepay(h,r):
    x=0
    if h > 40.0:
     x = r * 40.0 +(1.5*r*(h-40.0))
    elif h <= 40 :
   	 x= h*r
    return x

hrs = float(input("Enter Hours:"))
rate = float(input("Enter the rate:"))
p = computepay(hrs,rate)

p= str(p)

print("Pay " +p)