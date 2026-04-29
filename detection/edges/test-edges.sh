#usage: ./test-edges.sh [path/to/image]

python3 main.py --robust $1 30 60
python3 main.py $1 30 60 
python3 main.py --robust $1 30 90
python3 main.py $1 30 90 
python3 main.py --robust $1 50 100
python3 main.py $1 500 100 
python3 main.py --robust $1 50 150
python3 main.py $1 50 150
python3 main.py --robust $1 100 200
python3 main.py $1 100 200
python3 main.py --robust $1 100 300
python3 main.py $1 100 300
python3 main.py --robust $1 200 300
python3 main.py $1 200 300
python3 main.py --robust $1 200 400
python3 main.py $1 200 400
python3 main.py $1 200 600 
python3 main.py --robust $1 200 600



