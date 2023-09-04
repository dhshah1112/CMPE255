sudo apt-get update
sudo apt-get install python3

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt

python user.py &
python post.py &
python feed.py &
python follow.py &
python like.py &
python comment.py &
