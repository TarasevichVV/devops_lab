#!/usr/bin/env python
import argparse
import getpass
import requests


class variables:
    git_url = "https://api.github.com"
    login = "TarasevichVV"
    password = getpass.getpass()


parser = argparse.ArgumentParser()
parser.add_argument("--version", action="version", version="v0.0.1")
parser.add_argument("-owner", nargs=1, help="enter a repo owner", required=True)
parser.add_argument("-repo", nargs=1, help="enter a repo name", required=True)
parser.add_argument("-pull_number", nargs=1, help="enter a pull number")
parser.add_argument("-pulls", help="use for take info about pull request", action="store_true")
parser.add_argument("-files", help="use for take info about files info"
                                   "(you mast enter pull_number first!)",
                    action="store_true")
parser.add_argument("-commits", help="use for take info about commits info(you mast "
                                     "enter pull_number first!)",
                    action="store_true")
args = parser.parse_args()


def pulls():
    pulls = requests.get(
        variables.git_url + '/repos/' + args.owner[0] + '/' + args.repo[0] + '/pulls',
        auth=(variables.login, variables.password))
    return pulls.json()


def files():
    files = requests.get(
        variables.git_url + '/repos/' + args.owner[0] + '/' + args.
        repo[0] + '/pulls/' + args.pull_number[0] + '/files',
        auth=(variables.login, variables.password))
    return files.json()


def commits():
    commits = requests.get(
        variables.git_url + '/repos/' + args.owner[0] + '/' + args.
        repo[0] + '/pulls/' + args.pull_number[0] + '/commits',
        auth=(variables.login, variables.password))
    return commits.json()


if args.pulls:
    data_pulls = pulls()
    for i, j in enumerate(data_pulls):
        print(data_pulls[i]["title"], data_pulls[i]["created_at"], data_pulls[i]["state"])
elif args.commits:
    data_commits = commits()
    for item in data_commits:
        dict = {'Commit1': item.get('commit').get('author').get('name'),
                'Commit2': item.get('commit').get('author').get('email'),
                'Commit3': item.get('commit').get('author').get('date')}
        for i in dict:
            print(dict[i])
elif args.files:
    data_files = files()
    for i, j in enumerate(data_files):
        print(data_files[i]["filename"], data_files[i]["status"], "additions - ",
              data_files[i]["additions"], "deletions - ", data_files[i]["deletions"])
else:
    print("No input")
