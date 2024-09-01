from cx_Freeze import setup, Executable
import sys

files = ["robot.ico"]

base = None
if sys.platform == "win32":
    base = "Win32GUI"

Executable(
    script="gerador_de_senhas_interface.py",
    base="Win32GUI",
    icon="robot.ico"
  )

setup(

  name = "Gerador de Senhas",
  version = "1.0",
  description = "Sistema onde o usuário pode gerar senhas aleatórias.",
  author = "Gabriel Machado",
  executables = [Executable("gerador_de_senhas_interface.py", base=base, icon="robot.ico")],
  options = {
    "build_exe": {
      "packages": ["tkinter", "customtkinter"],
      "include_files": files,
      "include_msvcr": True
    }
  }
)
