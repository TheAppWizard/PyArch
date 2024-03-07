


def main():
    
    print("------------------------------------")
    print("Welcome to the Hotel Billing System!")
    print("------------------------------------")
    print("Please enter guest details:")
    guestname = input("Enter your name: ")
    print("Guest name:",guestname)
    
    
    print("------------------------------------")
    print("Please enter Room Details:")
    roomtype = input("Room type (single/double/suite): ")
    print("Your Room Type :",roomtype)
    roomNights = input("Number of Nights: ")
    print("Number of Nights Stayed:",roomNights)
    print("------------------------------------")


    #Argument based function to return room type
    def get_roomprice(roomtype):
        if(roomtype == "single"):
            return 100
        
        elif(roomtype == "double"): 
            return 300
        
        elif(roomtype == "suite"): 
            return 500

    
    
    roomPrice = get_roomprice(roomtype) * int(roomNights)
    print("Room Price",roomPrice,"$")
    print("------------------------------------")
    print("Additional Services:")
    roomLaundry = int(roomNights) * 5
    print("Laundry",roomLaundry,"$")
    roomService = int(roomNights) * 10
    print("Room Service",roomService,"$")
    subtotal = int(roomPrice) + int(roomService) + int(roomNights)
    print("Sub Total",subtotal,"$")
    print("------------------------------------")



    #Percentage Calculation
    def calculate_percentage(value, percentage):
       return (percentage / 100) * value
  

    #10 Percent tax
    tax_percentage = calculate_percentage(subtotal,10)
    
    print("Total Amount Due : ",tax_percentage+subtotal)
    print("------------------------------------")
    print("Thank you for choosing our hotel!")
    print("------------------------------------")


# Main Root
if __name__ == "__main__":
    main()
