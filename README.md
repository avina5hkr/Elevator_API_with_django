<h1 align="center">Implementing Elevator functions with Django</h1>

<p align="center">
  <img src="https://img.shields.io/github/issues/avina5hkr/Elevator_API_with_django">
  <img src="https://img.shields.io/github/forks/avina5hkr/Elevator_API_with_django">
  <img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103">
  <img src="https://img.shields.io/github/stars/avina5hkr/Elevator_API_with_django">
  <!-- <img src="https://img.shields.io/github/license/avina5hkr/Elevator_API_with_django"> -->
</p>

Description
---------------------


This is a Django Rest Framework based API implementing an Elevator system.

API Endpoints:
---------------------
<ul>
<h3>
<li>Endpoint: `/elevator/elevator/` </li>
</h3>

>METHODS: [GET, POST]  

Example Payload for creating new elevator:   
```json
    {  
            "location": "main",  
            "current_floor": 0,  
            "destination_floor": null,  
            "direction": None,  
            "working": True,  
            "min_floor": 0,  
            "max_floor": 10,  
            "max_occupancy": 10,  
            "current_occupancy": 0,  
            "status": 1  
        }
```  
        

<li><h3>Endpoint: `/elevator/elevator/<elevator-id>` <h3> </li>  

>METHODS: [GET, DELETE, UPDATE]  

Example JSON Payload for update:   
```json
    {  
            "location": "main",  
            "current_floor": 0,  
            "destination_floor": null,  
            "direction": None,  
            "working": True,  
            "min_floor": 0,  
            "max_floor": 10,  
            "max_occupancy": 10,  
            "current_occupancy": 0,  
            "status": 1  
        }
```


<li><h3>Endpoint: `/elevator/use/` <h3> </li>  

>METHODS: [POST] 

Example payload for using an elevator:
```json
{
    "elevator_id": 1,  
    "elevator_name": "main",   # (optional) if id is not provided
    "current_floor": 1,
    "destination_floor": 7
}
```

<li><h3>Endpoint: `/elevator/maintainence/` <h3> </li>  

>METHODS: [POST] 

Example payload to put elevator in maintainance and in normal mode:
```json
{
    "elevator_id": 1,
    "action": "start"    # "finish" for going back to normal mode
}
```

</ul>

Running on local machine
---------------------
1. Clone this project<br>
  ```
  $ git clone https://github.com/avina5hkr/Elevator_API_with_django.git
  ```  
2. Create and activate a virtual environment (optional) <br>
  ```bash python
  $ python -m venv venv
  $ source venv/bin/activate
  ```
3. Install the python dependencies
  ```python
  $ pip install -r requirements.txt
  ```
4. Run the development server
  ```python
  $ python manage.py runerver 0.0.0.0:8000
  ```





