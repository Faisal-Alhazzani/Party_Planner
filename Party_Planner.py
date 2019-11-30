def party_planner():
    leftovers = 0
    num_each = 0
    while True:
        try:
            cookies = int(input("How many cookies are you baking? "))
            people = int(input("How many people are attending? "))
            num_each = cookies // people
            leftovers = cookies % people
            if people > cookies:
                print("You Should cook cookies equal or more than people attending!")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid input!")
            continue

        except:
            print('please enter a valid number')
            continue

    return(people, num_each, leftovers)



if __name__ == "__main__":
    while True:
        try:
            people, cookies_each, leftovers = party_planner()

            message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
            print(message.format(people, cookies_each, leftovers))
        except:
            continue

        restart = input("\nWould you like to party more? (y or n) \n")

        if restart.lower() == 'n':
            break
