# Copyright (c) 2021 - present / Neuralmagic, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Input/Output Schemas for Image Classification.
"""

from typing import Any, List, Union

from pydantic import BaseModel, Field


class ImageClassificationInput(BaseModel):
    """
    Input model for image classification
    """

    images: Union[str, List[str], List[Any]] = Field(
        description="List of Images to process"
    )

    class Config:
        arbitrary_types_allowed = True


class ImageClassificationOutput(BaseModel):
    """
    Output model for image classification
    """

    labels: List[Union[int, str]] = Field(
        description="List of labels, one for each prediction"
    )
    scores: List[float] = Field(description="List of scores, one for each prediction")
