# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                                   #
#   A simple script which scans a website using a common directory list and returns all discovered directories.     #
#                                                                                                                   #
#   Author: Tyler Hooks                                                                                             #
#                                                                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from requests import head
import re

website = ""
with open("directories.txt") as directories:
    for d in directories:
        try:
            url = "{0}/{1}".format(website, d.strip())
            response = str(head(url))
            if re.search("2\d{2}", response):
                print("[*] DIRECTORY FOUND: %s" % url)
            else:
                continue
        except Exception as e:
            print(e)

