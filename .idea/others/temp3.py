line= 'supportingFiles =COVERAGE:stage0/abg_abg/rules/abg_anthem_coverage_crosswalk.csv;LOA:stage0/abg_abg/rules/abg_anthem_loa_cw.csv'
account = 'ALN_ALN/'
i=0
finalCrosswalks=[]
if line.startswith('supportingFiles'):
    used_crosswalks = line.split('=')[1].strip()
    listOfCW = used_crosswalks.split(';')
    if len(listOfCW) > 1:
        for i in range(len(listOfCW)):
            location = listOfCW[i].split(':')[1]
            crosswalk = "s3://deerwalk-rules/" + account + location
            finalCrosswalks.append( crosswalk)
            i= i+1
    else:
        location = listOfCW[i].split(':')[1]
        finalCrosswalks = "s3://deerwalk-rules/" + account + location

print(finalCrosswalks)