# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

BASE_DIR = Path(SPECPATH)

a = Analysis(
    ['main.py'],
    pathex=[str(BASE_DIR)],
    binaries=[],
    datas=[
        (str(BASE_DIR / 'precipitacion.ico'), '.'),
        (str(BASE_DIR / 'MONTEVIDEO.png'), '.'),
        (str(BASE_DIR / 'Logo_Grupo_Tau.png'), '.'),
        (str(BASE_DIR / 'Logo_imm.jpg'), '.'),
        (str(BASE_DIR / 'Logo_Dica.png'), '.'),
        (str(BASE_DIR / 'Coordenadas_Equipos.csv'), '.'),
        (str(BASE_DIR / 'Lugares-ID.csv'), '.'),
    ],
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
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(BASE_DIR / 'precipitacion.ico'),
)