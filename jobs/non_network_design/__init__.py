"""Non-networking design demonstrates Design Builder support for general infrastructure data."""

from nautobot.apps.jobs import register_jobs, StringVar, ObjectVar
from nautobot.extras.models import Tenant

from nautobot_design_builder.design_job import DesignJob

from .context import NonNetworkingDesignContext


class NonNetworkingDesign(DesignJob):
    """A basic non-networking design job example for things like tenants, services, and virtualization."""

    tenant = ObjectVar(
        label="Tenant",
        description="Tenant associated with this infrastructure bundle",
        model=Tenant,
    )

    app_name = StringVar(
        label="Application Name",
        description="Logical name for the service or app (used for grouping)",
    )

    environment = StringVar(
        label="Environment",
        description="Environment this design applies to (e.g., dev, staging, prod)",
        default="dev",
    )

    has_sensitive_variables = False

    class Meta:
        """Metadata describing this non-network design job."""

        name = "Non-Networking Design"
        commit_default = False
        design_file = "non_networking_design/0001_design.yaml.j2"
        context_class = NonNetworkingDesignContext
        nautobot_version = ">=2"


name = "Demo Designs"
register_jobs(NonNetworkingDesign)
