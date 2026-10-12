from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
import phonenumbers
import os, sys
import time

number = input('\n[+] Enter Phone Number to Analyze: ')

os.system("cls")

# banner starts
print('''
    ############################################################
    #                                                          #
    # ██╗███╗   ██╗██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗ #
    # ██║████╗  ██║██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝ #
    # ██║██╔██╗ ██║██████╔╝███████║██║   ██║██╔██╗ ██║█████╗   #
    # ██║██║╚██╗██║██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝   #
    # ██║██║ ╚████║██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗ #
    # ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ #
    #                                                          #
    #                                                          #
    # Author: answ3r                                           #
    # Team: Oraculus                                           #
    #                                                          #
    ############################################################
''')
# banner ends

print('[-] Analyzing...')
time.sleep(2)

try:
    parser = phonenumbers.parse(number, None)
except Exception as e:
    print('[!] Error:', e)
    sys.exit(1)

inter_format = phonenumbers.format_number(parser, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
print('\n[*] Phone Number:', inter_format)

possible = phonenumbers.is_possible_number(parser)
print('\n[*] Possible:', possible)

valid = phonenumbers.is_valid_number(parser)
print('[*] Valid:', valid)

nat_format = phonenumbers.format_number(parser, phonenumbers.PhoneNumberFormat.NATIONAL)
print('[*] National Format:', nat_format)

typelist = ['Fixed-line', 'Mobile', 'Toll-free', 'Premium Rate', 'Shared Cost', 'VoIP', 'Personal Numbers', 'UAN', 'Pager', 'Voicemail']

tp = phonenumbers.number_type(parser)
print('[*] Type:', typelist[tp])

geo = geocoder.description_for_number(parser, "en")
print('[*] Position (if localizable):', geo)

tz = timezone.time_zones_for_number(parser)
print('[*] Timezone(s):', tz)

car = carrier.name_for_number(parser, "en")
print('[*] Carrier:', car)

time.sleep(1)
print('\n[-] Scan Completed')
