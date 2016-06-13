pyinstaller ../src/app.py ^
    --name=paipai ^
    --noconsole^
    --onefile ^
    --distpath=./dist ^
    --key=we3FeKcRVUun7Gul ^
    --upx-dir=C:\upx391w\upx391w ^
    --icon=../src/resources/paipai.ico ^
    -p %PYTHONPATH%/Lib/site-packages/pil;
