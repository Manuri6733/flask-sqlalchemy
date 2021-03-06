from movies import *
# route to get all movies
@app.route('/')
def a():
    return 'Movies'
@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({'Movies': Movie.get_all_movies()})
# route to get movie by id
@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)

# route to add new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    request_data = request.get_json()  # getting data from client
    Movie.add_movie(request_data["title"], request_data["year"],
                    request_data["genre"])
    response = Response("Movie added", 201, mimetype='application/json')
    return response
# route to update movie with PUT method
@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    request_data = request.get_json()
    Movie.update_movie(id, request_data['title'], request_data['year'],                                      request_data['genre'])
    response = Response("Movie Updated", status=200, mimetype='application/json')
    return response
# route to delete movie using the DELETE method
@app.route('/movies/<int:id>', methods=['DELETE'])
def remove_movie(id):
    '''Function to delete movie from our database'''
    Movie.delete_movie(id)
    response = Response("Movie Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(debug=True)