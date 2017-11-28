from . import GreedySolver
import numpy as np

class GreedyBestFirstSolver(GreedySolver):
    def __init__(self, roads, astar, scorer):
        super().__init__(roads, astar, scorer)

    # Find the next state to develop
    def _getNextState(self, problem, currState):
        successors = list(problem.expand(currState))
        min_score = self._scorer.compute(currState,successors[0])
        bestIdx = 0
        for s in successors:
            curr_score = self._scorer.compute(currState,s)
            if curr_score < min_score:
                min_score = curr_score
                bestIdx = successors.index(s)
        return successors[bestIdx]
