# Avtaar Assignment 3

## DB and REST API for User-Events

##### Stack used Flask, MySQL, Postman
---

## Getting Started

### Dependencies
1. Python version 3.6 or above [Download](https://www.python.org/downloads/)
2. Postman (For API Testing and Development) [Download](https://www.postman.com/downloads/)
3. MySQL (For Creating User and Event Data in Database Through API) [Download](https://dev.mysql.com/downloads/mysql/)

### Installing

1. Clone the repo

   ```
   git clone https://github.com/AJ-Walker/Avtaar-Assignment-3.git 
   ```
   
2. Create virtual environment

   ```
   # On Linux/Mac
   python3 -m venv venv
   
   # On Windows
   python -m venv venv
   ```

3. Activate virtual environment

   ```
   # On Linux/Mac
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

4. Install Packages for running this API

   ```
   pip install -r requirements.txt
   ```

5. Open MySQL Command line Client, Create DATABASE for Creating Table and Inserting Into Table.

   ```sql
   CREATE DATABASE <your-database-name>;
   ```

### Executing the API

1. Open a terminal or command prompt (cmd)

   ```
   python app.py 
   ```
   
2. Open Postman for testing API

### API Documentation

**Create User**
---

Create a user in database and returns a JSON success message

* **URL**

  /api/user

* **Method:**

  `POST`

* **Data Params**

  **Required:**
    `{
        "name": "Ashish",
        "gender": "Male",
        "email": "abc@gmail.com"
    }`

* **Success Response:**

  * **Code:** 200
  * **Content:** `{ "message": "User Ashish is successfully created" }`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST
  * **Content:** `{ error : "Database Error" }`

* **Sample Call:**
Postman API Screenshot:
![user_api](https://github.com/AJ-Walker/Avtaar-Assignment-3/blob/main/user_api.PNG)
  

**Create Event**
---

Create a event in database and returns a JSON success message

* **URL**

  /api/event

* **Method:**

  `POST`

* **Data Params**

  **Required:**
    `{
        "uid": 1,
        "name": "demo_event",
        "occurrence": "ONETIME",
        "startDate": "28-12-2021",
        "endDate": "30-12-2021"
    }`

* **Success Response:**

  * **Code:** 200
  * **Content:** `{ "message": "Event demo_event is successfully created" }`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST
  * **Content:** `{ error : "Database Error" }`

* **Sample Call:**
![event_api](https://github.com/AJ-Walker/Avtaar-Assignment-3/blob/main/event_api.PNG)
  
 
