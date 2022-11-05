# Mockup generator

## Run

```
python3 -m venv env
# activate the environment
pip install requirements.txt
flask --app hello run
```

## Run with docker

```
docker build -t mockup_generator .
docker run -p 5000:5000 mockup_generator
```
