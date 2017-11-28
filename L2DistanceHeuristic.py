from . import Heuristic
from ways import tools

# Use the L2 aerial distance (in meters)
class L2DistanceHeuristic(Heuristic):
    def estimate(self, problem, state):
        coord1 = problem._roads[problem.target.junctionIdx].coordinates
        coord2 = problem._roads[state.junctionIdx].coordinates
        return tools.compute_distance(coord1, coord2)

