import importlib

from glob import glob
from pathlib import Path
modules = glob(str(Path(__file__).parent / "../../tasks/*.py"))

tasks = {}

for m in modules:
    m_name = m.split("/")[-1]

    spec = importlib.util.spec_from_file_location(m_name, m)
    m_exe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m_exe)

    tasks[m_name] = m_exe

