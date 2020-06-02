import glob
import importlib

modules = glob.glob("tasks/*.py")

tasks = {}

for m in modules:
    m_name = m.split("/")[-1]

    spec = importlib.util.spec_from_file_location(m_name, m)
    m_exe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m_exe)

    tasks[m_name] = m_exe

