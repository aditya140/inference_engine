# Copyright 2022 MOSEC Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
import struct
from socket import socket
from typing import List, Union

from tests.mock_socket import socket as mock_socket


def imitate_controller_send(sock: Union[mock_socket, socket], l_data: List[bytes]):
    # explicit byte format here for sanity check
    # placeholder flag, should be discarded by receiver
    header = struct.pack("!H", 0) + struct.pack("!H", len(l_data))
    body = b""
    sent_ids = []
    sent_payloads = []
    for data in l_data:
        tid = struct.pack("!I", random.randint(1, 100))
        sent_ids.append(tid)
        sent_payloads.append(data)
        length = struct.pack("!I", len(data))
        body += tid + length + data

    sock.sendall(header + body)  # type: ignore
    return sent_ids, sent_payloads
