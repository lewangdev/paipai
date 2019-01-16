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
a.datas += [('resources/paipai.ico', 'F:\\src\\resources\\paipai.ico', 'DATA')]
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='paipai',
          debug=True,
          strip=None,
          upx=True,
          console=True , icon='..\\src\\resources\\paipai.ico')
