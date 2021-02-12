import csv
import sys
import numpy as np

def convert_row(row):
    return(int(row[0]),int(row[1]),int(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),int(row[7]))

def convert_row_truth(row):
    return(int(row[0]),int(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),str(row[7]))

def convert_muon_data(fname):
    outf = open(fname.replace('.csv','_mod.csv'),'w')
    contains_truth = 'withtruth' in fname

    with open(fname) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        for index,row in enumerate(csv_reader):
            if index==0:
                outf.write(','.join(row)+'\n')
                continue
            if contains_truth:
                nevt,nmu,eta,mass,phi,pt,charge,truth = convert_row_truth(row)
                truth = True if truth == 'True' else False
            else:
                nrow,nevt,nmu,eta,mass,phi,pt,charge = convert_row(row)
            px = pt*np.cos(phi)
            py = pt*np.sin(phi)
            theta = 2*np.arctan(np.exp(-eta))
            p = pt/np.sin(theta)
            pz = p*np.cos(theta)
            E = np.sqrt(p*p + mass*mass)
            outvals = [nevt,nmu,px,py,pz,E,charge]
        if contains_truth: outvals.append(truth)
        else:
            outvals.insert(0,nrow)
        outrow = ','.join(str(x) for x in outvals)
        outf.write(outrow+'\n')
        
    csv_file.close()
    outf.close()
            
if __name__ == '__main__':
    convert_muon_data(sys.argv[1])
