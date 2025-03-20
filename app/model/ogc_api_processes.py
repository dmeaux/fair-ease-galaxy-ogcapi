# ===---------------------------------------------------------------------=== #
#    Copyright © 2024, Geomatys, SAS. All rights reserved.
#    http://www.geomatys.com
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you
#    may not use this file except in compliance with the License. You may
#    obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#    or implied. See the License for the specific language governing
#    permissions and limitations under the License.
# ===---------------------------------------------------------------------=== #

"""This is the `` module.

Description
"""

from __future__ import annotations

__author__: str = "David Meaux"
__version__: str = "0.0a1"


from enum import Enum
from typing import Any, Optional, Sequence, Union
from typing_extensions import Annotated

from pydantic import BaseModel, conlist, conset, Field

from model._common import (
    OptionalAnything,
    NonNegativeIntDefault0,
    OptionalBool,
    OptionalInt,
    OptionalFloat,
    OptionalNonNegativeInt,
    OptionalString,
    RequiredString,
)


class JobControlOptions(Enum):
    SYNC_EXECUTE = "sync-execute"
    ASYC_EXECUTE = "async-execute"
    DISMISS = "dismiss"


class OccurrenceBoundsType(Enum):
    UNBOUNDED = "unbounded"


class ValuePassingType(Enum):
    BY_VALUE = "byValue"
    BY_REFERENCE = "byReference"


class Link(BaseModel):
    """

    Attributes:
        href (str):
        rel (Optional[str]):
            Example: service
        type (Optional[str]):
            Example: application/json
        hreflang (Optional[str]):
            Example: en
        title (Optional[str]):
    """
    href: RequiredString
    rel: OptionalString
    type: OptionalString
    hreflang: OptionalString
    title: OptionalString


class MetadataLink(BaseModel):
    link: Link
    role: RequiredString


class MetadataModel(BaseModel):
    role: OptionalString
    title: OptionalString
    lang: OptionalString
    value: Any


Metadata = Union[
    MetadataLink,
    MetadataModel
]


class Reference(BaseModel):
    """
    Attributes:
        ref (str):
            Format: uri-reference
    """
    ref: RequiredString


class Properties(BaseModel):
    properties: OptionalAnything
    additionalProperties: Annotated[Sequence[Reference],
                                    Field(frozen=True),
                                    ]


class SchemaType(str, Enum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    NUMBER = "number"
    OBJECT = "object"
    STRING = "string"


SchemaReferences = conlist(Reference, min_length=1)


class SchemaModel(BaseModel):
    title: OptionalString
    multipleOf: Annotated[Optional[float], Field(frozen=True, gt=0)]
    maximum: OptionalFloat
    exclusiveMaximum: OptionalBool
    minimum: OptionalFloat
    exclusiveMinimum: OptionalBool
    maxLength: OptionalNonNegativeInt
    minLength: NonNegativeIntDefault0
    pattern: OptionalString
    maxItems: OptionalNonNegativeInt
    minItems: NonNegativeIntDefault0
    uniqueItems: OptionalBool
    maxProperties: OptionalNonNegativeInt
    minProperties: NonNegativeIntDefault0
    required: conset(Optional[str], min_length=1)
    enum: conlist(Any, min_length=1)
    type: SchemaType
    items: Annotated[Optional[Reference], Field(frozen=True)]
    properties: Annotated[Union[Any, Reference],
                          Field(frozen=True)]
    additionalProperties: Annotated[Optional[Properties],
                                    Field(frozen=True, default=True)]
    description: OptionalString
    format: OptionalString
    default: OptionalAnything
    nullable: OptionalBool
    readOnly: OptionalBool
    writeOnly: OptionalBool
    example: OptionalAnything
    deprecated: OptionalBool
    contentMediaType: OptionalString
    contentEncoding: OptionalString
    contentSchema: OptionalString


Schema = Union[
    Reference,
    SchemaModel,
    SchemaReferences,
]


class DescriptionType(BaseModel):
    title: OptionalString
    description: OptionalString
    keywords: Annotated[Optional[Sequence[str]], Field(frozen=True)] = None
    metadata: Annotated[Optional[Metadata], Field(frozen=True)] = None


class InputDescription(BaseModel):
    descriptionType: Annotated[DescriptionType, Field(frozen=True)]
    # schema: Annotated[Schema, Field(frozen=True)]
    dataClasses: Annotated[Optional[Sequence[str]], Field(frozen=True)] = None
    minOccurs: OptionalInt = 1
    maxOccurs: Annotated[Optional[int | OccurrenceBoundsType],
                         Field(frozen=True)] = None
    valuePassing: Annotated[Optional[Sequence[str]], Field(frozen=True)] = (
        str(ValuePassingType.BY_VALUE),
        str(ValuePassingType.BY_REFERENCE),
    )


class OutputDescription(BaseModel):
    descriptionType: Annotated[DescriptionType, Field(frozen=True)]
    # schema: Annotated[Schema, Field(frozen=True)]


class ProcessSummary(BaseModel):
    descriptionType: Annotated[DescriptionType, Field(frozen=True)]
    id: RequiredString
    version: RequiredString
    jobControlOptions: Annotated[Optional[Sequence[JobControlOptions]],
                                 Field(frozen=True),
                                 ] = None
    links: Annotated[Optional[Sequence[Link]], Field(frozen=True)] = None


class Process(BaseModel):
    processSummary: Annotated[ProcessSummary, Field(frozen=True)]
    inputs: Annotated[Sequence[InputDescription], Field(frozen=True)]
    outputs: Annotated[Sequence[OutputDescription], Field(frozen=True)]
