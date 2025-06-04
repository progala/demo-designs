"""The __init__.py module is required for Nautobot to load the jobs via Git."""

from .core_site import CoreSiteDesign
from .edge_site import EdgeDesign
from .initial_data import InitialDesign
from .p2p import P2PDesign

__all__ = [
    "CoreSiteDesign",
    "EdgeDesign",
    "InitialDesign",
    "P2PDesign",
]

def network_stringz(network: str) -> str:
    """Jinja2 filter to convert the IPNetwork object to a string.

    If an attribute is supplied, first lookup the attribute on the IPNetwork
    object, then convert the returned value to a string.

    Args:
        network (IPNetwork): Object to convert to string
        attr (str, optional): Optional attribute to retrieve from the IPNetwork prior
            to converting to a string. Defaults to "".

    Example:
    ```jinja
        {{ "1.2.3.4/24" | ip_network | network_string("ip") }}
    ```

    Returns:
        str: Converted object
    """
    return str(network)

def random_stuff(stuff: str) -> str:
    """Jinja2 filter to convert the IPNetwork object to a string.

    If an attribute is supplied, first lookup the attribute on the IPNetwork
    object, then convert the returned value to a string.

    Args:
        network (IPNetwork): Object to convert to string
        attr (str, optional): Optional attribute to retrieve from the IPNetwork prior
            to converting to a string. Defaults to "".

    Example:
    ```jinja
        {{ "1.2.3.4/24" | ip_network | network_string("ip") }}
    ```

    Returns:
        str: Converted object
    """
    return f"{stuff*5}"

from django.template import engines

jinja_env = engines['jinja'].env
jinja_env.filters['network_stringz'] = network_stringz
jinja_env.filters['random_stuff'] = random_stuff