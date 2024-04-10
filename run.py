from App import app  # Make sure the import path is correct
from waitress import serve

if __name__ == "__main__":
<<<<<<< HEAD
    serve(app, host='0.0.0.0', port=5000, threads=2)
    #app.run(debug=True)
=======
 serve(app, host='0.0.0.0', port=5000, threads=2)
  #  app.run(debug=True)
>>>>>>> e31be86d8861b08da3b951f919ac3aed360ba2d9
