import sklearn
import json

train_file=open('training.json', 'r')

N_train=int(train_file.readline())
X_acco, Y_acco, X_bio, Y_bio, X_cs, Y_cs, X_eco, Y_eco, X_pe, Y_pe = ([] for i in range(10))
for i in range(N_train):
    json_acceptable_string = train_file.readline().replace("'","\"")
    train_sample= json.loads(json_acceptable_string)
    keys=[]
    values=[]
    for [k, v] in train_sample.iteritems():
        keys.append(k)
    if 'Accountancy' in keys:
        X_acco.append([v for [k,v] in train_sample.iteritems() if (k!='serial') & (k!='Mathematics')])
        Y_acco.append(train_sample['Mathematics'])
    elif 'Biology' in keys:
        X_bio.append([v for [k,v] in train_sample.iteritems() if (k!='serial') & (k!='Mathematics')])
        Y_bio.append(train_sample ['Mathematics'])
    elif 'ComputerScience' in keys:
        X_cs.append([v for [k,v] in train_sample.iteritems() if (k!='serial') & (k!='Mathematics')])
        Y_cs.append(train_sample['Mathematics'])
    elif 'Economics' in keys:
        X_eco.append([v for [k,v] in train_sample.iteritems() if (k!='serial') & (k!='Mathematics')])
        Y_eco.append(train_sample['Mathematics'])
    elif 'PhysicalEducation' in keys:
        X_pe.append([v for [k,v] in train_sample.iteritems() if (k!='serial') & (k!='Mathematics')])
        Y_pe.append(train_sample['Mathematics'] )                   
        
for a, b, c, d, e, f, g, h, i, j in zip(X_acco, Y_acco, X_bio, Y_bio, X_cs, Y_cs, X_eco, Y_eco, X_pe, Y_pe):
    print a, b, c, d, e, f, g, h, i, j

print len(X_eco)
print len(X_acco)
print len(X_bio)
print len(X_cs)
print len(X_pe)

print len(Y_eco)
print len(Y_acco)
print len(Y_bio)
print len(Y_cs)
print len(Y_pe)
