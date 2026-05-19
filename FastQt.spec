# -*- mode: python ; coding: utf-8 -*-

import os

from PyInstaller.utils.hooks import collect_data_files


def collect_fast_bin():
    binaries = []
    datas = []
    bin_dir = os.path.join('fast', 'bin')
    for name in sorted(os.listdir(bin_dir)):
        path = os.path.join(bin_dir, name)
        if not os.path.isfile(path):
            continue
        if name.lower().endswith(('.dll', '.exe')):
            continue
        if os.access(path, os.X_OK):
            binaries.append((path, 'bin'))
        else:
            datas.append((path, 'bin'))
    return binaries, datas


def collect_mac_bin():
    datas = []
    for root, _, files in os.walk('mac_bin'):
        for name in sorted(files):
            if name == '.DS_Store':
                continue
            path = os.path.join(root, name)
            datas.append((path, root))
    return datas


fast_bin_binaries, fast_bin_datas = collect_fast_bin()

a = Analysis(
    ['_fastQt.py'],
    pathex=[],
    binaries=fast_bin_binaries,
    datas=fast_bin_datas + collect_mac_bin() + collect_data_files('qbstyles') + collect_data_files('qdarkstyle'),
    hiddenimports=['_fast'],
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
    name='FastQt',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
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
    name='FastQt',
)
