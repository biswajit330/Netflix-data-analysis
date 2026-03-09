import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("E:\\file_zipper\\Netflix-data-analysis\\netflix_data.csv")

print("First 5 rows:")
print(data.head())

# Average rating using NumPy
avg_rating = np.mean(data["Rating"])
print("\nAverage Rating:", avg_rating)

# Movies per genre
genre_count = data["Genre"].value_counts()
print("\nMovies per Genre:")
print(genre_count)

# Movies released per year
year_count = data["Year"].value_counts().sort_index()

# Top rated movies
top_movies = data.sort_values(by="Rating", ascending=False).head(3)

print("\nTop Rated Movies:")
print(top_movies[["Title","Rating"]])

# -----------------------------
# Visualization
# -----------------------------

# Genre Distribution
plt.figure(figsize=(6,4))
genre_count.plot(kind="bar")

plt.title("Movies by Genre")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.show()

# Movies released per year
plt.figure(figsize=(6,4))
year_count.plot(kind="line", marker="o")

plt.title("Movies Released per Year")
plt.xlabel("Year")
plt.ylabel("Number of Movies")

plt.show()