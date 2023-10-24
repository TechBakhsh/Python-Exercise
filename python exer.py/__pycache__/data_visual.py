
import seaborn as sns
import matplotlib.pyplot as plt  # Corrected import statement

sns.set_theme(style="ticks", color_codes=True)

# Import dataset
titanic = sns.load_dataset("titanic")
print(titanic)

# Plot basic graph
p = sns.countplot(x="sex", data=titanic, hue="class")
p.set_title("Malik MB Count plot")
plt.show()  # Corrected plt.show() call