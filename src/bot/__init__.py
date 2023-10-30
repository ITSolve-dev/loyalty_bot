from settings import settings

from .container import DirectorContainer

DirectorContainer.config.from_dict(settings.bot.model_dump())
container = DirectorContainer()
container.wire(packages=["src.apps"])

__all__ = (
    "DirectorContainer",
    "container",
)
