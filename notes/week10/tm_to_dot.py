import sys
print('digraph {')
print("  graph [overlap=false];")
nodes = set()
edges = set()
for line in open(sys.argv[1]):
    if line.startswith('//'): continue
    q, a, r, b, d = line.split()
    nodes.add(q)
    nodes.add(r)
    edges.add((q,r))
for q in nodes:
    print ('  n{} [shape=circle,label=""]'.format(q))
for q, r in edges:    
    print ('  n{} -> n{}'.format(q, r))
print('}')
