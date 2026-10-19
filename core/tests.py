from django.test import TestCase, override_settings


class UnknownUrlResponseTests(TestCase):
    @override_settings(DEBUG=False)
    def test_unknown_url_shows_standard_not_found_page(self):
        response = self.client.get('/no-existe/')

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, 'Not Found', status_code=404)
        self.assertNotContains(
            response,
            'Page not found (404)',
            status_code=404
        )
