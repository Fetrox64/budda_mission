from unittest import TestCase, main
from src.utils import logger


class GhaphTest(TestCase):

    def test(self):
        logger('Testing')
        self.assertTrue(3 < 5)


if __name__ == "__main__.py":
    main()
