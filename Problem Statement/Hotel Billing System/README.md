# Hotel Billing System

This is a Python-based hotel billing system designed to automate the billing process for guests staying at a hotel. The system calculates the total bill for each guest based on their room charges, additional services requested, and any applicable taxes.

## Requirements

1. **User Input**: The system should prompt the user to input details such as guest name, room type, number of nights stayed, and additional services requested.
2. **Room Types and Rates**: Predefined list of room types with corresponding nightly rates should be provided.
3. **Additional Services**: Predefined prices associated with additional services should be available.
4. **Total Bill Calculation**: The system should calculate the total bill for the guest, including room charges, additional service charges, and applicable taxes.
5. **Itemized Bill**: Display an itemized bill including room charges, additional service charges, taxes, and total amount due.
6. **Error Handling**: Gracefully handle invalid inputs and provide appropriate error messages.
7. **Printing/Save Option**: Provide an option for the user to print or save the bill.
8. **Multiple Guests**: The system should allow for multiple guests to be billed sequentially.

## Implementation

- **Modularization**: Use of functions to improve code readability and organization.
- **Data Storage**: Utilize dictionaries or classes to store room types, rates, additional services, and prices.
- **Error Handling**: Implement error handling to prevent program crashes due to incorrect inputs.
- **User-Friendly Interface**: Clear prompts and informative messages should be displayed.

## Example Output
```
Welcome to the Hotel Billing System!

Please enter guest details:
Guest name: John Doe
Room type (single/double/suite): double
Number of nights stayed: 3
Additional services (comma-separated, leave blank for none): room service, laundry

Itemized Bill for John Doe:

Room Charges (double room, 3 nights): $300
Additional Services:

Room Service: $20
Laundry: $15
Subtotal: $335
Taxes (10%): $33.50

Total Amount Due: $368.50

Thank you for choosing our hotel!

```


