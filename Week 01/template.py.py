"""
RECORD CHECK  -  my version
===========================

Name  :Coralie Marie
Lane  :IT
Date  :23/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
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



#    Remember: input() always gives back text.

label = ""      # : replace with an input() call
first = 0.0     # : replace with an input() call, converted
second = 0.0    # : replace with an input() call, converted


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
print(" " * 34)
print(" " * 34)
print("_" * 50)
difference_num = (gb_total - gb_used )
print(f"{"\033[3m Free GB is: \033[0m":>10}", f"{difference_num:>+21.2f}")
print("_" * 50)



perc_calculation= gb_used/gb_total* 100
print(f"{"\033[3m The Percentage is: \033[0m":>10}", f"{perc_calculation:>+14.2f} %")
print("_" * 50)
add_results = (perc_calculation + difference_num)
print(f"{ "\033[3m The Totality is : \033[0m":>10}",  f"{add_results:>+15.2f}")
print("_" * 50)
print(" " * 34)
print(" " * 34)


#    Do not type the answers. Calculate them.

difference = 0.0   #
percent = 0.0      #


# =================================================================== OUTPUT
# 3. Print the report.

#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here

print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
