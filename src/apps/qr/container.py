from dependency_injector import containers, providers

from src.storages import Storages


class QrContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    storages = providers.Container(Storages, config=config.storages)
