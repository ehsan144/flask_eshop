from flask import Flask
from .routes import bp

app = Flask(__name__)
# Configurations
app.debug = True


app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)