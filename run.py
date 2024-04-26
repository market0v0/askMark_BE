from App import app  # Make sure the import path is correct
from waitress import serve

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000, threads=2)
    # app.run(debug=True)