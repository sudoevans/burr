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

import pandas as pd

from burr.core import serde, state


def test_serde_of_pandas_dataframe(tmp_path):
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    og = state.State({"df": df})
    serialized = og.serialize(pandas_kwargs={"path": tmp_path})
    assert serialized["df"][serde.KEY] == "pandas.DataFrame"
    assert serialized["df"]["path"].startswith(str(tmp_path))
    assert (
        "df_a23d165ed4a2b8c6ccf24ac6276e35a9dc312e2828b4d0810416f4d47c614c7f.parquet"
        in serialized["df"]["path"]
    )
    ng = state.State.deserialize(serialized, pandas_kwargs={"path": tmp_path})
    assert isinstance(ng["df"], pd.DataFrame)
    pd.testing.assert_frame_equal(ng["df"], df)
