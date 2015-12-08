pyinstaller ../src/app.py ^
    --noconsole^
    --onefile ^
    --distpath=../dist ^
    --key=we3FeKcRVUun7Gul ^
    --upx-dir=C:\upx391w\upx391w ^
    --icon=../src/paipai.ico ^
    -p %PYTHONPATH%/Lib/site-packages/pil;
