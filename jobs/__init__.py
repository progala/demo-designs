"""The __init__.py module is required for Nautobot to load the jobs via Git."""

from .device_controllers import ControllerDesign
from .device_modules import ModuleDesign
from .cloud_networks import CloudNetworkDesign
from .core_site import CoreSiteDesign
from .device_controllers import ControllerDesign
from .edge_site import EdgeDesign
from .initial_data import InitialDesign

__all__ = [
    "CloudNetworkDesign",
    "ControllerDesign",
    "CoreSiteDesign",
    "EdgeDesign",
    "InitialDesign",
    "ModuleDesign",
]
