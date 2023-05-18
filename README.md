
# Project Title

KOA Senior Python Engineer Assessment


## Approach 


To solve the task of finding the closest points among a set of points on a grid, the following approach was taken:

Receiving and Parsing Input: The Django application's API endpoint receives a set of points as semicolon-separated values. The input is parsed to extract individual point coordinates.

Calculating Euclidean Distance: The Euclidean distance formula is used to calculate the distance between each pair of points. The formula is applied as follows for two points with coordinates (x1, y1) and (x2, y2):

Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

By calculating the distances between all pairs of points, we obtain a matrix of distances.

Identifying Closest Points: From the distance matrix, the points with the smallest distances are identified as the closest points. For each point, the algorithm finds the point(s) with the minimum distance.

Storing Data: The received set of points and the corresponding closest points are stored in a database using Django's ORM (Object-Relational Mapping) system. A suitable database model is defined to store the point coordinates and their closest points.

By utilizing the Euclidean distance formula, the algorithm determines the closest points among the provided set. The resulting pairs of closest points are then stored in the database for future retrieval and analysis.

## Assumptions 
The input points are in a two-dimensional grid system.
The input points are in a specific format of semicolon-separated values.
The points are to be stored in a MySQL database using Django's default ORM.
## API Reference
The API uses JWT Authentication. Each request needs to be appended with a valid user token in the headers.

#### Get all closest points inserted to dB

```http
  GET /api/closest-points
```

#### Check closest points 

```http
  POST /api/closest-points
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `points`      | `string` | **Required**.A semi-colon list of grid pair coordinates |



#### GET API Token

```http
  POST /api/token
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**.A valid username |
| `password`      | `string` | **Required**.A valid password |
    
## Run Locally

Clone the project

```bash
  git clone repo-url
```

Go to the project directory

```bash
  cd my-project
```

Setup Virtual Environment

```bash
  python -m venv /path/to/new/virtual/environment
```

```bash
  source venv_name/bin/activate
```

Install Dependencies to Virtual Environment

```bash
    pip install -r requirements.txt
```
Setup Database
  Create a database in your local MySQL Environment
  Add the database connections credentials to koapi.settings.py under DATABASES = {}

Run DB migrations

```bash
   python manage.py migrate
```

Create Super User

```bash
   python manage.py createsuperuser
```

Start the server

```bash
  python manage.py runserver
```


## Tech Stack

**Client:** HTML, Javascript, Bootstrap CSS

**API Server:** Python, Django, MySQL


## Testing
You can test the API in 2 different ways

 Running the unit tests

  ```bash
    python manage.py test
  ```
Use a tool like cURL, Postman, or any HTTP client library to send requests to the API endpoints
  If you are using Postman, import the Koa.postman_collection.json file to get started


Developed by,

Gitonga Mwaura - 2023