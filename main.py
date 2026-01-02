import pandas as pd

# 1. ЗАВАНТАЖЕННЯ ДАНИХ

books = pd.read_csv("books.csv")
ratings = pd.read_csv("ratings.csv")
book_tags = pd.read_csv("book_tags.csv")
tags = pd.read_csv("tags.csv")


# ОЧИЩЕННЯ СМІТТЄВОГО ВХОДУ

books = books[books["book_id"] > 0]
ratings = ratings[(ratings["book_id"] > 0) & (ratings["rating"] > 0)]


# СЕРЕДНІЙ РЕЙТИНГ ДЛЯ КОЖНОЇ КНИГИ

rating_stats = ratings.groupby("book_id").agg(
    mean_rating=("rating", "mean"),
    rating_count=("rating", "count")
).reset_index()

# поєднання датасетів
df = books.merge(rating_stats, on="book_id", how="inner")

# 4. РЕЙТИНГ З ПОРОГОМ ОЦІНОК
MIN_RATINGS = 100
df_thr = df[df["rating_count"] >= MIN_RATINGS]

top10 = df_thr.sort_values("mean_rating", ascending=False).head(10)


#  ВИЗНАЧЕННЯ ЖАНРІВ

book_tags = book_tags.merge(tags, on="tag_id", how="left")
book_tags["tag_name"] = book_tags["tag_name"].str.lower()

GENRES = [
    "fantasy", "romance", "science fiction", "fiction",
    "classics", "literature", "historical fiction",
    "young adult", "mystery", "thriller", "horror"
]

genre_tags = book_tags[book_tags["tag_name"].isin(GENRES)]


# ЖАНРОВЕ ПОКРИТТЯ ДЛЯ КОЖНОЇ КНИГИ

genres_per_book = (
    genre_tags.groupby("goodreads_book_id")["tag_name"]
    .nunique()
    .reset_index(name="genre_count")
)

df = df.merge(
    genres_per_book,
    left_on="book_id",
    right_on="goodreads_book_id",
    how="left"
)

df["genre_count"] = df["genre_count"].fillna(0).astype(int)


# ЖАНРИ ДЛЯ ТОП-10 КНИГ

top10_genres = (
    genre_tags[genre_tags["goodreads_book_id"].isin(top10["book_id"])]
    .groupby("goodreads_book_id")["tag_name"]
    .apply(list)
    .reset_index()
)

top10_final = top10.merge(
    top10_genres,
    left_on="book_id",
    right_on="goodreads_book_id",
    how="left"
)

top10_final["tag_name"] = top10_final["tag_name"].apply(
    lambda x: x if isinstance(x, list) else []
)


#ВИВІД ТОП-10 КНИГ

print("\n=== ТОП-10 КНИГ ЗА СЕРЕДНІМ РЕЙТИНГОМ (≥100 оцінок) ===\n")

for i, row in enumerate(top10_final.itertuples(), start=1):
    genres = ", ".join(row.tag_name) if row.tag_name else "немає визначених жанрів"
    print(f"{i}. {row.title}")
    print(f"   середній рейтинг: {row.mean_rating:.2f}")
    print(f"   кількість оцінок: {row.rating_count}")
    print(f"   жанри: {genres}\n")

# НАЙПОПУЛЯРНІШІ ЖАНРИ У ТОП-10

genre_popularity = (
    genre_tags[genre_tags["goodreads_book_id"].isin(top10["book_id"])]
    ["tag_name"]
    .value_counts()
)

print("НАЙПОПУЛЯРНІШІ ЖАНРИ У TOP-10 ")
print(genre_popularity)

