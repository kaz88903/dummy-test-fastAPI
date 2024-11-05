# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['dummy_test_fastAPI/dummy_fastAPI.py'],  # Main script
    pathex=[],
    binaries=[],
    datas=[
        # Include cal_test_fastAPI.py in datas if needed
        ('dummy_test_fastAPI/cal_test_fastAPI.py', '.'),  # Include at root level
	('dummy_test_fastAPI/resultflag_enum.py', '.'),
    ],
    hiddenimports=[
        'cal_test_fastAPI',
	'resultflag_enum',  # Include as a hidden import
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher,
)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='dummy_fastAPI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Set to True if you want a console window
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='dummy_fastAPI',
)
