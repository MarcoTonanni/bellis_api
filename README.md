# De Bellis Rei Publicae Romanae Django REST API
## An API serving and managing information about the wars of the Roman Republic

This API was created as a student project for learning and practicing the creation of back-end APIs with Django and Django REST Framework.

Here follows a list of features implemented:

- A REST API using JSON to send and receive data related to the wars of the Ancient Roman Republic, including its battles, commanders and citations from historic sources, with appropriate validations;
- Full CRUD system, based in user and group permissions;
- Extra layer of security based upon token creation and validation;
- Comes with one custom-admin Django command to import CSV lists of Commanders (dates based in the Ad Urbe Condita counting of years in order to bypass Django’s limitation regarding B.C. dates);

It was also deployed in production with [pythonanywhere](www.pythonanywhere.com) and successfully tested with Postman.
