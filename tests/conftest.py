import pytest
from ragger.conftest import configuration
from ragger.navigator import NavInsID, NavIns
from ragger.backend import SpeculosBackend, BackendInterface

###########################
### CONFIGURATION START ###
###########################

# You can configure optional parameters by overriding the value of ragger.configuration.OPTIONAL_CONFIGURATION
# Please refer to ragger/conftest/configuration.py for their descriptions and accepted values

configuration.OPTIONAL.MAIN_APP_DIR = "tests/.test_dependencies/"

configuration.OPTIONAL.BACKEND_SCOPE = "class"

MNEMONIC = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
configuration.OPTIONAL.CUSTOM_SEED = MNEMONIC

#########################
### CONFIGURATION END ###
#########################

# Pull all features from the base ragger conftest using the overridden configuration
pytest_plugins = ("ragger.conftest.base_conftest", )

