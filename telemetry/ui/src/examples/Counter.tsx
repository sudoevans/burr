/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

import { Link } from 'react-router-dom';

export const Counter = () => {
  return (
    <div className="flex justify-center items-center h-full w-full">
      <p className="text-gray-700">
        {' '}
        This is a WIP! Please check back soon or comment/vote/contribute at the{' '}
        <Link
          className="hover:underline text-dwlightblue"
          to="https://github.com/DAGWorks-Inc/burr/issues/69"
        >
          github issue
        </Link>
        .
      </p>
    </div>
  );
};
