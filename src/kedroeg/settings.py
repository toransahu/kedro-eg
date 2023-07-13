"""Project settings."""
from pathlib import Path

from kedro.config import TemplatedConfigLoader

from kedroeg.hooks import NodeHooks, ProjectHooks

# Instantiate and list your project hooks here
HOOKS = (ProjectHooks(), NodeHooks())

# List the installed plugins for which to disable auto-registry
# DISABLE_HOOKS_FOR_PLUGINS = ("kedro-viz",)

# Define where to store data from a KedroSession. Defaults to BaseSessionStore.
# from kedro.framework.session.store import ShelveStore
# SESSION_STORE_CLASS = ShelveStore

# Define keyword arguments to be passed to `SESSION_STORE_CLASS` constructor
# SESSION_STORE_ARGS = {
#     "path": "./sessions"
# }

# Define custom context class. Defaults to `KedroContext`
# CONTEXT_CLASS = KedroContext

# Define Project Path

# PROJECT_DIR = Path(__file__).resolve().parent.parent.parent
HERE = Path(__file__).resolve().parent
PROJECT_DIR = HERE.parent
print(" Path(__file__).resolve()", Path(__file__).resolve())
print("PROJECT_DIR", PROJECT_DIR)

# Define the configuration folder. Defaults to `conf`
# CONF_ROOT = "conf"
# conf_paths = ["../conf/base", "../conf/local"]
conf_paths = ["conf/base", "conf/local"]
# conf_paths = [f"{PROJECT_DIR}/conf/base", f"{PROJECT_DIR}/conf/local"]
conf_loader = TemplatedConfigLoader(conf_paths, globals_pattern="*.yml", globals_dict={"param1": "pandas.CSVDataSet"})
conf_catalog = conf_loader.get("catalog*", "catalog*/**")
conf_logging = conf_loader.get("logging*", "logging*/**")
conf_parameters = conf_loader.get("parameters*", "parameters*/**")
conf_credentials = conf_loader.get("credentials*", "credentials*/**")
