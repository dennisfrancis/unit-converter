# Unit Converter
A web app that can convert units of length, weight, temperature. The user can input a value and select the units to convert from and to. The application will then display the converted value.

## How to install and run?
1. Clone the repo.
```
git clone https://github.com/dennisfrancis/unit-converter.git
```

2. Create virtual environment for python and install dependencies.
```
cd unit-converter
python3 -m venv .venv
source .venv/bin/activate
pip install -r ./requirements.txt
```

3. Run development server
```
python3 manage.py runserver
```

4. Point the browser to the URL `127.0.0.1:8000/convert`

## Acknowledgements
This project was created from the specs provided at [roadmap.sh](https://roadmap.sh/projects/unit-converter).
