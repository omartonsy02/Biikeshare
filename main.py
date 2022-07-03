import time
import pandas as pd

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York': 'new_york_city.csv',
             'Washington': 'washington.csv'}
CITIES = ['Chicago', 'New York', 'Washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikers data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city do you want to explore Chicago, New York or Washington? \n> ', )
        if city in CITIES:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('All right! now it\'s time to provide us a month name or just say all to apply no month filter.'
                      ' \n(e.g. all, january, february, march, april, may, june) \n>', )
        if month in MONTHS:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('One last thing. Could you type one of the week day you want to analyze?'
                    ' You can type all again to apply no day filter. \n(e.g. all, monday, sunday)\n>', )
        if day in DAYS:
            break

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]
        # filter by day if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_popular_month = df['month'].value_counts().idxmax()
    print("The most popular month is :", most_popular_month)

    # display the most common day of week
    most_popular_day = df['day_of_week'].value_counts().idxmax()
    print("The most popular day is :", most_popular_day)

    # display the most common start hour
    most_popular_start_hour = df['hour'].value_counts().idxmax()
    print("The most popular start hour is :", most_popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_popular_start_station = df['Start Station'].value_counts().idxmax()
    print("The most popular start station :", most_popular_start_station)

    # display most commonly used end station
    most_popular_end_station = df['End Station'].value_counts().idxmax()
    print("The most popular used end station :", most_popular_end_station)

    # display most frequent combination of start station and end station trip
    most_popular_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most popular used start station and end station : {}, {}"
          .format(most_popular_start_end_station[0], most_popular_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    # display max travel time
    max_travel = df['Trip Duration'].max()
    print("Max travel time :", max_travel)

    print("Travel time for each user type:\n")
    # display the total trip duration for each user type
    group_by_user_trip = df.groupby(['User Type']).sum()['Trip Duration']
    for index, user_trip in enumerate(group_by_user_trip):
        print("  {}: {}".format(group_by_user_trip.index[index], user_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikers users."""

    print('\nCalculating User Stats...\n')
    time.time()

    # Display counts of user types
    print("Counts of user types:\n")
    user_counts = df['User Type'].value_counts()
    # iteratively print out the total numbers of user types
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))


def user_stats_gender(df):
    """Displays statistics of analysis based on the gender of bikers users."""

    # Display counts of gender
    print("Counts of gender:\n")
    gender_counts = df['Gender'].value_counts()
    # iteratively print out the total numbers of genders
    for index, gender_count in enumerate(gender_counts):
        print("  {}: {}".format(gender_counts.index[index], gender_count))

    print("_"*40)


def user_stats_birth(df):
    """Displays statistics of analysis based on the birth years of bikers users."""

    # Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    # the most common birth year
    most_common_year = birth_year.value_counts().idxmax()
    print("The most common birth year:", most_common_year)
    # the most recent birth year
    most_recent = birth_year.max()
    print("The most recent birth year:", most_recent)
    # the most earliest birth year
    earliest_year = birth_year.min()
    print("The most earliest birth year:", earliest_year)
    print("-" * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        user_stats_gender(df)
        user_stats_birth(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
