# Auto generated from template_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-08T00:32:35
# Schema: hello-world
#
# id: https://example.org/linkml/hello-world
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EX = CurieNamespace('ex', 'https://example.org/linkml/hello-world/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SDO = CurieNamespace('sdo', 'https://schema.org/')
DEFAULT_ = EX


# Types

# Class references
class PersonId(extended_str):
    pass


class FriendlyPersonId(PersonId):
    pass


@dataclass
class Person(YAMLRoot):
    """
    Minimal information about a person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SDO.Person
    class_class_curie: ClassVar[str] = "sdo:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = EX.Person

    id: Union[str, PersonId] = None
    first_name: Union[str, List[str]] = None
    last_name: str = None
    knows: Optional[Union[Union[str, PersonId], List[Union[str, PersonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self._is_empty(self.first_name):
            self.MissingRequiredField("first_name")
        if not isinstance(self.first_name, list):
            self.first_name = [self.first_name] if self.first_name is not None else []
        self.first_name = [v if isinstance(v, str) else str(v) for v in self.first_name]

        if self._is_empty(self.last_name):
            self.MissingRequiredField("last_name")
        if not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if not isinstance(self.knows, list):
            self.knows = [self.knows] if self.knows is not None else []
        self.knows = [v if isinstance(v, PersonId) else PersonId(v) for v in self.knows]

        super().__post_init__(**kwargs)


@dataclass
class FriendlyPerson(Person):
    """
    A person who actually knows someone
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EX.FriendlyPerson
    class_class_curie: ClassVar[str] = "ex:FriendlyPerson"
    class_name: ClassVar[str] = "FriendlyPerson"
    class_model_uri: ClassVar[URIRef] = EX.FriendlyPerson

    id: Union[str, FriendlyPersonId] = None
    first_name: Union[str, List[str]] = None
    last_name: str = None
    knows: Union[Union[str, PersonId], List[Union[str, PersonId]]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FriendlyPersonId):
            self.id = FriendlyPersonId(self.id)

        if self._is_empty(self.knows):
            self.MissingRequiredField("knows")
        if not isinstance(self.knows, list):
            self.knows = [self.knows] if self.knows is not None else []
        self.knows = [v if isinstance(v, PersonId) else PersonId(v) for v in self.knows]

        super().__post_init__(**kwargs)


# Enumerations


# Slots

