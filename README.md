#install software
sudo apt install vlc
#build python venv 
python3 -m venv .venv
source ./.venv/bin/active
#install python package
pip3 install uvicorn[standard]
pip3 install fastapi
pip3 insatll python-vlc
pip3 install getpodcast
pip3 install apscheduler
pip3 install SQLAlchemy
pip3 install RPi.GPIO
pip3 install jinja2
pip3 install gevent
#run FastAPI
uvicorn fast:app --host 192.168.1.196 --port 3000
uvicorn fast:app --host 0.0.0.0 --port 80
#deploy by gunicorn
sudo apt install gunicorn



sudo apt install python3-gevent ????

Note:
1. modify /etc/group,  add www-data to audio group
2. media file is at ./static/assets/ , I use symbolic link to link other directory. For FastAPI protection reason,  I need to modify  .py and .js file.
  -- modify dirpath in fast.py  somewhere API with file_path = os.path.realpath......
  -- modify dir2 in play.js   



# mount mp3 USB Drive to /media/usb1/
$sudo lsblk -o NAME,FSTYPE,UUID,MOUNTPOINTS
$ sudo vi /etc/fstab
/dev/sda1: UUID="E654-E418" BLOCK_SIZE="512" TYPE="vfat"
 sudo  mount -o iocharset=utf8 /dev/sda1 /media/usb-drive/
UUID=E654-E418 /media/usb1/ vfat umask=0022,gid=1000,uid=1000,iocharset=utf8  00
sudo findmnt --verify

