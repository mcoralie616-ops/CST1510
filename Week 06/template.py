"""
RECORD CHECK  -  my version
===========================

Name  :Coralie Marie 
Lane  :  IT     
Date  :08/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



# ==================================================================== LOAD
import pandas as pd

#load the data from a CSV file 
df =pd.read_csv("my_data.csv")
#Calculate perentage 
df["percent"]=(df["value"] / df["limit"])*100
#new column status
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)
print(df)
#keep rows where status is NOT "OK"
correct = df[df["status"]!= "OK"]
print(correct)


#print the counts per group
print(df.groupby("status")["status"].count())
df.to_csv("final_report.csv",index=False)

#save a bar chart
import matplotlib.pyplot as plt 
df["status"].value_counts().plot(kind="bar")
plt.savefig("my_status_chart.png")



print(df)


