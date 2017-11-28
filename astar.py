import numpy as np
import sys

class AStar:
    cost = None
    heuristic = None
    _cache = None
    shouldCache = None

    def __init__(self, heuristic, cost=None, shouldCache=False):
        self.heuristic = heuristic
        self.shouldCache = shouldCache
        self.cost = cost

        # Handles the cache. No reason to change this code.
        if self.shouldCache:
            self._cache = {}

    # Get's from the cache. No reason to change this code.
    def _getFromCache(self, problem):
        if self.shouldCache:
            return self._cache.get(problem)

        return None

    # Get's from the cache. No reason to change this code.
    def _storeInCache(self, problem, value):
        if not self.shouldCache:
            return

        self._cache[problem] = value

    # Run A*
    def run(self, problem):
        # Check if we already have this problem in the cache.
        # No reason to change this code.
        source = problem.initialState
        if self.shouldCache:
            res = self._getFromCache(problem)

            if res is not None:
                return res

        # Initializes the required sets
        closed_set = set()  # The set of nodes already evaluated.
        parents = {}  # The map of navigated nodes.

        # Save the g_score and f_score for the open nodes
        g_score = {source: 0}
        open_set = {source: self.heuristic.estimate(problem, problem.initialState)}

        developed = 0

        # TODO : Implement astar.
        # Tips:
        # - To get the successor states of a state with their costs, use: problem.expandWithCosts(state, self.cost)
        # - You should break your code into methods (two such stubs are written below)
        # - Don't forget to cache your result between returning it - TODO

        while (open_set):
            next_state = self._getOpenStateWithLowest_f_score(open_set)
            closed_set.add(next_state)
            if problem.isGoal(next_state):

                self._storeInCache(problem,self._reconstructPath(parents,next_state))
                return (self._reconstructPath(parents,next_state),g_score[next_state],self.heuristic.estimate(problem,problem.initialState),developed)
            for s in problem.expandWithCosts(next_state, self.cost):
                #s[0] => state
                #s[1] => cost
                developed += 1
                new_g = g_score[next_state] + s[1]
                if s[0] in open_set: #state s exists in open_set
                    old_node = s[0]
                    if (new_g < g_score[old_node]): # new parrent is better
                        g_score[old_node] = new_g
                        parents[old_node] = next_state
                        open_set[old_node] = new_g + self.heuristic.estimate(problem,old_node)
                    #else: #old path is better - DO NOTHING

                else: # state s not in open_set, maybe in closed
                    if closed_set.__contains__(s[0]): # a node with state s exists in closed_set
                        old_node = s[0]
                        if (new_g<g_score[old_node]): # new parrent is better
                            g_score[old_node] = new_g
                            parents[old_node] = next_state
                            open_set[old_node] =  new_g + self.heuristic.estimate(problem,old_node) # move old node from closed_set to open_set
                            closed_set.remove(old_node)
                        #else: #old path in better - DO NOTHING
                    else: #this is a new state - create new node
                        open_set[s[0]] = new_g + self.heuristic.estimate(problem,s[0])
                        g_score[s[0]] = new_g
                        parents[s[0]] = next_state
        return ([],-1, self.heuristic.estimate(problem, problem.initialState),developed)

    def _getOpenStateWithLowest_f_score(self, open_set):
        minState = min(open_set, key = open_set.get)
        del open_set[minState]
        return minState



    # Reconstruct the path from a given goal by its parent and so on
    def _reconstructPath(self, parents, goal):
        if (goal in parents):
            return self._reconstructPath(parents, parents[goal]) + [goal]
        else:
            return [goal]
