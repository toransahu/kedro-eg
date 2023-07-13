from kedro.pipeline import Pipeline

from kedroeg.reqres import client
from kedroeg.core.nodes import BaseNode


def reqres_list_users() -> Pipeline:
    """
    Return reqres list users pipeline
    """
    return Pipeline(
        [
            BaseNode(
                name="reqres_list_users_node",
                func=client.list_users,
                inputs=None,
                outputs="reqres_list_users_node_out",
                bl_type="conn_loc",
                owner="toran",
            ),
        ]
    )
