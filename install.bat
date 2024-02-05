pip install -r requirements.txt
python -m PyInstaller NotePad.py --onefile --windowed --icon=Resource/icon.ico
move dist\*.exe ./ && exit 0