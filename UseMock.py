import socket
import unittest
from unittest.mock import patch
from main import read, sleep_and_execute


class TestRead(unittest.TestCase):

    @patch('main.socket.socket')
    def test_read(self, mock_socket):
        """
        Test the read function.

        :param mock_socket: Mock object for socket.socket
        """
        mock_sock_instance = mock_socket.return_value
        mock_sock_instance.recv.return_value = b"Love Israel"
        self.assertEqual(read(mock_sock_instance), b"Love Israel")

    @patch('main.sleep_and_execute')
    def test_sleep_and_execute(self, mock_sleep_and_execute):
        """
        Test the sleep_and_execute function.

        :param mock_sleep_and_execute: Mock object for sleep_and_execute
        """
        def mock_func():
            return 3 + 5

        mock_sleep_and_execute.side_effect = lambda func: func()

        self.assertEqual(sleep_and_execute(mock_func), 8)


if __name__ == '__main__':
    unittest.main()
