def calculate_the_points_awarded():
  books_purchased = int(input("Input the number of books purchased in this month: "))

  if books_purchased == 0:
      points = 0
  elif 2 <= books_purchased <= 3:
      points = 5
  elif 4 <= books_purchased <= 5:
      points = 15
  elif 6 <= books_purchased <= 7:
      points = 30
  elif books_purchased >= 8:
      points = 60
  else:
      points = 0  # Default 

  print(f"\nPoints awarded: {points}")

calculate_the_points_awarded()