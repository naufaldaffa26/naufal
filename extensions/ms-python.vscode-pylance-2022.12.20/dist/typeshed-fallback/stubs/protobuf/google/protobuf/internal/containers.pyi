from collections.abc import Callable, Iterable, Iterator, MutableMapping, Sequence
from typing import Any, TypeVar, overload
from typing_extensions import SupportsIndex

from google.protobuf.descriptor import Descriptor
from google.protobuf.internal.message_listener import MessageListener
from google.protobuf.internal.python_message import GeneratedProtocolMessageType
from google.protobuf.internal.type_checkers import _ValueChecker
from google.protobuf.message import Message

_T = TypeVar("_T")
_K = TypeVar("_K", bound=bool | int | str)
_ScalarV = TypeVar("_ScalarV", bound=bool | int | float | str | bytes)
_MessageV = TypeVar("_MessageV", bound=Message)
_M = TypeVar("_M")

class BaseContainer(Sequence[_T]):
    def __init__(self, message_listener: MessageListener) -> None: ...
    def __len__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def sort(self, *, key: Callable[[_T], Any] | None = ..., reverse: bool = ...) -> None: ...
    @overload
    def __getitem__(self, key: SupportsIndex) -> _T: ...
    @overload
    def __getitem__(self, key: slice) -> list[_T]: ...

class RepeatedScalarFieldContainer(BaseContainer[_ScalarV]):
    def __init__(self, message_listener: MessageListener, type_checker: _ValueChecker[_ScalarV]) -> None: ...
    def append(self, value: _ScalarV) -> None: ...
    def insert(self, key: int, value: _ScalarV) -> None: ...
    def extend(self, elem_seq: Iterable[_ScalarV] | None) -> None: ...
    def MergeFrom(self: _M, other: _M) -> None: ...
    def remove(self, elem: _ScalarV) -> None: ...
    def pop(self, key: int = ...) -> _ScalarV: ...
    @overload
    def __setitem__(self, key: int, value: _ScalarV) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Iterable[_ScalarV]) -> None: ...
    def __delitem__(self, key: int | slice) -> None: ...
    def __eq__(self, other: object) -> bool: ...

class RepeatedCompositeFieldContainer(BaseContainer[_MessageV]):
    def __init__(self, message_listener: MessageListener, message_descriptor: Descriptor) -> None: ...
    def add(self, **kwargs: Any) -> _MessageV: ...
    def append(self, value: _MessageV) -> None: ...
    def insert(self, key: int, value: _MessageV) -> None: ...
    def extend(self, elem_seq: Iterable[_MessageV]) -> None: ...
    def MergeFrom(self: _M, other: _M) -> None: ...
    def remove(self, elem: _MessageV) -> None: ...
    def pop(self, key: int = ...) -> _MessageV: ...
    def __delitem__(self, key: int | slice) -> None: ...
    def __eq__(self, other: object) -> bool: ...

class ScalarMap(MutableMapping[_K, _ScalarV]):
    def __init__(
        self,
        message_listener: MessageListener,
        key_checker: _ValueChecker[_K],
        value_checker: _ValueChecker[_ScalarV],
        entry_descriptor: Descriptor,
    ) -> None: ...
    def __setitem__(self, k: _K, v: _ScalarV) -> None: ...
    def __delitem__(self, v: _K) -> None: ...
    def __getitem__(self, k: _K) -> _ScalarV: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_K]: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def get(self, key: _K, default: None = ...) -> _ScalarV: ...
    @overload
    def get(self, key: _K, default: _ScalarV | _T) -> _ScalarV | _T: ...
    def MergeFrom(self: _M, other: _M): ...
    def InvalidateIterators(self) -> None: ...
    def GetEntryClass(self) -> GeneratedProtocolMessageType: ...

class MessageMap(MutableMapping[_K, _MessageV]):
    def __init__(
        self,
        message_listener: MessageListener,
        message_descriptor: Descriptor,
        key_checker: _ValueChecker[_K],
        entry_descriptor: Descriptor,
    ) -> None: ...
    def __setitem__(self, k: _K, v: _MessageV) -> None: ...
    def __delitem__(self, v: _K) -> None: ...
    def __getitem__(self, k: _K) -> _MessageV: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_K]: ...
    def __eq__(self, other: object) -> bool: ...
    @overload
    def get(self, key: _K, default: None = ...) -> _MessageV: ...
    @overload
    def get(self, key: _K, default: _MessageV | _T) -> _MessageV | _T: ...
    def get_or_create(self, key: _K) -> _MessageV: ...
    def MergeFrom(self: _M, other: _M): ...
    def InvalidateIterators(self) -> None: ...
    def GetEntryClass(self) -> GeneratedProtocolMessageType: ...
