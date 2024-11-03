#!/env/bin/python3
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    echo "Virtual environment created and dependencies installed."
else
    echo "Virtual environment already exists."
fi