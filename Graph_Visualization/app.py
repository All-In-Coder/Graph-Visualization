from flask import Flask, url_for, request, render_template
import graph
import os
import time

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/previous')
def previous():
    hists = os.listdir('static/images')
    hists = ['images/' + file for file in hists]
    if len(hists) == 0:
        error = "You Do not have any Graph"
    else:
        error = ""
    return render_template('previous.html', images=hists, error=error)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/draw')
def draw():
    return render_template('draw.html', error="")


@app.route('/drawG', methods=["POST", "GET"])
def drawG():
    n = request.form["nodes"]
    e = request.form["edges"]
    action = request.form["action"].lower()
    print(action)
    vertices = []

    if action and n and e and request.form["vertices"] and \
            request.form["fileName"]:
        # extracting vertices from the text area....

        for i in request.form["vertices"]:
            if i != '\r':
                if i != '\n':
                    if i != ' ':
                        vertices.append(int(i))

        

        # If number of specified edges are less than given then error.....
        if len(vertices) // 2 != int(e):
            return render_template('draw.html', error="Add all  the edge")

        # Now all the errors are removed, We built are tree...
        fileName = request.form["fileName"]
        source_target = request.form["source_target"]
        graph.newGraph()
        if action == "dfs":
            print("hello")
            build = graph.buildGraph(vertices, fileName, action, int(source_target[0]))
            print(build)
            if build != "Error":
                # time.sleep(2)
                return render_template("show.html", fileName='images/' + fileName + '.png', build=build, check=True)
            else:
                graph.newGraph()
                return render_template("draw.html", error="No Path Between the two")

        elif action == "bfs":

            build = graph.buildGraph(vertices, fileName, action, int(source_target[0]))
            if build != "Error":
                time.sleep(2)
                return render_template("show.html", fileName='images/' + fileName + '.png', build=build, check=True)
            else:
                return render_template("draw.html", error="No Path Between the two")

        elif action == "shortest path":
            build = graph.buildGraph(vertices, fileName, action, int(source_target[0]),
                                     int(source_target[2]))
            if build != "Error":
                time.sleep(2)
                return render_template("show.html", fileName='images/' + fileName + '.png', build=build, check=True)
            else:
                return render_template("draw.html", error="No Path Between the two")

        elif action == "bipartite":
            build = graph.buildGraph(vertices, fileName, action)
            if build:
                time.sleep(2)
                return render_template("show.html", fileName='images/' + fileName + '.png', build=build, check=False)
            else:
                return render_template("draw.html", error="Not a Bipartite")

        elif action == "cycle":
            build = graph.buildGraph(vertices, fileName, action)
            if build != "Not Contain A Cycle":
                return render_template("show.html", fileName='images/' + fileName + '.png', build=build, check=True)
            else:
                return render_template("draw.html", error="Does Not Contain a Cycle")




    else:
        return render_template("draw.html", error="Please Fill all the Details")


app.run(debug=True)
