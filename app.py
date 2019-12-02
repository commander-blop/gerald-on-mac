@app.route('/' ,methods=["GET"])
gef getMethod():
  return "GET METHOD"
  
@app.route('/init, methods=["POST"])
def receiveCommand():
  print("Connection Successful")
  return "Connection okay"
