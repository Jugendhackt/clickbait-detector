import json
from request_meaningcloud import mc_request
from video_info import video_info
from flask import Flask
from flask import Response
app = Flask(__name__)


@app.route('/id/<id>')
def get_video_name(id):
	vid_i=video_info()
	video_title=vid_i.get_info_form_url("https://www.youtube.com/watch?v="+id)
	return	Response(json.dumps({"clickbait": mc_request(video_title)}), mimetype= 'application/json')


if __name__ == '__main__':
	app.run()
