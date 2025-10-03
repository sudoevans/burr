# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import json

import pydantic
import pytest

from burr.core import serde
from burr.integrations.opentelemetry import convert_to_otel_attribute


class SampleModel(pydantic.BaseModel):
    foo: int
    bar: bool


@pytest.mark.parametrize(
    "value, expected",
    [
        ("hello", "hello"),
        (1, 1),
        ((1, 1), [1, 1]),
        ((1.0, 1.0), [1.0, 1.0]),
        ((True, True), [True, True]),
        (("hello", "hello"), ["hello", "hello"]),
        (SampleModel(foo=1, bar=True), json.dumps(serde.serialize(SampleModel(foo=1, bar=True)))),
    ],
)
def test_convert_to_otel_attribute(value, expected):
    assert convert_to_otel_attribute(value) == expected
