"""Usando o módulo ‘subprocess’ de Python, crie um processo externo e imprima o PID dele."""

import subprocess

p = subprocess.Popen(["notepad", "exemplo.txt"])
print("PID do processo criado:", p.pid)