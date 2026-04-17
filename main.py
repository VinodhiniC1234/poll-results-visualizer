import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/poll_data.csv")
df.columns = df.columns.str.strip()

print("Dataset Preview:")
print(df.head())

# -----------------------------
# Basic Analysis
# -----------------------------
tool_counts = df["Preferred Tool"].value_counts()
tool_percent = (tool_counts / len(df)) * 100

print("\nVote Share (%):")
print(tool_percent)

# -----------------------------
# Bar Chart
# -----------------------------
plt.figure()
tool_counts.plot(kind='bar')
plt.title("Tool Preference")
plt.savefig("outputs/bar_chart.png")
plt.show()

# -----------------------------
# Pie Chart
# -----------------------------
plt.figure()
tool_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Vote Share")
plt.savefig("outputs/pie_chart.png")
plt.show()

# -----------------------------
# NEW: Age Group Analysis
# -----------------------------
plt.figure()
sns.countplot(x="Age Group", hue="Preferred Tool", data=df)
plt.title("Tool Preference by Age Group")
plt.savefig("outputs/age_analysis.png")
plt.show()

# -----------------------------
# NEW: Gender Analysis
# -----------------------------
plt.figure()
sns.countplot(x="Gender", hue="Preferred Tool", data=df)
plt.title("Tool Preference by Gender")
plt.savefig("outputs/gender_analysis.png")
plt.show()

# -----------------------------
# Insight
# -----------------------------
print("\nMost Preferred Tool:", tool_counts.idxmax())