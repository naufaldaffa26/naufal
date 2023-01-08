from typing import Any, Callable, Dict, Iterator, Optional, Tuple, Union

from django.core.files.base import File
from django.core.files.storage import FileSystemStorage, Storage
from django.utils._os import _PathCompatible
from django.utils.functional import LazyObject

_PostProcessT = Iterator[Union[Tuple[str, str, bool], Tuple[str, None, RuntimeError]]]

class StaticFilesStorage(FileSystemStorage):
    base_location: str
    location: _PathCompatible
    def __init__(
        self, location: Optional[_PathCompatible] = ..., base_url: Optional[str] = ..., *args: Any, **kwargs: Any
    ) -> None: ...
    def path(self, name: _PathCompatible) -> str: ...

class HashedFilesMixin:
    default_template: str = ...
    max_post_process_passes: int = ...
    patterns: Any = ...
    hashed_files: Any = ...
    keep_intermediate_files: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def file_hash(self, name: str, content: File = ...) -> str: ...
    def hashed_name(self, name: str, content: Optional[File] = ..., filename: Optional[str] = ...) -> str: ...
    def url(self, name: str, force: bool = ...) -> str: ...
    def url_converter(self, name: str, hashed_files: Dict[str, Any], template: str = ...) -> Callable: ...
    def post_process(self, paths: Dict[str, Any], dry_run: bool = ..., **options: Any) -> _PostProcessT: ...
    def clean_name(self, name: str) -> str: ...
    def hash_key(self, name: str) -> str: ...
    def stored_name(self, name: str) -> str: ...

class ManifestFilesMixin(HashedFilesMixin):
    manifest_version: str = ...
    manifest_name: str = ...
    manifest_strict: bool = ...
    keep_intermediate_files: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def read_manifest(self) -> str: ...
    def load_manifest(self) -> Dict[str, Any]: ...
    def save_manifest(self) -> None: ...
    def post_process(self, *args: Any, **kwargs: Any) -> _PostProcessT: ...
    def stored_name(self, name: str) -> str: ...

class ManifestStaticFilesStorage(ManifestFilesMixin, StaticFilesStorage): ...  # type: ignore
class ConfiguredStorage(LazyObject): ...

staticfiles_storage: Storage