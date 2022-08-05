from pywidevine.device import Device
from pathlib import Path

import click


def main():
    device = Device(
        type_=Device.Types.ANDROID,
        security_level=3,
        flags=None,
        private_key=Path(r"./devices/private_key.pem").read_bytes(),
        client_id=Path(r"./devices/client_id.bin").read_bytes()
    )
# save it to a .wvd file for easier loading next time
    device.dump(r"./devices/device.wvd")
