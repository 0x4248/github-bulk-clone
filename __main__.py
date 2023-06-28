#!/usr/bin/python3
# Github bulk clone
# Quickly Download all of a users or organisations public repository's.
# Github: https://www.github.com/lewisevans2007/github-bulk-clone
# License: GNU General Public License v3.0

import urllib
from urllib import request
import json
import os
import sys
from colorama import Fore, Back, Style
exclude = []
mode = ""
user_list_repo_cache = ""
org_list_repo_cache = ""
def user_list_repo_names(user):
    """Returns a list of the names of the repos owned by user."""
    url = 'https://api.github.com/users/' + user + '/repos'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return [repo['name'] for repo in data]

def org_list_repo_names(org):
    """Returns a list of the names of the repos owned by org."""
    url = 'https://api.github.com/orgs/' + org + '/repos'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode())
    return [repo['name'] for repo in data]

def clone_user(user):
    """Clones the repos owned by user."""
    for i in user_list_repo_names(user):
        if i in exclude:
            continue
        os.system('git clone 

if __name__ == "__main__":
    print("GitHub Bulk Clone Tool")
    mode = "user"
    for i in sys.argv:
        if i.startswith("--exclude="):
            i = i.replace("--exclude=", "")
            for i in i.split(","):
                exclude.append(i)
        elif i == "-o":
            mode = "org"
        elif i == "-u":
            mode = "user"
    if mode == "org":
        try:
            org_list_repo_cache = org_list_repo_names(sys.argv[-1])
        except urllib.error.HTTPError:
            print(Fore.RED+"User not found"+Style.RESET_ALL)
            sys.exit(1)
        print("The organisation "+sys.argv[-1]+" has "+str(len(org_list_repo_cache))+" repos")
        print(Fore.CYAN+"The repos are:"+Style.RESET_ALL)
        for i in org_list_repo_cache:
            print(Fore.GREEN+i,end=" "+Style.RESET_ALL)
        print("\n")
        if len(exclude) > 0:
            print("The repos you want to exclude are:")
            for i in exclude:
                print(Fore.RED+i,end=" "+Style.RESET_ALL)
            print("\n")

        print("Are you sure you want to clone these repos? (y/n)")
        while True:
            ans = input(">")
            if ans == "y":
                break
            elif ans == "n":
                sys.exit(0)
            else:
                print("Please enter y or n")
        clone_org(sys.argv[-1])
    if mode == "user":
        try:
            user_list_repo_cache = user_list_repo_names(sys.argv[-1])
        except urllib.error.HTTPError:
            print(Fore.RED+"User not found"+Style.RESET_ALL)
            sys.exit(1)
        print("The user "+sys.argv[-1]+" has "+str(len(user_list_repo_cache))+" repos")
        print(Fore.CYAN+"The repos are:"+Style.RESET_ALL)
        for i in user_list_repo_cache:
            print(Fore.GREEN+i,end=" "+Style.RESET_ALL)
        print("\n")
        if len(exclude) > 0:
            print("The repos you want to exclude are:")
            for i in exclude:
                print(Fore.RED+i,end=" "+Style.RESET_ALL)
            print("\n")
        
        print("Are you sure you want to clone these repos? (y/n)")
        while True:
            ans = input(">")
            if ans == "y":
                break
            elif ans == "n":
                sys.exit(0)
            else:
                print("Please enter y or n")
        clone_user(sys.argv[-1])
