import sys
import os
from cx_Freeze import setup, Executable

arquivos = ["caixa.ico", "imagens/"]

config = Executable(
    script="app.py",
    icon="caixa.ico",
)
setup(
    name="Sistema Caixa",
    version="1.0",
    description="Sistema de caixa para imobiliaria",
    author="Felipe Mattei Ximenes",
    options={"build_exe": {"include_files": arquivos}},
    executables=[config]
)