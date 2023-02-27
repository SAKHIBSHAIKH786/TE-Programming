def astar(start_node, goal_node):
  open_set = set([start_node])
  closed_set = set()
  
  g_score = {start_node:0}
  f_score = {start_node:start_node.heuristic(goal_node)}
  parent=0
  
  while open_set:
    current = min(open_set, key=lambda node:f_score[node])
