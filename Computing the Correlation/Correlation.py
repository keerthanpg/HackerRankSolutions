N=int(input())
MPC=[]
for i in range(N):
    inputline=raw_input()
    marklist=[float(x) for x in inputline.split()]
    MPC.append(marklist)


sum_M=sum(x[0] for x in MPC)
sum_P=sum(x[1] for x in MPC)
sum_C=sum(x[2] for x in MPC)
sum_M2=sum(x[0]**2 for x in MPC)
sum_P2=sum(x[1]**2 for x in MPC)
sum_C2=sum(x[2]**2 for x in MPC)
sum_MP=sum(x[0]*x[1] for x in MPC)
sum_PC=sum(x[1]*x[2] for x in MPC)
sum_CM=sum(x[2]*x[0] for x in MPC)

R_MP=(N*sum_MP-sum_M*sum_P)/(((N*sum_M2-sum_M**2)**0.5) * ((N*sum_P2-sum_P**2)**0.5))
R_PC=(N*sum_PC-sum_P*sum_C)/(((N*sum_P2-sum_P**2)**0.5) * ((N*sum_C2-sum_C**2)**0.5))
R_CM=(N*sum_CM-sum_C*sum_M)/(((N*sum_C2-sum_C**2)**0.5) * ((N*sum_M2-sum_M**2)**0.5))

print ("%.2f" %R_MP)
print ("%.2f" %R_PC)
print ("%.2f" %R_CM)


    
    
    #print(re.split(r'\t+', MPC))
    
    #print [splits for splits in MPC.split("\t") if splits is not ""]
