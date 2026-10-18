"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here
def status_of(percent):
    """Return the status of number whether its over limit,warning or ok """
    if percent>=100:
        return "OVER LIMIT"
    elif percent>=90:
        return "WARNING"
    else:
        return "OK"

def check_recort(value,limit):
    """check_recort(value, limit) that returns the difference and the percentage as two values"""
    difference= limit-value
    percent= (value/limit)*100
    return difference,percent 

def print_report(label, value, limit, difference, percent, status):
    """ Print all the output of the two functions"""
    print(f"{label}\nstatus:{value}\nvalue:{limit}\nlimit:{difference}\ndifference:{percent}\npercentage:{status}\n ")
   



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records= []   
def load_records(path):
    """ load records from a file and rerurns a list of dictionaries"""
    try: 
        records=[]
        with open(path,"r") as f:
            for line in f:
                parts=line.strip().split(",")


                label=parts[0]
                value=float(parts[1])
                limit=float(parts[2])

               

                records_dict={"label":label, "value":value, "limit":limit}
                records.append(records_dict)
        return records
    except FileNotFoundError: 
        print("File not found")
        return[]

my_records = load_records("data.txt")
print(my_records )        



# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here
my_records = load_records("data.txt")
overlimit_count=0
for record in my_records :
    print(f"{record["label"]}:")
    
    if record ["value"] > record["limit"]:
        overlimit_count +=1
        print("OVER LIMIT")
    else:
        print("OK")
    print(f"OVERLIMIT: {overlimit_count}")



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
