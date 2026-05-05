for _ in range(3):
  a = int(input("Enter your lucky number between 1 to 20: "))

  match a:
      case 1:
            print("you won rs 22")
      case 2:
            print("you won rs 56")
      case 6:
            print("you won rs 787")
      case _:
            print("better luck next time")
 