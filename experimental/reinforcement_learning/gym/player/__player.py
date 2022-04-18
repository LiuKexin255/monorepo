from typing import Tuple

import numpy


class Player:
    """
    适用于 gym 的 player 基类。提供 action 函数，输入环境观测和行动空间，返回选择的行动
    """

    def action(self, obs: numpy.ndarray, action_space: numpy.ndarray, action_mask: numpy.ndarray = None) -> Tuple[None, int]:
        """
        输入环境的观测和行动空间，返回所选择的行动。

        obs: 环境的观测
        action_space: 行动空间
        action_mask: 行动掩码，由 0 和 1 组成的数组，与 action_space 结构相同。不可选择的行动对应的掩码设置为 0。

        return: player 选择的行动和对应的在行动空间中的 index
        """
        pass
