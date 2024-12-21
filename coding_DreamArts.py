def parse_input():
    # 標準入力から1行ずつデータを取得
    input_lines = []
    while True:
        try:
            line = input()
            if line.strip():
                input_lines.append(line.strip())
        except EOFError:
            break
    # データの整理
    edges = []
    for line in input_lines:
        parts = [x.strip() for x in line.split(",")]
        start, end, distance = int(parts[0]), int(parts[1]), float(parts[2])
        edges.append((start, end, distance))
    return edges

def find_longest_path(edges):
    longest_distance = 0
    longest_path = []
    # グラフを構築
    graph = {}
    for start, end, distance in edges:
        if start not in graph:
            graph[start] = []
        graph[start].append((end, distance))
        if end not in graph:
            graph[end] = []

    def dfs(node, visited, path, current_distance):
        nonlocal longest_distance, longest_path

        # 現在の経路を更新
        visited.add(node)
        path.append(node)

        # 現在の経路が最長なら記録
        if current_distance > longest_distance:
            longest_distance = current_distance
            longest_path = path[:]
        
        # 隣接ノードを探索
        if node in graph:
            for neighbor, dist in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited, path, current_distance + dist)
        # 探索終了後にvisitedを開放
        visited.remove(node)
        path.pop()

    # 全ノードを始点として探索
    for start_node in graph.keys():
        dfs(start_node, set(), [], 0)
        # 最後のノードから最初のノードへの戻り経路が存在するか
        for neighbor, dist in graph[longest_path[-1]]:
            if neighbor == longest_path[0]:
                # 経路が存在する場合、戻りの距離を加算
                longest_path.append(longest_path[0])
                longest_distance += dist
                break
    return longest_path

if __name__ == "__main__":
    # 入力データのパース
    edges = parse_input()
    # 最長経路の探索
    longest_path= find_longest_path(edges)
    # 結果の出力
    for node in longest_path:
        print(node)