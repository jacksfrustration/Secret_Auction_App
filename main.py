logo = '''

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''
winner_logo = '''
              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              /___________\
'''

loop = True
bids = {}
max_bid = 0
while loop:
    print(logo)
    print("Welcome to the secret auction program")
    name = input("What is your name?\n").title()
    bid = float(input("What is your bid?\n"))
    bids[name] = bid
    keep_going = input("Are there any other bidders?\n"
                       "Type 'yes' or 'no'\n").lower()
    if keep_going == "y" or keep_going == "ye" or keep_going == "yes":
        continue
    elif keep_going == "n" or keep_going == "no":
        loop = False
    else:
        print("Wrong input. Restart program")
for item in bids.items():
    if item[1] > max_bid:
        max_bid = item[1]
        winner = item[0]
print(bids)
print(winner_logo)
print(f"Winner was {winner}\n"
      f"They won with a whopping bid of £{max_bid}")


