from flask import Flask, request, jsonify

demo_api_controller = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]


def _find_next_id():
    return max(country["id"] for country in countries) + 1


@demo_api_controller.get("/countries")
def get_countries():
    return jsonify(countries)


@demo_api_controller.get("/countries/<int:id>")
def get_id_countries(id):
    for index, countrie in enumerate(countries):
        if countrie['id'] == id:
            return jsonify(countrie), 200
    return {"error": "error"}, 415


@demo_api_controller.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415


@demo_api_controller.delete("/countries/<int:id>")
def delete_country(id):
    for index, country in enumerate(countries):
        if country['id'] == id:
            country.pop(index)
    print(country)
    return {'message': 'success'}, 200


@demo_api_controller.put("/countries/<int:id>")
def put_country(id):
    if request.is_json:
        country_request = request.get_json()
        for index, country in enumerate(countries):
            if country['id'] == id:
                country.update(country_request)
                return jsonify(countries), 200
    return {"error": "error"}, 415


@demo_api_controller.patch("/countries/<int:id>")
def patch_country(id):
    if request.is_json:
        country_request = request.get_json()
        for index, country in enumerate(countries):
            if country['id'] == id:
                country.update(country_request)
                return jsonify(countries), 200
    return {"error": "error"}, 415


if __name__ == '__main__':
    demo_api_controller.run(debug=True)


