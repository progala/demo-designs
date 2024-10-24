"""The __init__.py module is required for Nautobot to load the jobs via Git."""

from .cloud_networks import CloudNetworkDesign
from .core_site import CoreSiteDesign
from .device_controllers import ControllerDesign
from .device_modules import ModuleDesign
from .edge_site import EdgeDesign
from .initial_data import InitialDesign
from .p2p import P2PDesign

__all__ = [
    "CloudNetworkDesign",
    "ControllerDesign",
    "CoreSiteDesign",
    "EdgeDesign",
    "InitialDesign",
    "ModuleDesign",
    "P2PDesign",
]
