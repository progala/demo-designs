"""Initial data required for modules."""
from nautobot.apps.jobs import register_jobs

from nautobot_design_builder.design_job import DesignJob
from nautobot_design_builder.contrib.ext import LookupExtension

from .context import ModuleDesignContext


class ModuleDesign(DesignJob):
    """Initialize the database with default values needed by the core site designs."""
    has_sensitive_variables = False

    class Meta:
        """Metadata needed to implement the backbone site design."""

        name = "Module Data"
        commit_default = False
        design_file = "designs/0001_design.yaml.j2"
        extensions = [LookupExtension]
        context_class = ModuleDesignContext
        has_sensitive_variables = False

name = "Nautobot Demo Designs"
register_jobs(ModuleDesign)
