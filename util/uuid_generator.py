import uuid
import os

def uuid_v4():
    return "fake_UUID" if 'TEST' in os.environ else uuid.uuid4()

