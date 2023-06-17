import datetime
import sys


now = datetime.datetime.now()
current_hour = now.strftime("%H")

# address format -  10289 Street Rd,sub address,City,FL 90001,US
# whole example -  ticket_code device_number '123 Main Rd, sub address, the city, IL 90001' 'cause type - unplugged'

"""opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]"""


def main():
    ...
    validate_sys_args()

    # email_template(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    # email_template()
    print(sys.argv[1])
    if sys.argv[1] == "-a":
        email_template(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif sys.argv[1] == "-s":
        email_template(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif sys.argv[1] == "-m":
        email_template(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    else:
        raise SystemExit(
            f"Usage: {sys.argv[0]} (-a | -s | -m) <arguments>...\n\n-a: Advanced SDWAN\n-s: Standard SDWAN\n-m: Managed Router\n\n"
        )


def email_template(type, ticket, device_number, address, cause):
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
        state_zip_split = address[2].split(" ")
        zip_code = state_zip_split[2]
        if zip_code.isnumeric():
            pass

        else:
            # city = address[1].strip()
            city = address[2].strip()
            # zip_code = address[3].strip()
            state_zip_split = address[3].split(" ")
            zip_code = state_zip_split[2]
            """            print(city + "\n")
            # print(city2+"\n")
            print(zip_code + "\n")
            print("there is more to the address")"""

        address = street.title() + ", " + city.title() + ", " + zip_code.strip()

    if 0 < int(current_hour) < 12:
        greeting = "Good morning,"
        time_of_day = "this morning"
    elif 12 < int(current_hour) < 18:
        greeting = "Good afternoon,"
        time_of_day = "this afternoon"
    elif 18 < int(current_hour) < 24:
        greeting = "Good evening,"
        time_of_day = "this evening"
    else:
        greeting = "Greetings,"
        time_of_day = "today"

    if type == "-a":
        print(
            f"\n\nSUBJECT LINE == Proactive Monitoring {ticket} || {device_number} || {address}\n\n\n{greeting}\n\nOur proactive monitoring system received an alert for the following network device. Ticket {ticket} || {device_number} || {address}  was (Advanced SDWAN - {cause}) automatically created as part of proactive monitoring, I ensured your site was connected and continued to monitor the site for four (4) hours verifying there were no additional issues. I will be closing ticket {ticket}, please let me know if you have any questions.\n"
        )
    elif type == "-s":
        print(
            f"\n\nSUBJECT LINE == Proactive Monitoring {ticket} || {device_number} || {address}\n\n\n{greeting}\n\nOur proactive monitoring system received an alert for the following network device. Ticket {ticket} || {device_number} || {address}  was (Standard SDWAN - {cause}) automatically created as part of proactive monitoring, I ensured your site was connected and continued to monitor the site for four (4) hours verifying there were no additional issues. I will be closing ticket {ticket}, please let me know if you have any questions.\n"
        )
    elif type == "-m":
        print(
            f"\n\nSUBJECT LINE == Managed Router {ticket} || {device_number} || {address}\n\n\n{greeting}\n\nTicket {ticket} Site: {device_number} Reason: Managed Router - {cause} was automatically created as part of proactive monitoring, I ensured your site was connected and continued to monitor the site for 4 hours ensuring no additional issues. I will be closing ticket {ticket} now, please let me know if you have any questions.\n"
        )
    else:
        pass


def validate_sys_args():
    # argvs have no file formats

    sys_argv_length = len(sys.argv)

    if sys_argv_length == 6:  # too few argvs
        for _ in sys.argv:
            print(_)
        return sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]

    else:
        sys.exit(
            f"\nUsage: {sys.argv[0]} (-a | -s | -m) <arguments>\n\n-a: Advanced SDWAN\n-s: Standard SDWAN\n-m: Managed Router\n\nThis requires five (6) CLI argurements, including the file ({sys.argv[0]}, system type, ticket, device_number, address, and cause). Address requires ' or \" ('address' or \"address\"). The address must also follow the following formatting: Splunk - '10289 stree Rd,UNIT RIGHT,Redlands,FL 90001,US' where the sub adress (Unit is optional -- UNIT RIGHT); BPOM -  '42142 street DR, redlands, CA' with no additional options. The cause also requires ' or \" ('cause' or \"cause\")  (i.e. 'Intermittent Connectivity (Hard Down)')\n\nComplete example: {sys.argv[0]} -m ticket_code device_number '123 Main Rd, sub address, the city, IL 90001' 'cause type - unplugged'\n"
        )


if __name__ == "__main__":
    main()
