import sys
import requests
import json


def main(argv):
    url_ = "XXXXX"
    url = url_+"/api/hash"
    p = {"q": argv}
    Response = requests.get(url, params=p)
    print(json.loads(Response.text)["hash"])


if __name__ == '__main__':
    main(input())
