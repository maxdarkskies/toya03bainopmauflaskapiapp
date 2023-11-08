"""
00 fork this replit to your replit 

01a do your code
01b your final goal is to hit Run and have all tests PASS IN GREEN

02a git commit push to github repo - view guide https://drive.google.com/file/d/1PZZ2xIlamM0pPtLlbpDodseCKcIVhTzW/view?usp=sharing
02b get url to your git repo in 02a above - we call it :gitrepourl

03 paste :gitrepourl into this google form and submit it
   https://forms.gle/cuxhb8cbYaJLHRYz5
   ma_debai = toya03bainopmauflaskapiapp
"""

from flask import Flask, jsonify, request
import requests
import os
#
from src.helper import github_request

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))


@app.route("/", methods=["GET"])
def index():
  return jsonify({})


@app.route('/release', methods=["GET"])
def release():
  url = "https://api.github.com/repos/pyenv/pyenv/releases"
  response = requests.get(url)
  if response.status_code == 200:
    releases = response.json()
    result = []
    for release in releases:
      release_info = {
          "created_at": release["created_at"],
          "tag_name": release["tag_name"],
          "body": release["body"],
      }
      result.append(release_info)
    return jsonify(result)
  else:
    return jsonify({}), 404


@app.route('/most_3_recent/release', methods=["GET"])
def most_3_recent__release():
  url = "https://api.github.com/repos/pyenv/pyenv/releases"
  response = requests.get(url)
  if response.status_code == 200:
    releases = response.json()
    releases.sort(key=lambda x: x["created_at"], reverse=True)
    most_recent_releases = releases[:3]
    result = []
    for release in most_recent_releases:
      release_info = {
          "created_at": release["created_at"],
          "tag_name": release["tag_name"],
          "body": release["body"],
      }
      result.append(release_info)
    return jsonify(result)
  else:
    return jsonify({}), 404


if __name__ == '__main__':
  app.run(debug=True, port=os.environ.get('PORT', 5000))
