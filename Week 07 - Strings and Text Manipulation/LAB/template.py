"""
RECORD CHECK  -  my version
===========================

Name  :coralie marie 
Lane  :   IT      (delete two)
Date  :08/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Parses a messy line into a dictionary"""
    #clean the whole line 
    clean_line = raw_line.strip()

    #split hostname from the rest 
    hostname_part, rest = clean_line.split(",",1)
    hostname = hostname_part.strip().lower()

    #split the rest into pieaxes
    pieces = rest.split(",")
    used_str= pieces[0].strip()
    total_str =pieces[1].strip()

    #convert to floats
    used_value = float(used_str.split("=")[1])
    total_value = float(total_str.split("=")[1])

    #return dictionary 
    return {
        "hostname": hostname,
        "used": used_value,
        "total": total_value
    }

def status_of(record):
    """Determines the status based on usaged percentage"""
    #calculate the percentage 
    percent = (record["used"]/record["total"]) *100

    if percent >= 100:
        return "OVER LIMIT"
    elif percent >=90:
        return "WARNING"
    else:
        return "OK"
    

raw_records = [
    " SRV-01 , used=87 , total=100 ",
    "srv-02,used=120,total=100",
    " Srv-03 , used=95 , total=100 ",
    "SRV-04, used=45 , total=100",
    " Srv-05,used=150, total=100 "
]

over_limit_count =0
print("--- RECORD REPORT ---")
for line in raw_records:
    #parse the line into a dict 
    parsed_dict = parse_line(line)

    current_status = status_of(parsed_dict)

    if current_status == "OVER LIMIT":
        over_limit_count +=1

    print(f"Host: {parsed_dict['hostname'].upper()} | Used: {parsed_dict['used']} | Status: {current_status}")

print("\n--- SUMMARY ---")
print(f"Total records processed: {len(raw_records)}")
print(f"Total OVER LIMIT: {over_limit_count}")

# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = []   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

for raw_record in raw_records:
    pass   # replace with your code


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
