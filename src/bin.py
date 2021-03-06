import requests
import argparse
import os,sys


def main(argv=None):

    argv = (argv or sys.argv)[1:]

    parser = argparse.ArgumentParser(description='download .gitignore file from gitignore.io')
    parser.add_argument('language',metavar='language_name',type=str, nargs='+',help='please give the language names')
    args = parser.parse_args(argv)

    url = 'https://www.toptal.com/developers/gitignore/api/'
    url = '.'.join(args.language)

    print(url)
    r = requests.get(url, allow_redirects=True)

    open('.gitignore','wb').write(r.content)
