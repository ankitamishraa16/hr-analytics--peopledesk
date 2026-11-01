import pandas as pd
import matplotlib.pyplot as plt

# PeopleDesk HR Analytics
# Fictional employee data for learning purposes

monthly_data = {
    "Month": pd.date_range("2026-01-01", periods=12, freq="MS"),
    "Hires": [8, 12, 10, 14, 9, 11, 15, 10, 13, 12, 9, 14],
    "Exits": [4, 5, 7, 6, 5, 8, 6, 7, 5, 9, 6, 7],
}

df = pd.DataFrame(monthly_data)
df["Headcount"] = 100 + (df["Hires"] - df["Exits"]).cumsum()
df["MA_3"] = df["Headcount"].rolling(3).mean()
df["MA_6"] = df["Headcount"].rolling(6).mean()

# Chart 1: Headcount trend and moving averages
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(12, 8), sharex=True,
    gridspec_kw={"height_ratios": [3, 1]}
)

ax1.plot(df["Month"], df["Headcount"],
         color="black", linewidth=2.5, label="Headcount")
ax1.plot(df["Month"], df["MA_3"],
         color="blue", linewidth=2, label="3-Month Moving Average")
ax1.plot(df["Month"], df["MA_6"],
         color="red", linewidth=2, label="6-Month Moving Average")

ax1.set_title("PeopleDesk HR Analytics - Workforce Trend")
ax1.set_ylabel("Employees")
ax1.legend()
ax1.grid(alpha=0.25)

ax2.bar(df["Month"], df["Hires"], label="Hires",
        color="seagreen", width=10)
ax2.bar(df["Month"], -df["Exits"], label="Exits",
        color="tomato", width=10)
ax2.axhline(0, color="black", linewidth=0.8)
ax2.set_ylabel("Hires / Exits")
ax2.legend()
ax2.grid(axis="y", alpha=0.25)

plt.tight_layout()
plt.savefig("hr_workforce_trends.png", dpi=150)
plt.show()

# Department analytics using fictional data
departments = pd.DataFrame({
    "Department": ["HR", "Finance", "IT", "Marketing", "Operations"],
    "Employees": [12, 20, 35, 18, 25],
    "Attrition": [2, 3, 4, 5, 3]
})

departments["Attrition_Rate"] = (
    departments["Attrition"] / departments["Employees"] * 100
)

print("\nMONTHLY HR SUMMARY")
print(df[["Month", "Hires", "Exits", "Headcount"]].to_string(index=False))

print("\nDEPARTMENT ANALYTICS")
print(departments.to_string(index=False))

plt.figure(figsize=(9, 5))
plt.bar(departments["Department"], departments["Employees"],
        color="steelblue")
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("department_analytics.png", dpi=150)
plt.show()
