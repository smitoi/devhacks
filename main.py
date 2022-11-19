from app import app

@app.route("/test")
def me_api():
    return {
        "it": "works",
        "foo": True,
        "bar": 0,
    }