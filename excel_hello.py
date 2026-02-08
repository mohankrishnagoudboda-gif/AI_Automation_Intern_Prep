import pandas as pd

# Create a simple Excel file
df = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Task": ["Onboard", "Setup Laptop"]
})

# Write to Excel
df.to_excel("hello.xlsx", index=False)
print("Excel file created successfully!")

# Read it back
df2 = pd.read_excel("hello.xlsx")
print("Reading back the Excel file:")
print(df2)