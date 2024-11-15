This is an API for a fictional restaurant named "Little Lemon."
The API handles the menu and table bookings for the Little Lemon restaurant.
The API can receive HTTP requests such as GET, POST, PUT and DELETE, and updates the Django models, which in turn, updates the data in a MySQL database.
The application is set up with user registration and authentication.
It also contains unit tests.
Lastly, the API can be tested with the Insomnia REST client.

URLs that can be visited:

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

MySQL:
'USER': 'root',
'PASSWORD': 'password'
