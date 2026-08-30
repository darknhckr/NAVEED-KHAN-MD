"""Compatibility adapter for the Telegram bot's proxy harvester import."""

from types import SimpleNamespace

from proxy_manager import ProxyManager


class ProxyHarvester(ProxyManager):
    """ProxyManager-backed harvester used by the Telegram bot."""

    def __init__(self, config=None):
        if config is None:
            config = SimpleNamespace(
                MIN_WORKING_PROXIES=5,
                PROXY_SOURCES=[],
                PROXY_TEST_URLS=["https://httpbin.org/ip"],
            )
        super().__init__(config)
