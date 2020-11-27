URL shortening application:

Tools Used: 
Flask, Python, MongoDB, Docker

Description: 
The application returns a shortened URL which redirects to the original URL that is sent as a message body to the server. 
The docker container uses a pre-existing mongo image on Docker Hub as a database to connect to the flask application.
The flask application runs on port 5000 and mongo runs on port 27017.

How to run from this directory:
1. docker-compose build
2. docker-compose up
3. On a separate terminal, use HTTP POST commands to localhost:5000/submit to submit an URL and retrieve the shortened URL(curl examples shown below).
4. Visiting the provided shortened URL redirects to the original URL sent to the server.


Examples:

curl -i -H "Content-Type: application/json" -X POST -d '{"body":"https://www.youtube.com/watch?v=RmvZyC6s_Wk"}' http://localhost:5000/submit
curl -i -H "Content-Type: application/json" -X POST -d '{"body":"https://www.youtube.com/watch?v=2f1PtJV0vIs"}' http://localhost:5000/submit



