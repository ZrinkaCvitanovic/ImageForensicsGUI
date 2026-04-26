#usage: ./test-color.sh [path/to/image1] [path/to/image/2]
python3 main.py $1 hsv
python3 main.py $1 lum 
python3 main.py $2 hsv
python3 main.py $2 lum