# generated by datamodel-codegen:
#   filename:  model_repository.yaml

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class RepositoryIndexRequest(BaseModel):
    ready: Optional[bool] = None


class State(Enum):
    UNKNOWN = "UNKNOWN"
    READY = "READY"
    UNAVAILABLE = "UNAVAILABLE"
    LOADING = "LOADING"
    UNLOADING = "UNLOADING"


class RepositoryIndexResponseItem(BaseModel):
    name: str
    version: Optional[str] = None
    state: "State"
    reason: str


class RepositoryIndexResponse(BaseModel):
    __root__: List["RepositoryIndexResponseItem"]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, idx):
        return self.__root__[idx]

    def __len__(self):
        return len(self.__root__)

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if isinstance(v, dict):
            return v.get("__root__", [])
        return v


class RepositoryIndexErrorResponse(BaseModel):
    error: Optional[str] = None


class RepositoryLoadErrorResponse(BaseModel):
    error: Optional[str] = None


class RepositoryUnloadErrorResponse(BaseModel):
    error: Optional[str] = None
