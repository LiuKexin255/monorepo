from typing import Tuple

import numpy

from . import *


class RandomPlayer(Player):
    """
    随机 Player，action 随机返回行动空间的一个可用行动
    """

    def action(self, obs: numpy.ndarray, action_space: numpy.ndarray, action_mask: numpy.ndarray = None) -> Tuple[None, int]:
        """
        随机返回行动空间中一个可用的行动
        """

        rand = numpy.random.normal(size=action_space.shape)
        if action_mask is not None:
            rand = rand * action_mask
        index = numpy.argmax(rand)
        return action_space[index], index
