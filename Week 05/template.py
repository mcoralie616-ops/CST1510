"""
RECORD CHECK  -  my version
===========================

Name  :Coralie Marie
Lane  : IT    
Date  :23/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

#==================================================================
class Record:
    over_limit_count=0
    def __init__(self, label, value, limit):
        self.label = label
        self.value = float(value)
        self.limit = float(limit)

    def status(self):
        """Return the status based on the value and limit."""
                
        p = self.percent()
        if p >= self.limit:
            Record.over_limit_count+=1
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"

    def percent(self):
        perc= (self.value/self.limit)*100
        return perc
    
        
            

# ==================================================================== RECORDS

r1=Record("R-001",67.0,100.0)
r2=Record("R-002",98.0,100.0)
print(r1.status())
print(r2.status())

def load_records():
    records = []  
    with open ("my_records.txt","r") as f: 
        for line in f:
            clean_line=line.strip()
            if clean_line== "":
                continue
            parts=clean_line.split(",")
            if len(parts)==3:
                label=parts[0]
                value=parts[1]
                limit=parts[2]
                new_record=Record(label,value,limit)
                records.append(new_record)
        
    return records
my_records = load_records()
for rec in my_records:
    print(rec.label,rec.value,rec.limit)



# ==================================================================== OUTPUT


for rec in my_records: 
    print()
    print("="*34)
    print(f"RECORD CHECK - {rec.label},{rec.value},{rec.limit}")
    print("="*34)
    print(f"{rec.status()}")
    if rec.status()=="OVER LIMIT":
       Record.over_limit_count+=1
    print(f"Count:{Record.over_limit_count}")

print("="*34)





# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring
