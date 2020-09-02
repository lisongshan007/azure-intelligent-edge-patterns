# -*- coding: utf-8 -*-
"""App.
"""

import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class ImagesConfig(AppConfig):
    """App Config.
    """
    name = 'vision_on_edge.images'

    def ready(self):
        """ready.
        """
        # pylint: disable = unused-import, import-outside-toplevel
        from . import signals
