# contest-API

## Technology used
    Python, Flask-restful, Web scrapping using BeautifulSoup (bs4)

## Instructions:

### Prerequisites:
    1. Python3 should be installed on the system.

### To run the project locally, follow the following steps:
    1. Setup a virtual environment:
        For ubuntu:
            1. sudo apt install virtualenv
            2. virtualenv -p python3 name_of_environment
            3. To activate: source name_of_environment/bin/activate
        For windows:
            1.	pip install virtualenv
            2.	python -m venv <path for creating virtualenv>
            3.	To activate: <virtualenv path>\Scripts\activate

    2. Clone the repository: git clone https://github.com/Pirate2606/contest-API
    3. Change the directory: cd contest-API
    4. Install the requirements: pip install -r requirements.txt
    5. Run the server: python3 app.py
    6. Use Postman to fetch results from API using following endpoints:
        -> Get all the contests: http://127.0.0.1:5000/contests
        -> Get the number of contests: http://127.0.0.1:5000/contests/count
