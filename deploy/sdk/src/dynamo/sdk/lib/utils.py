# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import socket


def get_host_port():
    """Gets host and port for web worker from environment variables set at the top level by circus
    """
    # Check for web worker specific env vars first
    # If port is 0, uvicorn and OS will find us a good random port
    port = os.environ.get("DYN_WEB_WORKER_PORT", 0)
    host = os.environ.get("DYN_WEB_WORKER_HOST", "0.0.0.0")
    return host, int(port)
