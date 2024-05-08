"""The __init__.py module is required for Nautobot to load the jobs via Git."""

from .cloud_networks import CloudNetworkDesign
from .core_site import CoreSiteDesign
from .device_controllers import ControllerDesign
from .device_modules import ModuleDesign
from .edge_site import EdgeDesign
from .initial_data import InitialDesign
from .l3vpn import L3vpnDesign

__all__ = [
    "CloudNetworkDesign",
    "ControllerDesign",
    "CoreSiteDesign",
    "EdgeDesign",
    "InitialDesign",
    "ModuleDesign",
    "L3vpnDesign",
]
