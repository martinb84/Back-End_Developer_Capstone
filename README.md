http://127.0.0.1:8000/restaurant/api-token-auth/ #test this out on Insomnia to resgister a user. 
#Enter a username and password and make a POST request to obtain the token.
#Once the token has been created, copy it, 
#and add the details on Insomnia under Bearer to make a GET request to view the menu at:
http://127.0.0.1:8000/restaurant/menu

OR

http://127.0.0.1:8000/auth/users/ #Test this out in the browser to register the user. Then visit:
http://127.0.0.1:8000/auth/token/login/ #Enter the username and password to obtain the token. Visit:
http://127.0.0.1:8000/restaurant/menu #Click on "Log in" on the top right hand corner and enter username and password.

