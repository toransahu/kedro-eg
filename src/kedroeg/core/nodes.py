from typing import Callable, Dict, Iterable, List, Union
from kedro.pipeline.node import Node as Node


class BaseNode(Node):
    def __init__(
        self,
        func: Callable,
        inputs: Union[None, str, List[str], Dict[str, str]],
        outputs: Union[None, str, List[str], Dict[str, str]],
        *,
        name: str = None,
        tags: Union[str, Iterable[str]] = None,
        decorators: Iterable[Callable] = None,
        confirms: Union[str, List[str]] = None,
        namespace: str = None,
        **kwargs
    ):
        self.kwargs = kwargs
        super().__init__(
            func, inputs, outputs, name=name, tags=tags, decorators=decorators, confirms=confirms, namespace=namespace
        )
