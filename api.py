from bottle import Bottle, run, request, response

app = Bottle()

@app.route('/prompt', method='GET')
def prompt():
    prompt = request.query.get('prompt')
    model = request.query.get('model')
    repeat = request.query.get('repeat')

    if not prompt or not model or not repeat:
        response.status = 400
        return {'error': 'Missing parametr'}

    response.content_type = 'application/json'
    with open('prompt.txt', 'a') as file:
        file.write(f'{prompt};{model};{repeat}\n')

    return {'status':'added to que'}

@app.route('/status', method='GET')
def status():
    response.content_type = 'application/json'
    with open('prompt.txt', 'r') as file:
        first_line = file.readline().strip()
        if first_line == "1":
            return {'status':'generating'}
        else:
            return {'status':'waiting'}
    

if __name__ == "__main__":
    run(app, host='localhost', port=8000)
