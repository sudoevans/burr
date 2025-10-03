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

import inspect
from typing import AsyncGenerator, AsyncIterable, Generator, List, TypeVar, Union

T = TypeVar("T")

GenType = TypeVar("GenType")

SyncOrAsyncIterable = Union[AsyncIterable[T], List[T]]
SyncOrAsyncGenerator = Union[Generator[GenType, None, None], AsyncGenerator[GenType, None]]
SyncOrAsyncGeneratorOrItemOrList = Union[SyncOrAsyncGenerator[GenType], List[GenType], GenType]


async def asyncify_generator(
    generator: SyncOrAsyncGenerator[GenType],
) -> AsyncGenerator[GenType, None]:
    """Convert a sync generator to an async generator.

    :param generator: sync generator
    :return: async generator
    """
    if inspect.isasyncgen(generator):
        async for item in generator:
            yield item
    else:
        for item in generator:
            yield item


async def arealize(maybe_async_generator: SyncOrAsyncGenerator[GenType]) -> List[GenType]:
    """Realize an async generator or async iterable to a list.

    :param maybe_async_generator: async generator or async iterable
    :return: list of items -- fully realized
    """
    if inspect.isasyncgen(maybe_async_generator):
        out = [item async for item in maybe_async_generator]
    else:
        out = [item for item in maybe_async_generator]
    return out
