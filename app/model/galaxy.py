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

__author__: str = "David Meaux (Geomatys)"
__version__: str = "0.0a1"


from typing import Any, Sequence
from typing_extensions import Annotated

from pydantic import BaseModel, Field

from model._common import (
    RequiredString,
    RequiredBool,
)


class ToolInputs(BaseModel):
    properties: Annotated[dict[str, Any], Field(frozen=True)]


class StepInput(BaseModel):
    id: RequiredString
    type: RequiredString
    tool_id: RequiredString
    tool_version: RequiredString
    annotation: RequiredString
    tool_inputs: Annotated[ToolInputs, Field(frozen=True)]


class Workflow(BaseModel):
    id: RequiredString
    name: RequiredString
    published: RequiredBool
    importable: RequiredBool
    deleted: RequiredBool
    hidden: RequiredBool
    tags: Annotated[set[str], Field(frozen=True)]
    owner: RequiredString
    slug: RequiredString
    inputs: Annotated[Sequence[str], Field(frozen=True)]
    annotation: RequiredString
    license: RequiredString
    steps: Annotated[dict[str, StepInput], Field(frozen=True)]
