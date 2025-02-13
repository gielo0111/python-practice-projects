from fastapi import FastAPI

app= FastAPI()



# Now point your browser to localhost:5000/api/docs/

@app.post("/get-user/{user_id}")
def get_user(user_id):

    user_data = {
        "user_id": user_id,
        "name": "Gielo Joseph Fernandez",
        "email": "gielo0111@gmail.com"
    }
    extra = request.args.get('extra')
    if extra:
        user_data["extra"] = extra
    return user_data, 200


if __name__ == "__main__":
    app.run(debug=True)
