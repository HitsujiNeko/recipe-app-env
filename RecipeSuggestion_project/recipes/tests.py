from django.test import TestCase
from .utils import extract_youtube_thumbnail

class UtilsTestCase(TestCase):
    def test_extract_youtube_thumbnail_standard_url(self):
        url = "https://www.youtube.com/watch?v=UOzLY-2aJ30"
        expected_thumbnail = "https://img.youtube.com/vi/UOzLY-2aJ30/maxresdefault.jpg"
        self.assertEqual(extract_youtube_thumbnail(url), expected_thumbnail)

    def test_extract_youtube_thumbnail_short_url(self):
        url = "https://youtu.be/UOzLY-2aJ30"
        expected_thumbnail = "https://img.youtube.com/vi/UOzLY-2aJ30/maxresdefault.jpg"
        self.assertEqual(extract_youtube_thumbnail(url), expected_thumbnail)

    def test_extract_youtube_thumbnail_invalid_url(self):
        url = "https://www.example.com/watch?v=invalid"
        self.assertIsNone(extract_youtube_thumbnail(url))