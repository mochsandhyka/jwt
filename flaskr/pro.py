from configuration import app,jwt_required,get_jwt_identity

@app.route("/protected")
@jwt_required()
def protected():
    a = get_jwt_identity()
    return a