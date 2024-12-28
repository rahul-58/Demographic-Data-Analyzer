import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # print(df.head())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    df.set_index('race', inplace=True)

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    count_bachelors = df[df['education'] == 'Bachelors'].shape[0]
    total_count = df.shape[0]
    percentage_bachelors = round((count_bachelors / total_count) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = ['Bachelors', 'Masters', 'Doctorate']
    lower_education = [edu for edu in df['education'].unique() if edu not in higher_education]

    higher_education_df = df[df['education'].isin(higher_education)]
    lower_education_df = df[df['education'].isin(lower_education)]

    # percentage with salary >50K
    higher_education_rich = round((higher_education_df[higher_education_df['salary'] == '>50K'].shape[0] / higher_education_df.shape[0]) * 100, 1)

    lower_education_rich = round((lower_education_df[lower_education_df['salary'] == '>50K'].shape[0] / lower_education_df.shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = round(df['hours-per-week'].min(), 1)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round((min_workers[min_workers['salary'] == '>50K'].shape[0] / min_workers.shape[0]) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    earn_above_50k = df[df['salary'] == '>50K']

    total_by_country = df['native-country'].value_counts()

    earn_above_50k_by_country = earn_above_50k['native-country'].value_counts()

    percentage_earn_above_50K = round((earn_above_50k_by_country / total_by_country) * 100, 1)

    highest_earning_country = percentage_earn_above_50K.idxmax()
    highest_earning_country_percentage = percentage_earn_above_50K.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india_earn_50K = earn_above_50k[earn_above_50k['native-country'] == 'India']

    top_IN_occupation = india_earn_50K['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
