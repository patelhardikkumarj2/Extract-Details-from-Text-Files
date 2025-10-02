fname = input("Enter file name: ")
f2name = "C:\\Users\\91972\\Downloads\\" + fname
fhndl = open(f2name)
lcount = 0
rtotal = 0
avg = 0
for line in fhndl:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    lcount = lcount + 1
    pos = line.find('0.')
    fnmber = float(line[pos:])
    rtotal= rtotal + fnmber
    avg = rtotal / lcount



print("Average spam confidence:", avg)

#data = fhndl.read()
#strpdt= data.rstrip()
#print(strpdt.upper())