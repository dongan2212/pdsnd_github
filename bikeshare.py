import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    while True:
        city = input("Input for city (chicago, new york city, washington): ").strip().lower()
        if city in ['chicago', 'new york city', 'washington']:
            return city
        else:
            print("Invalid input city. Please try again.")

def get_month():
    while True:
        month = input("Input for month (all, january, february, ... , june): ").strip().lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            return month
        else:
            print("Invalid input month. Please try again.")

def get_day():
    while True:
        day = input("Input for month (all, monday, tuesday, ... , sunday): ").strip().lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            return day
        else:
            print("Invalid input day. Please try again.")


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington)
    city = get_city()

    # get user input for month (all, january, february, ... , june)
    month = get_month()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = get_day()

    print('-'*60)
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
    # load data file into a dataframe
    file_name = CITY_DATA.get(city)
    if file_name:
        df = pd.read_csv(file_name)
    else:
        print("File not found")

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        index = list(map(lambda x: x.strip().lower(), months)).index(month.strip().lower())
        month_num = index + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month_num]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    month_counts = df['month'].value_counts()
    most_common_month = month_counts.idxmax()
    print("Most Frequent Month: ", most_common_month)

    # Display the most common day of week
    day_counts = df['day_of_week'].value_counts()
    most_common_day_of_week = day_counts.idxmax()
    print("Most Frequent Day: ", most_common_day_of_week)
    
    # Display the most common start hour
    hour_counts = df['hour'].value_counts()
    most_common_hour = hour_counts.idxmax()
    print("Most Frequent Hour: ", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    start_station_counts = df['Start Station'].value_counts()
    most_popular_start_station = start_station_counts.idxmax()
    print("Most Popular Start Station: ", most_popular_start_station)

    # Display most commonly used end station
    end_station_counts = df['End Station'].value_counts()
    most_popular_end_station = end_station_counts.idxmax()
    print("Most Popular End Station: ", most_popular_end_station)

    # Display most frequent combination of start station and end station trip
    trip_counts = df.groupby(['Start Station', 'End Station']).size().reset_index(name='count')
    most_popular_trip = trip_counts.loc[trip_counts['count'].idxmax()]
    print("Most Popular Trip: ", most_popular_trip['Start Station'], "to", most_popular_trip['End Station'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('Calculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_duration = df['Trip Duration'].sum()
    print("Total Trip Duration: ", total_duration)

    # Display mean travel time
    average_duration = df['Trip Duration'].mean()
    print("Average Trip Duration: ", average_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('Calculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("User Type Statistics:")
    print(user_type_counts)

    # Display counts of gender
    if 'Gender' in df.columns:
        print("\nGender Statistics:")
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    else:
        print("\nGender Column not exists!!!")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode().values[0])
        print("\nBirth Year Statistics:")
        print("Earliest Birth Year Statistics: ", earliest_birth_year)
        print("Most Recent Birth Year Statistics: ", most_recent_birth_year)
        print("Most Common Birth Year Statistics: ", most_common_birth_year)
    else:
        print("\nBirth Year Column not exists!!!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('Would you like to restart? Enter yes or no.\n')
        if restart.strip().lower() != 'yes':
            break


if __name__ == "__main__":
	main()
