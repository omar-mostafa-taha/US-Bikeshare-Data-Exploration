import time
import pandas as pd
import numpy as np
import sys

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
Months=['January', 'February', 'March', 'April', 'May',  'June' , 'All']
WeekDays=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','All']

def exit_prog(ans):
    if ans.lower()=='exit':
        print('Thank you!')
        sys.exit()


def get_filters():
    while True:
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input("Would you like to view data for new york city , chicago, or washington? ")
        exit_prog(city)
        if city.lower() not in ['washington',"new york city",'chicago']:
            print('Please choose one of the mentioned cities!\n')
            continue
        else:
            break
    while True:
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input("Would you like to view data for January, February, March, April, May, or June or All?")
        exit_prog(month)
        if month.capitalize() not in Months:
            print("Please choose one of the mentioned months!\n")
            continue
        else:
            break
    while True:
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day=input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All?")
        exit_prog(day)
        if day.capitalize() not in WeekDays:
            print("Please make sure you entered a day!\n")
            continue
        else:
            break
    print('-'*40)
    return city , month ,day


def load_data(city,month,day):
    df=pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['Month']=df['Start Time'].dt.month
    df['Day']=df['Start Time'].dt.weekday
    if month.lower()!='all':
        df=df[df['Month']==(Months.index(month.capitalize())+1)]
    if day.lower()!='all':
        df=df[df['Day']==(WeekDays.index(day.capitalize()))]
    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    most_common_month=df['Month'].mode()[0]
    print('The most common Month is: {}'.format(Months[most_common_month-1]))
    most_common_day=df['Day'].mode()[0]
    print('The most common Day is: {}'.format(WeekDays[most_common_day]))
    most_common_hour=df['Start Time'].dt.hour.mode()[0]
    print("The most common Hour is: {}".format(most_common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print('The most commonly used Start Statoin is: {}'.format(start_station))
    # TO DO: display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print('The most commonly used End Statoin is: {}'.format(end_station))
    # TO DO: display most frequent combination of start station and end station trip
    start_end_comb=df[['Start Station','End Station']].mode()
    print('The most frequent combination of start station and end station trip is:\n{}'.format(start_end_comb.iloc[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is: {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The total travel time is: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_counts=df['User Type'].value_counts()
    print("Counts of users types:\n{}".format(type_counts))
    try:
        # TO DO: Display counts of gender
        gender_counts=df["Gender"].value_counts()
        print("\nCounts of users genders:\n{}".format(gender_counts))

        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nThe earliest year of birth is: {}'.format(df['Birth Year'].min()))
        print('The most recent year of birth is: {}'.format(df['Birth Year'].max()))
        print('The most common year of birth is: {}'.format(df['Birth Year'].mode()))
    except:
        print("\nNo available data on users Gender Or Birth Year")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    print('Welcome to US Bikeshare Data Explorer!\nTo end the program type exit')
    
    while True:
        city,month,day=get_filters()
        df=load_data(city,month,day)
        start=0
        while True:
            try:
                choice=int(input('Press:\n1 ==> to view Time Statistics \n2 ==> to view Station Statistics\n3 ==> to view Trip Duraiton Statistics\n4 ==> to view Users Statistics\n5 ==> to veiw all the Statistics\n6 ==> to see five lines of raw data \n7 ==> to exit\nYour Choice: '))
            except:
                print('Please Enter a number!')
                continue
            print('-'*40)
            
            if choice==1:
                time_stats(df)
            elif choice==2:
                station_stats(df)
            elif choice==3:
                trip_duration_stats(df)
            elif choice==4:
                user_stats(df)
            
            elif choice==5:
                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df)
            elif choice==6:
                if (df.shape[0]-start)<5:
                    print(df.iloc[start:,:])
                else:
                    print(df.iloc[start:start+5,:])
                if (start+5)==df.shape[0]:
                    print('you reached the end of the data set!')
                else:
                    start+=5
                    
                
            elif choice==7:
                break
            else:
                print("Invalid input!")
                
        
        user_input=input('Type Yes if you wanted to Explore another city and anything else if you wanted to exit: ')
        if user_input.lower()!='yes':
            print('Thank you!')
            break
        
if __name__ == "__main__":
	main()
