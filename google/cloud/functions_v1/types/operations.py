# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.protobuf import any_pb2 as any  # type: ignore
from google.protobuf import timestamp_pb2 as timestamp  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.functions.v1",
    manifest={"OperationType", "OperationMetadataV1",},
)


class OperationType(proto.Enum):
    r"""A type of an operation."""
    OPERATION_UNSPECIFIED = 0
    CREATE_FUNCTION = 1
    UPDATE_FUNCTION = 2
    DELETE_FUNCTION = 3


class OperationMetadataV1(proto.Message):
    r"""Metadata describing an [Operation][google.longrunning.Operation]

    Attributes:
        target (str):
            Target of the operation - for example
            projects/project-1/locations/region-1/functions/function-1
        type (~.operations.OperationType):
            Type of operation.
        request (~.any.Any):
            The original request that started the
            operation.
        version_id (int):
            Version id of the function created or updated
            by an API call. This field is only populated for
            Create and Update operations.
        update_time (~.timestamp.Timestamp):
            The last update timestamp of the operation.
        build_id (str):
            The Cloud Build ID of the function created or
            updated by an API call. This field is only
            populated for Create and Update operations.
    """

    target = proto.Field(proto.STRING, number=1)

    type = proto.Field(proto.ENUM, number=2, enum="OperationType",)

    request = proto.Field(proto.MESSAGE, number=3, message=any.Any,)

    version_id = proto.Field(proto.INT64, number=4)

    update_time = proto.Field(proto.MESSAGE, number=5, message=timestamp.Timestamp,)

    build_id = proto.Field(proto.STRING, number=6)


__all__ = tuple(sorted(__protobuf__.manifest))