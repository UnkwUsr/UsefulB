from pathlib import Path
BUILTIN_TASKS_FOLDER_PATH = str((Path(__file__).parent / "../../tasks").resolve())
from config import config_get
from ast import literal_eval
# config format: list of paths to folders with .py files that contains class 'Task'
TASKS_FOLDERS_PATHS = literal_eval(config_get("Core", "tasks_folders_paths", [BUILTIN_TASKS_FOLDER_PATH]))
# check all elements in list is str
if not all(isinstance(x, str) for x in TASKS_FOLDERS_PATHS):
    exit("'tasks_folders_paths' is list ONLY with strings\n(try wrap all elements to quotes)")

from glob import glob
py_files = []
for p in TASKS_FOLDERS_PATHS:
    py_files += glob(p + "/*.py")

module_by_name_dict = {}
from importlib import util as import_util
for m in py_files:
    # m_name = m.split("/")[-1]
    m_name = m.split("/")[-1].split(".")[0]

    spec = import_util.spec_from_file_location(m_name, m)
    m_exe = import_util.module_from_spec(spec)
    spec.loader.exec_module(m_exe)

    module_by_name_dict[m_name] = m_exe

str_all_tasks_names = ' '.join(list(module_by_name_dict.keys()))
# config format: space separated list of Task names
TASKS_QUEUE = config_get("Core", "tasks_queue", str_all_tasks_names).split(' ')

tasks = []
for task_name in TASKS_QUEUE:
    if not task_name in module_by_name_dict:
        print(task_name + " not found in tasks_folders_paths")
    else:
        tasks.append(module_by_name_dict[task_name].Task())

if not tasks:
    exit("No tasks for solve. Check your tasks_queue")

