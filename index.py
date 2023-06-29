
import asyncio
from flask import Flask, jsonify, redirect, render_template, request, session
import requests
import json
import os
from colorama import init, Fore

app = Flask(__name__)

app.secret_key = os.urandom(24)
                                 
clientID = os.environ.get('clientID')
secretID = os.environ.get('secretID')
redirectURI = "http://127.0.0.1:2000/redirect.html"

counter=0

"""
    STEP 5:
    Refresh token is needed after 14 days to renew credentials like access token and 
    refresh token. This function going to send a request POST to Access Token Endpoints
    Server to renew credentials that is part of the process of OAuth 2.0 to protect users
    and applications. When you have an invalid token you are going to receive an message 401.
    That is the flag (401) to activate this function get_tokens_refresh (). All this refresh happen
    in the backend.

"""

def get_tokens_refresh():
    print(Fore.YELLOW + "\n+++ Function get_token_refresh() +++\n")
    url = "https://webexapis.com/v1/access_token"
    headers = {'accept':'application/json','content-type':'application/x-www-form-urlencoded'}
    payload = ("grant_type=refresh_token&client_id={0}&client_secret={1}&"
                    "refresh_token={2}").format(clientID, secretID, session['refresh_token'])
    req = requests.post(url=url, data=payload, headers=headers)
    results = json.loads(req.text)
    
    access_token = results["access_token"]
    refresh_token = results["refresh_token"]

    print(Fore.CYAN + "New Access Token: " + access_token)
    print(Fore.CYAN + "New Refresh Token: " + refresh_token)

    session['oauth_token'] = access_token
    session['refresh_token'] = refresh_token

    print(Fore.MAGENTA + "New Token stored as session : " + session['oauth_token'])
    print(Fore.MAGENTA + "New Refresh Token stored as session : " + session['refresh_token'])
    return 

"""
    STEP 4:
    At this moment the parameter code and state is collected previously. In the
    function get_token(code) going to send a POST request to Access Token Server(Cisco)
    in order to get the access token and refresh token.

"""
def get_token(code):
    print(Fore.BLUE + "\n+++ Function get_token(code) +++\n")
    print(Fore.YELLOW + "code:" + code)

    url = "https://webexapis.com/v1/access_token"
    headers = {'accept':'application/json','content-type':'application/x-www-form-urlencoded'}
    payload = ("grant_type=authorization_code&client_id={0}&client_secret={1}&"
              "code={2}&redirect_uri={3}").format(clientID, secretID, code, redirectURI)
    req = requests.post(url=url, data=payload, headers=headers)
    results = json.loads(req.text)
    access_token = results["access_token"]
    refresh_token = results["refresh_token"]

    print(Fore.GREEN + "Access Token: " + access_token)
    print(Fore.CYAN + "Refresh Token: " + refresh_token)

    session['oauth_token'] = access_token 
    session['refresh_token'] = refresh_token

    print(Fore.MAGENTA + "Token stored as session : " + session['oauth_token'])
    print(Fore.MAGENTA + "Refresh Token stored as session : " + session['refresh_token'])
    return render_template("next.html")

"""
    STEP 1:
    That is the initial point for Flow OAuth 2.0
    @app.route('/') is the web page http://127.0.0.1:2000/
    In this point the user going to clic the button "Login with Webex"

"""
@app.route('/')
def home():
    print(Fore.BLUE + "\n+++ Function home() +++\n")
    return render_template('home.html')

"""
    STEP 2:
    The button "Login with Webex redirect to the page "http://127.0.0.1:2000/next.html"
    Funtion next() redirect to the url https://webexapis.com/v1/authorize?...
    Then User introduce credentials in the web page redirected previously 
    from Authorization Endpoints Server(Cisco)

"""
@app.route('/next.html')
def next():
    print(Fore.YELLOW + "\n+++ Function Next() +++\n")
    url = "https://webexapis.com/v1/authorize?client_id=Cb4268541f68984c205305cd19f1ec4769fde9e3142ec03ca8d26f57230704771&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A2000%2Fredirect.html&scope=spark%3Aall%20spark%3Akms&state=set_state_here"
    return redirect(url)
       
"""
    STEP 3:
    After of successful credentials provided to Authorization Endpoint Server
    * The Authorization Endpoint Server redirect to address "http://127.0.0.1:2000/redirect.html"
    where sending a code message and state in the request GET Incomming to Flask.
    The address: http://127.0.0.1:2000/redirect.html is the Redirect URI(s) parameter created
    in the web page Webex for developers https://developer.webex.com/ previously.
    Function get_code() capture the first GET Incomming and collect in var code and state the values,
    However, if comming another request GET that is redirected to the page redirect.html because
    at this point we have the values needed to continue with the flow OAuth 2.0.

"""
@app.route('/redirect.html', methods=['GET'])
async def get_code():
    global counter
    
    try:
        print(f"\033[91m +++ Try +++ = \033[0m", counter)
        if request.method == 'GET' and 'code' in request.args and counter < 1:
            counter = counter + 1
            
            print(Fore.GREEN + "\n+++ Function get_code() +++\n")
            # Get parameters code and state
            code = request.args.get('code')
            state = request.args.get('state')

            # Object JSON is created with parameters code and state
            data = {
                'code': code,
                'state': state
                }

            code = data['code']
            print("Code: ", code)
            state = data['state']
            print("State: ", state)
            await asyncio.sleep(1)
            return get_token(code) 
        else:
            # The credentials we have at this point; other get incoming is not necesary beacuse 
            # We have full acces to request the token from our Access Token Endpoint Server
            return render_template('redirect.html')
    
    except Exception as e:
        return "Error: Ocurrió un problema. Detalles: {}".format(str(e))
"""
    STEP 5:
    In this section we are going to use the access token to send some request GET using
    the function api_call() to get information.
    In that case is getting the Spaces and showed in the portal web spaces.html.
    To generate the GET Request you need to navigate to http://127.0.0.1:2000/spaces.html and
    make clic in the botton Spaces to see all the information collected.:) 

"""
@app.route("/spaces.html",methods=['GET'])
def spaces():
    print(Fore.BLUE + "\n+++ Function spaces() +++\n")
    print("accessing token ...")
    response = api_call()

    print("status code : ", response.status_code)
    # To check on the response if the access_token is invalid then use refresh
    # function get_tokens_refresh() get new access token and refresh token.
    if (response.status_code == 401) :
        get_tokens_refresh()
        response = api_call()

    r = response.json()['items']
    print("response status code : ", response.status_code)
    spaces = []
    for i in range(len(r)) :
        spaces.append(r[i]['title'])

    for space in spaces:
        print(Fore.GREEN + space)
    return render_template("spaces.html", spaces = spaces)

def api_call():
    print(Fore.YELLOW + "\n+++ Funcion api_call() +++\n")
    accessToken = session['oauth_token']
    url = "https://webexapis.com/v1/rooms"
    headers = {'accept':'application/json','Content-Type':'application/json','Authorization': 'Bearer ' + accessToken}
    response = requests.get(url=url, headers=headers)
    print(response.text)
    return response


if __name__ == '__main__':        
    app.run(port=2000, debug=True)
