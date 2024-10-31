http://127.0.0.1:8000/restaurant/api-token-auth/ #test this out on Insomnia to resgister a user. 
#Enter a username and password and make a POST request to obtain the token.
#Once the token has been created, copy it, 
#and add the details on Insomnia under Bearer to make a GET request to view the menu at:
http://127.0.0.1:8000/restaurant/menu

OR

http://127.0.0.1:8000/auth/users/ #Test this out in the browser to register the user. Then visit:
http://127.0.0.1:8000/auth/token/login/ #Enter the username and password to obtain the token. #Visit:
http://127.0.0.1:8000/restaurant/menu #Click on "Log in" on the top right hand corner and enter #username and password.

#Visit:
http://127.0.0.1:8000/restaurant/booking/tables/ #You can view the reservations or make a #reservation on the browser. If using Insomnia with the POST method, the booking_date must be in #the format: YYYY-MM-DD

Just in case:

little lemon admin:
superuser:
Username: admin
Email: admin@littlelemon.com
Password: lemonAdmin@3!


username: user1
email: user1@littlelemon.com
pass: lemonuser1
auth_token: 7e60eecfac8f45bc2e64466d1c32c4f7ce82e91a

username: user2
email: user2@littlelemon.com
pass: lemonuser2
auth_token: bdca8a651e6daa2572f4b8299694322e0d9c6fe1

MySQL:
'USER': 'root',
'PASSWORD': 'password'
