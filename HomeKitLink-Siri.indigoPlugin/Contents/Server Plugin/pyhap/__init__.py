import os
import logging

ROOT = os.path.abspath(os.path.dirname(__file__))
RESOURCE_DIR = os.path.join(ROOT, "resources")

CHARACTERISTICS_FILE = os.path.join(RESOURCE_DIR, "characteristics.json")
SERVICES_FILE = os.path.join(RESOURCE_DIR, "services.json")

logger = logging.getLogger("Plugin.HomeKit_pyHap")
# Flag if QR Code dependencies are installed.
# Installation with `pip install HAP-python[QRCode]`.
SUPPORT_QR_CODE = True
try:
    import base36  # noqa: F401
    import pyqrcode  # noqa: F401

    SUPPORT_QR_CODE = True
except ImportError:
    pass
