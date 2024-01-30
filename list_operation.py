class InvalidListSize(Exception):
    "Raised when the input string length is not a multiple of 10"
    pass
def process_user_list(input):
    try:
        user_list = input.split()
        size=len(user_list)
        if (size%10!=0 or size==0) :
            raise InvalidListSize
        else:
            for i in range(size):
            # convert each item to int type
                user_list[i] = int(user_list[i])
            #remove values from indices which are multiple of 2 or 3
            new_list = [value for index, value in enumerate(user_list) if (index + 1) % 2 != 0 and (index + 1) % 3 != 0]
            print("New  list :",new_list)

    except InvalidListSize:
     print("List size is not a multiple of 10")
    except ValueError:
        print("The input was not a valid integer.")
     
input_string = input('Enter elements of a list separated by space :\n')
process_user_list(input_string)
