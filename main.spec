# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\PC\\PycharmProjects\\plcmonitor\\monitor',
             'C:\\Users\\PC\\PycharmProjects\\plcmonitor\\monitor\\window',
             'C:\\Users\\PC\\PycharmProjects\\plcmonitor\\monitor\\ui_py',
             'C:\\Users\\PC\\PycharmProjects\\plcmonitor\\monitor\\function',
             ],
             binaries=[],
             datas=[],
             hiddenimports=['monitor.py', 'ui_centerCar.py', 'ui_leftCar.py', 'ui_monitor.py', 'ui_rightCar.py', 'pyModbus.py', 'communication.py', 'config.py'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
