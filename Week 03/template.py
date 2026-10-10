"""
RECORD CHECK  -  my version
===========================

Name  :Coralie Marie 
Lane  :  IT      (delete two)
Date  :10/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
def status_of(percent):
    """Return the status of number whether its over limit,warning or ok """
    if percent>=100:
        return "OVER LIMIT"
    elif percent>=90:
        return "WARNING"
    else:
        return "OK"

def check(value,limit):
    """check(value, limit) that returns the difference and the percentage as two values"""
    difference= limit-value
    percent= (value/limit)*100
    return difference,percent 

def print_report(label, value, limit, difference, percent, status):
    """ Print all the output of the two functions"""
    print(f"{label}\nstatus:{value}\nvalue:{limit}\nlimit:{difference}\ndifference:{percent}\npercentage:{status}\n ")



# ==================================================================== INPUT
# 2. Ask for your three values.
print(" " * 34)
print("=" * 34)
print("RECORD CHECK SVR-01")
print("=" * 34)
input(f"{'Label:':>24}")
print("=" * 34)
gb_used=float(input(f"{'Value: ':>24}"))
print("=" * 34)
gb_total=float(input(f"{'Limit:':>24}"))

label = ""      # replace with an input() call
value = 0.0     # replace with an input() call, converted
limit = 0.0     # replace with an input() call, converted


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
print(" " * 34)
print(" " * 34)
print("_" * 50)
difference = (gb_total - gb_used )
print("_" * 50)



percent= gb_used/gb_total* 100
print(f"{"\033[3m Status: \033[0m":>10}", f"{status_of(percent):>14}\n", f"{'_'*50}\n", f"{"\033[3m Difference and Percentage\033[0m":>10}",f"{check(gb_used,gb_total)}")
print("_" * 50)
print("_" * 50)

add_results = (percent + difference)
print(f"{ "\033[3m The Totality is : \033[0m":>10}",  f"{add_results:>+15.2f}")
print("_" * 50)





over_limit_count=0
while label!="quit":
    label=input(f"{'Label (or quit to stop):':>24}")
    if label == "quit":
        break
    gb_used =float(input(f"{'Value: ':>24}"))
    gb_total=float(input(f"{'Limit:':>24}"))

    difference ,percent= check(gb_used,gb_total)
    status=status_of(percent)

    if status =="OVER LIMIT":
        over_limit_count += 1
     
    print_report(label, gb_used, gb_total, difference, percent, status)
    print(f"OVERLIMIT: {over_limit_count}")


# =================================================================== OUTPUT
# 4. Print the report.

#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here

print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
