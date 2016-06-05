pyinstaller ../src/app.py ^
    --name=assistant ^
    --noconsole^
    --onefile ^
    --distpath=./dist ^
    --icon=../src/resources/paipai.ico ^
    -p %PYTHONPATH%/Lib/site-packages/pil;
