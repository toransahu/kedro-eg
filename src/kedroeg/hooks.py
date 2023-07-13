"""Project hooks."""
from typing import Any, Dict, Iterable, Optional

from kedro.config import ConfigLoader
from kedro.framework.hooks import hook_impl
from kedro.io import DataCatalog
from kedro.versioning import Journal
from kedro.pipeline.node import Node

from kedroeg.core.nodes import BaseNode


class ProjectHooks:
    @hook_impl
    def register_config_loader(
        self,
        conf_paths: Iterable[str],
        env: str,
        extra_params: Dict[str, Any],
    ) -> ConfigLoader:
        return ConfigLoader(conf_paths)

    @hook_impl
    def register_catalog(
        self,
        catalog: Optional[Dict[str, Dict[str, Any]]],
        credentials: Dict[str, Dict[str, Any]],
        load_versions: Dict[str, str],
        save_version: str,
        journal: Journal,
    ) -> DataCatalog:
        return DataCatalog.from_config(catalog, credentials, load_versions, save_version, journal)


class NodeHooks:
    # NOTE: make sure, its registered in settings.py
    @hook_impl
    def after_node_run(
        self,
        node: BaseNode,
        catalog: DataCatalog,
        inputs: Dict[str, Any],
        outputs: Dict[str, Any],
        is_async: bool,
        run_id: str,
    ) -> None:
        import pdb
        from kedroeg.settings import conf_parameters

        pdb.set_trace()

        if node.name == "reqres_list_users_node":
            print("HERE")
