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
    # this is module file name (as file.py), not task name
    m_name = m.split("/")[-1]

    spec = import_util.spec_from_file_location(m_name, m)
    m_exe = import_util.module_from_spec(spec)
    spec.loader.exec_module(m_exe)

    task_name = m_exe.TASK_NAME

    module_by_name_dict[task_name] = m_exe

    # create config entries for each loaded module
    # (also store it for transfer to Task-constructor later)
    if hasattr(m_exe, "CONFIG"):
        for entry_name, def_value in m_exe.CONFIG.items():
            # automatic cast str from config_get to type of 'default_value'
            entry_type = type(def_value)
            config_value = config_get(task_name, entry_name, def_value)
            m_exe.CONFIG[entry_name] = entry_type(config_value)

str_all_tasks_names = ' '.join(list(module_by_name_dict.keys()))
# config format: space separated list of Task names
TASKS_QUEUE = config_get("Core", "tasks_queue", str_all_tasks_names).split(' ')

tasks = []
for task_name in TASKS_QUEUE:
    if not task_name in module_by_name_dict:
        print(task_name + " not found in tasks_folders_paths")
    else:
        cur_module = module_by_name_dict[task_name]
        task_instance = cur_module.Task()
        tasks.append(task_instance)

if not tasks:
    exit("No tasks for solve. Check your tasks_queue and/or tasks_folders_paths")

