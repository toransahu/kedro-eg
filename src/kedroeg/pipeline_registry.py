"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from kedroeg.pipelines.reqres import reqres_list_users


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    return {
        "reqres_list_users": reqres_list_users(),
        "__default__": pipeline([]),
    }
