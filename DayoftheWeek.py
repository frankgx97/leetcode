class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        '''
        ac
        calculate total days passed from 1970-1-1(Fri)
        then %7 to determine the weekday
        '''
        num_leap_years = (year - 1969) // 4
        full_year_days = (year - 1971) * 365 + num_leap_years
        full_month_days = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] # len is 13
        total_days = full_year_days + full_month_days[month] + day
        if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)) and month > 2:
            total_days +=1
        weekdays = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        return weekdays[total_days % 7 - 1]
