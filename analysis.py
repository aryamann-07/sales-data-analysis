# Sales Data Analysis using pandas

import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Sales": [50000, 30000, 20000, 70000, 40000],
    "Month": ["Jan", "Jan", "Jan", "Feb", "Feb"]
}

df = pd.DataFrame(data)

# Total sales
print("Total Sales:", df["Sales"].sum())

# Best selling product
print("Best Product:", df.groupby("Product")["Sales"].sum().idxmax())

# Monthly sales
print("Monthly Sales:\n", df.groupby("Month")["Sales"].sum())
