def the_average_rainfall():
  total_years = int(input("Input the number of years: "))
  total_months = total_years * 12
  total_rainfall = 0

  for year in range(1, total_years + 1):
      for month in range(1, 13):
          rainfall = float(input(f"Input inches of rainfall for Year {year}, Month {month}: "))
          total_rainfall += rainfall

  the_average_rainfall = total_rainfall / total_months

  print(f"\nNumber of months: {total_months}")
  print(f"Total inches of rainfall: {total_rainfall}")
  print(f"The average rainfall per month is: {the_average_rainfall:.2f} inches")


the_average_rainfall()