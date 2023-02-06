#
python3 -m venv .venv
source ./.venv/bin/active
#
pip install uvicorn[standard]
pip3 install fastapi
pip3 install uvicorn
python-vlc
RPi.GPIO
jinja2
getpodcast
itempelates



uvicorn main:app --host 192.168.1.192 --port 2000

