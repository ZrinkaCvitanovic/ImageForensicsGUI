#usage: ./test-edges.sh [path/to/image]

python3 main.py --robust $1 30 200
python3 main.py $1 30 200 
python3 main.py $1 50 400 
python3 main.py --robust $1 50 400 
python3 main.py $1 100 500 
python3 main.py --robust $1 100 500 
python3 main.py $1 200 600 
python3 main.py --robust $1 200 600 


