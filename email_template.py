import datetime
import sys

now = datetime.datetime.now()
current_hour = now.strftime("%H")

# address format -  10289 Ulmerton Rd,UNIT RIGHT,LARGO,FL 33771,US


def main():
    validate_sys_args()
    email_template(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


def email_template(ticket, number, address, cause):
    if "US" in address:
        address = address.split(",")
        street = address[0].strip()
        # sub_unit = address[1]
        sub_unit = ""
        city = address[2].title()
        print(city)
        state_zip_split = address[3].split(" ")
        state = state_zip_split[0].strip()
        zip_code = state_zip_split[1].strip()
        if str(sub_unit) == "":
            address = (
                street.title()
                + ", "
                + city.title()
                + ", "
                + state.upper()
                + ", "
                + zip_code
            )
        else:
            address = (
                street.title()
                + ", "
                + sub_unit.capitalize().strip()
                + ", "
                + city.titel()
                + ", "
                + state.upper()
                + ", "
                + zip_code
            )

    # country = address[4] not needed
    else:
        # 54 GLENMAURA NATIONAL BLVD, MOOSIC, PA
        address = address.split(",")
        street = address[0].strip()
        # sub_unit = address[1]
        city = address[1].strip()
        zip_code = address[2].strip()

        address = street.title() + ", " + city.title() + ", " + zip_code.strip()

    if 0 < int(current_hour) < 12:
        greeting = "Good Morning,"
        time_of_day = "this morning"
    elif 12 < int(current_hour) < 18:
        greeting = "Good Afternoon,"
        time_of_day = "this afternoon"
    elif 18 < int(current_hour) < 24:
        greeting = "Good Evening,"
        time_of_day = "this evening"
    else:
        greeting = "Greetings,"
        time_of_day = "today"

    print(
        f"\n\nSUBJECT LINE == {ticket} || {number} || {address}\n\n\n{greeting}\n\nOur system received an alert for the following network device. Ticket {ticket} || {number} || {address}  was ({cause}) automatically created {time_of_day} as part of the monitoring, I ensured your site was connected and continued to monitor the site for four (4) hours verifying there were not additional issues. I will be closing ticket {ticket}, please let me know if you have any questions.\n"
    )

    print(
        f"\n\nSUBJECT LINE == {ticket} || {number} || {address}\n\n\n{greeting}\n\nTicket {ticket} Site: {number} Reason: {cause}. Issue recovered was automatically created {time_of_day} as part of the monitoring, I ensured your site was connected and continued to monitor the site for 4 hours ensuring no issue. I will be closing ticket {ticket} now, please let me know if you have any questions.\n"
    )


def validate_sys_args():
    # argvs have no file formats

    sys_argv_length = len(sys.argv)

    if sys_argv_length == 5:  # too few argvs
        return sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    else:
        sys.exit(
            "\nThis requires five (5) CLI argurements, including the file ("
            + sys.argv[0]
            + " ticket number address cause). Address requires 'address' or \"address\" (i.e) '123 Main Ave,,City,FL 90909,US'. Same for Cause (i.e. 'Subject - Issue')\n"
        )


if __name__ == "__main__":
    main()
