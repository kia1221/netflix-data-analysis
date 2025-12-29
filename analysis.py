import pandas as pd
import matplotlib.pyplot as plt



# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv("data/netflix_titles.csv")

print("Dataset loaded successfully")
print(df.shape)


# =========================
# 2. DATA CLEANING
# =========================


# Check missing values
print("\nMissing values:")
print(df.isnull().sum())


# Fill missing country
df['country'] = df['country'].fillna('Unknown')


# Drop rows with missing rating
df = df.dropna(subset=['rating'])

# Convert date_added to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

print("\nAfter cleaning:")
print(df.isnull().sum())

# =========================
# 3. ANALYSIS & VISUALIZATION
# =========================

# Movies vs TV Shows
plt.figure()
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()


# Top 10 Countries
plt.figure()
df['country'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()


# Year-wise Content Addition
plt.figure()
df['year_added'].value_counts().sort_index().plot(kind='line', marker='o')
plt.title("Netflix Content Added Over the Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.show()

# Ratings Analysis
plt.figure()
df['rating'].value_counts().head(7).plot(kind='bar')
plt.title("Top Content Ratings on Netflix")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Genre Analysis
genres = df['listed_in'].str.split(', ').explode()
plt.figure()
genres.value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()