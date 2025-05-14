def is_valid_git_tree(tree_map):
    """
    Determines if a given tree structure represents a valid Git tree.

    A valid Git tree should:
    1. Have exactly one root (no parent).
    2. Contain no cycles.

    Args:
        tree_map: a dictionary representing the Git tree (commit ID to list of child commit IDs)

    Returns:
        True if the tree is a valid Git tree, False otherwise
    """
    parent_map = {}
    for node, children in tree_map.items():
        if node not in parent_map:
            parent_map[node] = []

        for child in children:
            if child not in parent_map:
                parent_map[child] = [node]
            else:
                parent_map[child].append(node)

    roots = [node for node, parents in parent_map.items() if not parents]
    if len(roots) != 1:
        return False

    visited = set()
    in_current_path = set()

    def has_cycle(node):
        if node in in_current_path:
            return True

        if node in visited:
            return False

        visited.add(node)
        in_current_path.add(node)

        for child in tree_map.get(node, []):
            if has_cycle(child):
                return True

        in_current_path.remove(node)
        return False

    return not has_cycle(roots[0])


if __name__ == '__main__':
    valid_tree = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": [],
        "D": []
    }

    invalid_tree = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]  # cycle
    }

    print(f"Is valid tree: {is_valid_git_tree(valid_tree)}")  # Should be True
    print(f"Is valid tree: {is_valid_git_tree(invalid_tree)}")  # Should be False