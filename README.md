
# [![image]( https://user-images.githubusercontent.com/38144008/222942190-0b3464ca-a7e4-4ade-9a69-a6c674808467.png)](https://youtu.be/exnjjN5TOOI)
[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/ERICK-ZABALA/AUTOMATING-A-NETWORK-INVENTORY-WITH-PYTHON) [![Run in Cisco Cloud IDE](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://developer.cisco.com/devenv/?id=devenv-vscode-base&GITHUB_SOURCE_REPO=https://github.com/ERICK-ZABALA/AUTOMATING-A-NETWORK-INVENTORY-WITH-PYTHON)

<div align=center>
        <img src="./media/image1.png" style="width:3.63448in;height:3.64827in"
        alt="What is OAuth? Meet this protocol you use so often. - Applications and Systems" />
        <h1> The OAuth 2.0 Authorization for Webex Integrations </h1>
        <p> OAUTH 2.0 </p>
        <p> 2023 </p>
</div>

Authorization framework standard that allows a user to grant a third-party web site or application access to the user's protected and control access to their applications and resources. In the OAuth2 flow, there are typically four parties involved: the user, the client (the application requesting access to the user's resources), the authorization server (responsible for authenticating the user and obtaining their consent), and the resource server (where the user's protected resources are stored).

The OAuth2 protocol works by using access tokens, which are issued by the authorization server after the user grants permission to the client. These access tokens are then presented to the resource server by the client to gain access to the protected resources on behalf of the user. This separation of authorization and resource servers allows for increased security, as the client never directly handles the user's credentials. 

Requirements

1.  Create an account in the portal web Webex for Developers
    <https://developer.webex.com/>.


2.  Create your Webex Apps

<div align=center>
<img src="./media/image2.png"
style="width:5.77844in;height:2.27398in" />

<img src="./media/image3.png" style="width:6.1375in;height:3.18472in" />

<img src="./media/image4.png" style="width:6.1375in;height:3.11319in" />

<img src="./media/image5.png" style="width:6.1375in;height:2.73889in" />

<img src="./media/image6.png" style="width:6.1375in;height:2.89375in" />
</div>

3.  Create a virtual environment in python 3.9 +

> Store the variables using environment variable in your system Linux.
>
> clientID = "Cb4268541f68984c205305cd19f1ecec03ca8d26f57230704771"
>
> secretID = "2826a140ad33730e2ab787a44ca4c714d6cc4cb5896168"
>
> redirectURI = <http://127.0.0.1:2000/redirect.html>
>
> url =
> "https://webexapis.com/v1/authorize?client_id=Cb4268541f68984c205305cd19f1ec4769fde9e26f57230704771&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A2000%2Fredirect.html&scope=spark%3Aall%20spark%3Akms&state=set_state_here"

Process in Linux:

```yaml
 (oauth) devnet@PC1 ~/devnet/webex \$ export secretID="2826a140ffe0643ee2ab787a44ca4c714d6cc4cb5896168" > ~/.bashrc
```

```yaml
 (oauth) devnet@PC1 ~/devnet/webex \$ export clientID="Cb4268541f6898e9e3142ec03ca8d26f57230704771" > ~/.bashrc
```

```yaml
 (oauth) devnet@PC1 ~/devnet/webex \$ source ~/.bashrc
```

```yaml
 (oauth) devnet@PC1 ~/devnet/webex \$ echo $secretID
 2826a140ffe0643eb3a5ad2244ad33730e2ab787a44ca4c714d6cc4cb5896168
 (oauth) devnet@PC1 ~/devnet/webex \$ echo \$clientID
 Cb4268541f68984c205305cd19f1ec4769fde9e3142ec03ca8d26f57230704771
```

4.  Activate Flask in your virtual environment and install the libraries
    listed in requirements.txt

```python
devnet@PC1 ~/devnet/webex \$ python3.10 -m venv oauth

devnet@PC1 ~/devnet/webex \$ source oauth/bin/activate

devnet@PC1 ~/devnet/webex \$pip install -r requirements.txt
```

# Flow OAuth 2.0

<div align=center>
<img src="./media/image7.png" style="width:6.1375in;height:3.16181in" />
        
Figure. Cisco Live – DEVNET 2675

<https://www.ciscolive.com/on-demand/on-demand-details.html?#/video/1687390798629001IngZ>
</div>

<div align=center>
<img src="./media/image8.png" style="width:6.1375in;height:3.92243in"
alt="Build - Login with Webex | Webex for Developers" />
</div>

# Proof of Concept

https://github.com/ERICK-ZABALA/OAUTH2/assets/38144008/16aa3e9f-873b-4cd3-98ce-e7e8bbdc9b62


# References

- Implementing OAuth 2.0 Authorization for Webex Integrations - DEVNET 2675
  
  (https://www.ciscolive.com/on-demand/on-demand-details.html?#/video/1687390798629001IngZ)

- Cisco Developer
  (https://developer.cisco.com/)
