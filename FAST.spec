# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['_fast.py'],
    pathex=[],
    binaries=[('fast/bin/crx2rnx', 'bin'), ('fast/bin/lftp', 'bin'), ('fast/bin/uncompress', 'bin'), ('fast/bin/unzip', 'bin')],
    datas=[('fast/bin/fast_download_src.json', 'bin'), ('fast/bin/IGSNetwork.csv', 'bin')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='FAST',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    contents_directory='.',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='FAST',
)
