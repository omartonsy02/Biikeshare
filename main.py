import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("tmdb-movies.csv")


def details():
    print(df.shape)
    print(df.count())
    print(df.describe())


def runtime():
    """movies run time."""
    plt.figure(figsize=(20, 10))
    sns.histplot(df["runtime"], bins=15)
    plt.xlabel('min', fontsize=15)
    plt.ylabel('num of mov', fontsize=20)
    plt.title('Movies run time', fontsize=20)
    plt.show()
    # how is the runtime changes with years
    runtime_in_years = df.groupby(['release_year'])['runtime'].describe()
    print(runtime_in_years)
    avg_run_by_year = runtime_in_years['mean']
    min_run_by_year = runtime_in_years['mean'] - runtime_in_years['std']
    max_run_by_year = runtime_in_years['mean'] + runtime_in_years['std']
    plt.plot(avg_run_by_year)
    plt.plot(min_run_by_year)
    plt.plot(max_run_by_year)
    plt.title('how is the runtime changes with years')
    plt.xlabel('year', fontsize=15)
    plt.ylabel('min', fontsize=20)
    plt.show()
    # what is the longest movie
    print("lg")
    print(df.original_title[df.runtime == df.runtime.max()])
    print(df.runtime[df.runtime == df.runtime.max()])
    # what is the shortest movie
    ddf = df[df['runtime'] != 0]
    print("sh")
    print(ddf.original_title[ddf.runtime == ddf.runtime.min()])
    print(ddf.runtime.min())


def year():
    """the most release year"""
    x = df['release_year']
    sns.countplot(x=x)
    plt.xticks(rotation=90)
    plt.title("the most release year")
    plt.show()


def month():
    """the most release month"""
    df['release_date'] = pd.to_datetime(df['release_date'])
    y = df['release_date'].dt.month
    plt.title("the most release month")
    sns.countplot(x=y)
    plt.show()


def profit():
    """The 10 highest-grossing movies of all time"""
    df['profit'] = df['revenue'] - df['budget']
    dfs = df[['original_title', 'profit']].sort_values('profit', ascending=False).head(10)
    sns.barplot(x='profit', y='original_title', data=dfs, palette='Blues')
    plt.title('the highest 10 profit movie', size=25)
    plt.yticks(size=20)
    plt.xticks(size=20)
    plt.show()
    print(df.original_title[df.profit == df.profit.max()], df['profit'].max())
    print(df.original_title[df.profit == df.profit.min()], df['profit'].min())


def gen():
    """ What release is in the most genres  """
    g = df['genres'].str.get_dummies(sep='|')
    gg = g.sum().reset_index()
    print(gg)
    sns.barplot(x=g.columns, y=g.sum(), data=gg)
    plt.title("the most release genres", size=25)
    plt.yticks(size=20)
    plt.xticks(size=20)
    plt.xticks(rotation=90)

    plt.show()


def rate():
    """ the best 10 rate movie """

    R = df['vote_average']
    v = df['vote_count']
    M = v.describe()
    m = M['mean']
    C = R.describe()
    c = C['std']
    r = {}
    r = pd.DataFrame(r)
    r['name'] = df['original_title']
    r['rate'] = (v / (v + m)) * R + (m / (v + m)) * c
    r['vote_average'] = df['vote_average']
    r['vote_count'] = df['vote_count']
    dfs = r.sort_values('rate', ascending=False).head(10)
    sns.barplot(x='rate', y='name', data=dfs)
    plt.yticks(size=20)
    plt.title("the best 10 rate movie", size=25)
    plt.xticks(size=20)
    plt.show()
    print(dfs)


def main():
    rate()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
