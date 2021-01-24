from flask import Flask, make_response, render_template

app = Flask(__name__, template_folder='template')
# app.debug = True


@app.route('/')
def index():
    return 'Hello, World!'


@app.errorhandler(404)
def http_404_handler(error):
    return '<i>My custom 404 error </i>', 404


class Route:

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return "This is custom route"


@app.route('/route/<int:route_id>')
def get_route(route_id):
    response = make_response(f'<b>ERROR</b> #{route_id}', 404)
    response.headers['Content-Type'] = 'text/html'
    params = {'route_id': route_id}
    # route_list = [route_id, route_id * 2, route_id * 3]
    return render_template('temp_1.html', route_list=[])


@app.route('/eur_to_usd/<int:amount>')
def eur_to_usd(amount):
    # requests
    # result
    # open file History
    # add row
    # return result
    return


@app.route('/history')
def get_history():
    pass


if __name__ == '__main__':
    # create with name History
    app.run(debug=True)
