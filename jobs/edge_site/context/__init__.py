"""This module contains the render context for the basic design."""
import os
import uuid
from nautobot_design_builder.context import Context, context_file

from django_jinja import library

NAMESPACE_UUID = os.getenv("NAMESPACE_UUID", "12345678-1234-5678-1234-567812345678")

@context_file("context.yaml")
class EdgeDesignContext(Context):
    """Render context for basic design."""

    def deterministic_uuid(self, name: str, model: str) -> str:
        namespace = uuid.UUID(NAMESPACE_UUID)
        name = str(name).lower()
        model = str(model).lower()
        seed = f"{model}__{name}"
        # Generate and return a UUID using the uuid5 method, which combines the namespace and the name
        return str(uuid.uuid5(namespace, seed))
    
    @library.filter
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