# -*- coding: utf-8 -*-
"""App drf url tests.
"""

from unittest import mock

import pytest
from django.urls import resolve, reverse

from .factories import CameraFactory

pytestmark = pytest.mark.django_db


@mock.patch("vision_on_edge.cameras.models.Camera.verify_rtsp",
            mock.MagicMock(return_value=True))
def test_view_detail():
    """test_view_detail.

    Args:
        camera (Camera): camera
    """
    cam_1 = CameraFactory()
    cam_1.save()
    assert (reverse("api:camera-detail",
                    kwargs={"pk": cam_1.id}) == f"/api/cameras/{cam_1.id}")
    assert resolve(f"/api/cameras/{cam_1.id}").view_name == "api:camera-detail"


def test_view_list():
    """test_view_list.
    """
    assert reverse("api:camera-list") == "/api/cameras"
    assert resolve("/api/cameras").view_name == "api:camera-list"