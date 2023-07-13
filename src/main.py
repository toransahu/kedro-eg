from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

from kedroeg.settings import PROJECT_DIR


metadata = bootstrap_project(PROJECT_DIR)

# NOTE: path project path to solve hard coded log config path in session,config,context
with KedroSession.create(package_name=metadata.package_name, project_path=PROJECT_DIR) as session:
    session.run(pipeline_name="reqres_list_users")
