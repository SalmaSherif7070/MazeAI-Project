import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from maze import Maze
from uninformed.bfs_agent import BFSAgent
from uninformed.dfs_agent import DFSAgent
from uninformed.ids import IDSAgent
from uninformed.UCS import UCSAgent
from heuristic.greedy import GreedyAgent
from heuristic.a_star import A_StarAgent
from localsearch.hill_climbing import HillClimbingAgent
from localsearch.simulated import Simulated
from localsearch.genetic import GeneticAgent
from localsearch.stochastic_hill_climbing import StochasticHillClimbingAgent
from localsearch.first_choice_hill_climbing import FirstChoiceHillClimbingAgent
from localsearch.steepest_ascent_hill_climbing import SteepestAscentHillClimbingAgent
import json

with open('Mazes json\maze2.json', 'r') as file:
    maze2 = json.load(file)

if __name__ == "__main__":
    maze = Maze(maze2)

    # BFS
    bfs_agent = BFSAgent(maze)
    path_bfs = bfs_agent.bfs()
    maze.print_maze(path_bfs)
    maze.plot(path_bfs, 'BFS')

    # DFS
    dfs_agent = DFSAgent(maze)
    path_dfs = dfs_agent.dfs()
    maze.plot(path_dfs, 'DFS')

    # IDS
    ids_agent = IDSAgent(maze)
    path_ids = ids_agent.ids()
    maze.plot(path_ids, 'IDS')

    #UCS
    ucs_agent = UCSAgent(maze)
    path_ucs = ucs_agent.ucs()
    maze.plot(path_ucs, 'UCS')

    #Greedy
    greedy_agent = GreedyAgent(maze)
    path_greedy = greedy_agent.greedy()
    maze.plot(path_greedy, 'greedy')

    #AStar
    astar_agent = A_StarAgent(maze)
    path_astar = astar_agent.a_star()
    maze.plot(path_astar, 'astar')

    # Hill Climbing
    hill_climbing_agent = HillClimbingAgent(maze)
    path_hill_climbing = hill_climbing_agent.hill_climbing()
    maze.plot(path_hill_climbing, 'Hill Climbing')
    
    # Stochastic Hill Climbing
    stochastic_hill_climbing_agent = StochasticHillClimbingAgent(maze)
    path_stochastic_hill_climbing = stochastic_hill_climbing_agent.stochastic_hill_climbing()
    maze.plot(path_stochastic_hill_climbing, 'Stochastic Hill Climbing')

    # First Choice Hill Climbing
    first_choice_agent = FirstChoiceHillClimbingAgent(maze)
    path_first_choice = first_choice_agent.first_choice_hill_climbing()
    maze.plot(path_first_choice, 'First-Choice Hill Climbing')

    # Simulated Annealing
    sa = Simulated(maze)
    path_sa = sa.simulated_annealing()
    maze.plot(path_sa, "Simulated Annealing")

    # Genetic
    genetic_agent = GeneticAgent(maze,max_path_length=2000)
    path_genetic = genetic_agent.genetic()
    maze.plot(path_genetic, 'Genetic')