
# Project Title

KOA Senior Python Engineer Assessment


## Demo

Insert gif or link to demo


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


## Deployment

The API is deployed on an AWS EC2 instance
    
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
Run DB migrations

```bash
    pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```


## Tech Stack

**Client:** HTML, Javascript, Bootstrap CSS

**API Server:** Python, Django, MySQL

