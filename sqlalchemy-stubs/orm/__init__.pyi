from typing import Any, Optional
from .mapper import (
    Mapper as Mapper,
    class_mapper as class_mapper,
    configure_mappers as configure_mappers,
    reconstructor as reconstructor,
    validates as validates
)
from .interfaces import (
    EXT_CONTINUE as EXT_CONTINUE,
    EXT_STOP as EXT_STOP,
    PropComparator as PropComparator
)
from .util import (
    aliased as aliased,
    join as join,
    object_mapper as object_mapper,
    outerjoin as outerjoin,
    polymorphic_union as polymorphic_union,
    was_deleted as was_deleted,
    with_parent as with_parent,
    with_polymorphic as with_polymorphic
)
from .properties import ColumnProperty as ColumnProperty
from .relationships import RelationshipProperty as RelationshipProperty
from .descriptor_props import (
    ComparableProperty as ComparableProperty,
    CompositeProperty as CompositeProperty,
    SynonymProperty as SynonymProperty
)
from .relationships import foreign as foreign, remote as remote
from .session import (
    Session as Session,
    close_all_sessions as close_all_sessions,
    object_session as object_session,
    sessionmaker as sessionmaker,
    make_transient as make_transient,
    make_transient_to_detached as make_transient_to_detached
)
from .scoping import scoped_session as scoped_session
from . import mapper as mapperlib
from .query import AliasOption as AliasOption, Query as Query, Bundle as Bundle
from .strategy_options import Load as Load
from ..ext.declarative import DeclarativeMeta

def create_session(bind: Optional[Any] = ..., **kwargs): ...

relationship = RelationshipProperty

def relation(*arg, **kw): ...
def dynamic_loader(argument, **kw): ...

column_property = ColumnProperty
composite = CompositeProperty

def query_expression() -> ColumnProperty: ...

def backref(name, **kwargs): ...
def deferred(*columns, **kw): ...

mapper = Mapper
synonym = SynonymProperty
comparable_property = ComparableProperty

def compile_mappers(): ...
def clear_mappers(): ...

# TODO: these are function "aliases"
joinedload: Any = ...
joinedload_all: Any = ...
contains_eager: Any = ...
defer: Any = ...
undefer: Any = ...
undefer_group: Any = ...
with_expression: Any = ...
load_only: Any = ...
lazyload: Any = ...
lazyload_all: Any = ...
subqueryload: Any = ...
subqueryload_all: Any = ...
selectinload: Any = ...
selectinload_all: Any = ...
immediateload: Any = ...
noload: Any = ...
raiseload: Any = ...
defaultload: Any = ...
selectin_polymorphic: Any = ...

def eagerload(*args, **kwargs): ...
def eagerload_all(*args, **kwargs): ...
def declarative_base(*args, **kwargs): ...
contains_alias = AliasOption


class MapperExtension:
    @classmethod
    def _adapt_instrument_class(cls, self, listener) -> None: ...

    @classmethod
    def _adapt_listener(cls, self, listener) -> None: ...

    @classmethod
    def _adapt_listener_methods(cls, self, listener, methods) -> None: ...

    def instrument_class(self, mapper, class_) -> Any: ...
    def init_instance(self, mapper, class_, oldinit, instance, args, kwargs) -> Any: ...
    def init_failed(self, mapper, class_, oldinit, instance, args, kwargs) -> Any: ...
    def reconstruct_instance(self, mapper, instance) -> Any: ...
    def before_insert(self, mapper, connection, instance) -> Any: ...
    def after_insert(self, mapper, connection, instance) -> Any: ...
    def before_update(self, mapper, connection, instance) -> Any: ...
    def after_update(self, mapper, connection, instance) -> Any: ...
    def before_delete(self, mapper, connection, instance) -> Any: ...
    def after_delete(self, mapper, connection, instance) -> Any: ...
