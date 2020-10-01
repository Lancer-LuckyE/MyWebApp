# MyWebApp
This is a authentication demo implemented with Vue.js and Flask.
The front-end app uses Vue.js and Bootstrap.
The back-end app uses Flask and postgres database and encrypts the password with bcrypt python lib.

Flask api returns different http codes to help front-end app filter some known errors such as duplicate user account.
The api is following RESTful api style, although There are only a few apis are implemented.
