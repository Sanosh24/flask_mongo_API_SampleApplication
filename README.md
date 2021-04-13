### Restful API with Python-Flask and MongoDB

This is a sample project demonstrated how to design Restful API with Python-Flask and
MongoDB.

First you'll need to get the source of the project. You could do this by cloning the repository:


##### Install dependencies

```python
pip install -r requirements.txt
```

##### Start MongoDB Server

If you're using MacOS, you could use `brew` to start the server.

```bash
brew services start mongodb
```

#### Config the application

Change the `DATABASE_NAME` in the config file according to the database name you are using.

##### Start the application

```bash
python run-app.py
```

Once the application is started, go to [localhost](http://localhost:5000/)
on Postman and explore the APIs.

##### Insert data into database

Url : http://localhost:5000/api/v5/users

##### POST Json Request
```bash
[
   {
      “id”:1,
      “name”:”John”,
       “email”:”John@gmail.com”,
       “phone”:”124-246-5498”,
       “location”:”USA”
  }
]
```
##### Fetch Data from Database

Url : http://localhost:5000/api/v5/users?id=1

##### Update User

Url : http://localhost:5000/api/v5/users/1

##### POST Json Request
```bash
{
	“$set”: {
		“name”:”Peter”
	  }
}
```

##### Delete User

Url : http://localhost:5000/api/v5/users/1

 

