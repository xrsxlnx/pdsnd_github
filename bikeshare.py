#This script will be used for Udacity Git project

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Choose and type a city for - Chicago, New York city or Washington: ').lower()
    while city not in ('chicago', 'new york city', 'washington'):
        print('Your input is incorrect')
        city = input('Choose and type a city for - Chicago, New York city or Washington: ').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Choose and type a month for - all, january, february, ... , june: ').lower()
    while month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        print('Your input is incorrect')
        month = input('Choose and type a month for - all, january, february, ... , june: ').lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Choose and type a day for - all, monday, tuesday, ... sunday: ').lower()
    while day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        print('Your input is incorrect')
        day = input('Choose and type a day for - all, monday, tuesday, ... sunday: ').lower()


    print('-'*40)
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
    raw_data = input('If you want to see 5 lines of raw data, enter "yes" or "no" to skip the step\n').lower()
    start_row = 0
    end_row = 5
    while raw_data != 'no':
        print(df.iloc[start_row : end_row])
        raw_data = input('If you want to see next 5 lines of raw data, enter "yes" or "no" to skip\n').lower()
        start_row += 5
        end_row += 5


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    #print(df['month'])
    #print(df['day'])



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(common_month))


    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('The most common day of week is: {}'.format(common_day))


    # TO DO: display the most common start hour
    #df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is: {}'.format(common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(common_start_station))


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    frequent_start_end_stations = (df['Start Station'] + ' --- ' + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip is: {}'.format(frequent_start_end_stations))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    #start_hour_in_minutes = (df['Start Time'].dt.hour)*60 + df['Start Time'].dt.minute
    #end_hour_in_minutes = (df['End Time'].dt.hour)*60 + df['End Time'].dt.minute

    print('Total travel time is: {}'.format(total_travel_time))


    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time is: {}'.format(average_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print('Counts of user types are: \n', user_types_count)
    print()



    # TO DO: Display counts of gender
    gender_types_count = df['Gender'].value_counts()
    print('Counts of gender are: \n', gender_types_count)
    print()


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year = df['Birth Year'].min()
    most_recent_year = df['Birth Year'].max()
    common_year = df['Birth Year'].mode()[0]
    print('The earliest year of birth is: {} \nThe most recent year of birth is: {} \nThe most common year of birth is: {}'.format(earliest_year, most_recent_year, common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)
        else:
            print('Washington city does not contain Gender and Birth Year columns')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
