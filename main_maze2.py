from maze import Maze
from bfs_agent import BFSAgent
from dfs_agent import DFSAgent
from ids import IDSAgent
from UCS import UCSAgent
from greedy import GreedyAgent
from a_star import A_StarAgent
from hill_climbing import HillClimbingAgent
from genetic import GeneticAgent
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

    # Genetic
    genetic_agent = GeneticAgent(maze,max_path_length=3000)
    path_genetic = genetic_agent.genetic()
    maze.plot(path_genetic, 'Genetic')