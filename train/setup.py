
from distutils.core import setup

setup(
    name="salsamodules",
    version="0.1.0",
    description="Modules used by SalsaNext",
    packages=[
        "tasks",
        "tasks.semantic",
        "tasks.semantic.modules",
        "common",
        "common.sync_batchnorm",
    ]
)
