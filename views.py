from flask import render_template, request, Blueprint
from wordle_solver import play_on_browser as pob

views = Blueprint(__name__, "views")


@views.route("/", methods=["post", "get"])
def index():
	return render_template('index.html')


@views.route("/search", methods=["post", "get"])
def search():
	form = request.form
	word = form["wordleword"]
	eletters = form["excluded-letters"]
	iletters = form["included-letters"]
	word_list = pob(word, eletters, iletters, 800)
	return render_template('words.html', word_list=word_list)