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
    print('Hey there, welcome! Let\'s explore some US bikshare data.')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city would you like to analyze?\n Chicago, New York City or Washington\n').lower()
        if city not in ('chicago', 'new york city','washington'):
           print('Your city selection was not recognized. Please try again.')
           continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to analyze?\n January, February, March, April, May, or June\n').lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june'):
            print('Your month selection was not recognized. Please try again.')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('What day of the week would you like to analyze?\n Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n').lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('Your weekday selection was not recognized. Please try again.')
            continue 
        else:
            break

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['weekday'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().keys()[0]
    print(f'The most common month is {common_month}')
    

    # TO DO: display the most common day of week
    common_day = df['weekday'].value_counts().keys()[0]
    print(f' THe most common day of the week is {common_day}')

    # TO DO: display the most common start hour
    hour = df['Start Time'].value_counts().keys()[0]
    common_hour = str(hour)[11:13]
    print(f'The most common start hour is {common_hour}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].value_counts().keys()[0]
    count_start = df['Start Station'].value_counts().tolist()[0]
    print(f'The most commonly used Start Station is {popular_start} with count {count_start}.')


    # TO DO: display most commonly used end station
    popular_end = df['End Station'].value_counts().keys()[0]
    count_end = df['End Station'].value_counts().tolist()[0]
    print(f'The most commonly used End Station is {popular_end} with count {count_end}.')


    # TO DO: display most frequent combination of start station and end station trip
    df['Combination of Stations'] = df['Start Station'] + ' ' + df['End Station']
    popular_combination = df['Combination of Stations'].value_counts().keys()[0]
    count_combination = df['Combination of Stations'].value_counts().tolist()[0]

    print(f'The most frequent combination is {popular_combination} with count {count_combination}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    seconds = df['Trip Duration'].sum()
    print(f' The total travel time is {seconds:.0f} seconds.')

    # TO DO: display mean travel time
    mean_seconds = df['Trip Duration'].mean()
    print(f' The mean travel time is {mean_seconds:.0f} seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

 
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().keys()
    count_users = df['User Type'].value_counts().tolist()
    users_count = dict(zip(user_types,count_users))
    print(users_count)

    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts().keys()
        other_genders = df['Gender'].value_counts().tolist()
        genders_count = dict(zip(genders,other_genders))
        print(genders_count)
    except: 
        print('There is no gender count for this column.')
 
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].value_counts().keys()[0]
        print(f'The earliest birth year is {earliest}')
        print(f'The most recent birth year is {recent}')
        print(f'The most common birth year is {common}')
    except:
        print('There is no birth year for this column.')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        counter1 = 0
        counter2 = 0
        while True:
          raw_data = input('\nDo you want to see raw data? Enter yes or no.\n')
          raw_data = raw_data.lower() 
          if raw_data == 'yes':
            print(df.iloc[counter1:counter2])
            counter1 = counter1 + 5
            counter2 = counter2 + 5
            break
          else:
            break
  

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            restart_sure = input('Are you sure you\'d like to exit? Enter yes or no.\n')
            if restart_sure == 'yes':
                break
            

if __name__ == "__main__":
	main()
