import unittest

from experimental.reinforcement_learning.gym.player import RandomPlayer

import numpy


class TestRandomPlayer(unittest.TestCase):
    """RandomPlayer 单元测试用例"""

    def test_action(self):
        """RandomPlayer.action 测试用例"""

        testcases = [
            {
                "name": "测试输入不带掩码",
                "args": {
                    "action_space": numpy.array(range(10)),
                    "epoch": 100,
                },
            }
        ]

        for case in testcases:
            args = case["args"]
            p = RandomPlayer()
            for _ in range(args["epoch"]):
                action, index = p.action(None, args["action_space"])
                self.assertIn(
                    action, args["action_space"], f'action {action} want in action_space f{args["action_space"]}')
                self.assertGreaterEqual(
                    index, 0, f'action index {index} want greater or equal than 0')
                self.assertLess(index, len(
                    args["action_space"]), f'action index {index} want less than {args["action_space"]}')

    def test_action_with_mask(self):
        """RandomPlayer.action 测试用例，带行动掩码"""

        testcases = [
            {
                "name": "测试输入带掩码，所有行动均可用",
                "args": {
                    "action_space": numpy.array((1, 2, 3)),
                    "action_mask": numpy.array((1, 1, 1)),
                    "epoch": 100,
                },
            },
            {
                "name": "测试输入带掩码，部分行动不可用",
                "args": {
                    "action_space": numpy.array((1, 2, 3)),
                    "action_mask": numpy.array((1, 0, 1)),
                    "epoch": 100,
                },
            }
        ]

        for case in testcases:
            args = case["args"]
            p = RandomPlayer()
            for _ in range(args["epoch"]):
                action, index = p.action(
                    None, args["action_space"], args["action_mask"])
                self.assertIn(
                    action, args["action_space"], f'action {action} want in action_space f{args["action_space"]}')
                self.assertGreaterEqual(
                    index, 0, f'action index {index} want greater or equal than 0')
                self.assertLess(index, len(
                    args["action_space"]), f'action index {index} want less than {args["action_space"]}')
                self.assertNotEqual(args["action_mask"][index], 0,
                                    f'action index mask {args["action_mask"][index]} want not 0')

    def test_action_none(self):
        """RandomPlayer.action 测试用例，一些异常情况"""

        testcases = [
            {
                "name": "输入行动空间为 []",
                "args": {
                    "action_space": numpy.array([]),
                    "action_mask": numpy.array([1, 1]),
                }
            },
            {
                "name": "掩码中没有有效行动",
                "args": {
                    "action_space": numpy.array((1, 2, 3, 4)),
                    "action_mask": numpy.array((0, 0, 0, 0)),
                },
            }
        ]

        for case in testcases:
            args = case["args"]
            p = RandomPlayer()
            action, index = p.action(
                None, args["action_space"], args["action_mask"])
            self.assertIsNone(action, f'action {action} want None')
            self.assertEqual(index, -1, f'action index {index} want -1')


if __name__ == "__main__":
    unittest.main()
