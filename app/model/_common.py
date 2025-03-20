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

__author__: str = "David Meaux"
__version__: str = "0.0a1"

from typing import Any, Optional
from typing_extensions import Annotated

from pydantic import Field


Anything = Annotated[Any, Field(frozen=True)]
OptionalAnything = Annotated[Any, Field(frozen=True, default=None)]

OptionalBool = Annotated[Optional[bool], Field(strict=True,
                                               frozen=True,
                                               default=None,
                                               )]
RequiredBool = Annotated[bool, Field(frozen=True)]

OptionalInt = Annotated[Optional[int], Field(strict=True,
                                             frozen=True,
                                             default=None,
                                             )]
RequiredInt = Annotated[int, Field(frozen=True)]
NonNegativeInt = Annotated[int, Field(strict=True,
                                      frozen=True,
                                      ge=0,
                                      )]
OptionalNonNegativeInt = Annotated[Optional[int], Field(strict=True,
                                                        frozen=True,
                                                        ge=0,
                                                        default=None,
                                                        )]

NonNegativeIntDefault0 = Annotated[int, Field(strict=True,
                                              frozen=True,
                                              ge=0,
                                              default=0,
                                              )]

OptionalFloat = Annotated[Optional[float], Field(strict=True,
                                                 frozen=True,
                                                 default=None,
                                                 )]
RequiredFloat = Annotated[float, Field(frozen=True)]

OptionalString = Annotated[Optional[str], Field(strict=True,
                                                frozen=True,
                                                default=None,
                                                )]
RequiredString = Annotated[str, Field(frozen=True)]
