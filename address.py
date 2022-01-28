# Created by: Zack Isingoma
# Created on: 27th Jan 2022.
# Prints a mailing address for Ontario

def format_address(street_num, street_name, appt_num=None):
    format_address = street_num
    if appt_num is not None:
        format_address = appt_num + " " + street_num
    format_address = street_num + " " + street_name
    return format_address


def main():
    name = input("Enter your first and last name: ")
    question = input("Do you have an apartment: ")
# appartment question
    if question.upper() == 'Y' or question.upper() == 'YES':
        apt_num = input("Enter your apartment number: ")

    street_num = input("Enter your street number: ")
    street_name = input("Enter your street name: ")
    city = input("Enter your city: ")
    province = input("Enter your province 'ON', 'BC': ")
    postal_code = input("Enter your postal code: ")

    if question.upper() == 'N' or question.upper() == 'NO':
        address = format_address(street_num, street_name)
    else:
        address = format_address(apt_num, street_num, street_name)
# output
    print("")
    print("Your canadian mailing address is")
    print(name)
    print(address)
    print(city, province, postal_code)


if __name__ == "__main__":
    main()
