# HackTheNorth2021
1) Create virtual environ:
```
For Windows users:
virtualenv venv     # create your virtual environment
./venv/Scripts/activate # activate your newly created virtual environment
```
```
For Mac users:
virtualenv venv
source venv/bin/activate
```

2) ```pip install -r requirements.txt```
3)  ```npm install```
4) Wait for installation to finish. ```npm start```
5) Install Lilypond, a music notation generator. http://lilypond.org/
6) Install docker, and run the following on the command line:
```docker run -p 9000:9000 -p 9001:9001 -e "MINIO_ROOT_USER=JIYE" -e "MINIO_ROOT_PASSWORD=JIYE4EVER"  quay.io/minio/minio server /data --console-address ":9001"```
7) cd root/backend
8) ```python app.py```

Here is a demo of our project:
https://devpost.com/software/score-me?ref_content=user-portfolio&ref_feature=in_progress

youtube link:
https://www.youtube.com/watch?v=jaaZM0HFJLA
