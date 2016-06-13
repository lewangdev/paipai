# -*- mode: python -*-

block_cipher = pyi_crypto.PyiBlockCipher(key='we3FeKcRVUun7Gul')


a = Analysis(['..\\src\\app.py'],
             pathex=['C:\\Python27/Lib/site-packages/pil', '', 'F:\\build'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='paipai',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='..\\src\\resources\\paipai.ico')
