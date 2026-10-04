"""
RECORD CHECK  -  my version
===========================

Name  :Coralie Marie
Lane  :  IT 
Date  :02/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask for your three values.
#     (a name, a hostname, an IP)  -> no conversion needed


print(" " * 34)
print("=" * 34)
print("RECORD CHECK SVR-01")
print("=" * 34)
gb_used=float(input(f"{'Enter your GB used: ':>24}"))
print("=" * 34)
input(f"{'Enter your hostname:':>24}")
print("=" * 34)
gb_total=float(input(f"{'Enter your GB total:':>24}"))




label = ""      # replace with an input() call
value = 0.0     # replace with an input() call, converted with float()
limit = 0.0     # replace with an input() call, converted with float()


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.  
print(" " * 34)
print(" " * 34)
print("_" * 50)
difference_num = (gb_total - gb_used )
print(f"{"\033[3m Used           : \033[0m":>18}", f"{difference_num:>+15.2f}")
print("_" * 50)


perc_calculation= gb_used/gb_total* 100
print(f"{"\033[3m Percentage     : \033[0m":>18}", f"{perc_calculation:>+15.2f} %")
print("_" * 50)
add_results = (perc_calculation + difference_num) 
print(f"{"\033[3m Total          : \033[0m":>18}",  f"{add_results:>+15.2f}")
print("_" * 50)


value = gb_used
limit = 100
print(f"{"\033[3m Value          :\033[0m":>5}",f"{value:>15}")
print("_" * 50)
if value >=limit:
    status=print(f"{"\033[3m Status        : OVER LIMIT":>25}")
elif value > 90 :
    status=print(f"{"\033[3m Status        : WARNING":>25}")
else:
    status=print(f"{"\033[3m Status        : OK":>25}")
print(" " * 34)
print(" " * 34)



difference = 0.0   # replace with your calculation
percent = 0.0       # replace with your calculation
# 3. Decide a status and store it in a variable called status.




#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

status = ""   # replace with your if / else (or if / elif / else)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
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
#    [ ] Check every variable name says what it holds
