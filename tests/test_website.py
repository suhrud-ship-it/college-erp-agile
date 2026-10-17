import pathlib
import unittest

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
HTML_FILE = PROJECT_ROOT / "index.html"


class CollegeERPWebsiteTests(unittest.TestCase):
    def test_homepage_exists(self):
        self.assertTrue(HTML_FILE.is_file())

    def test_homepage_has_valid_basic_structure(self):
        html = HTML_FILE.read_text(encoding="utf-8")
        self.assertIn("<!DOCTYPE html>", html)
        self.assertIn("<html lang=\"en\">", html)
        self.assertIn("</html>", html)

    def test_all_five_college_erp_features_exist(self):
        html = HTML_FILE.read_text(encoding="utf-8")
        features = [
            "Student Registration",
            "Course Registration",
            "Attendance Tracking",
            "Timetable Viewing",
            "Fee Payment Status",
        ]
        for feature in features:
            with self.subTest(feature=feature):
                self.assertIn(feature, html)


if __name__ == "__main__":
    unittest.main()
