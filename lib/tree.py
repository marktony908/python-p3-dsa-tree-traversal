class Tree:
    def __init__(self, root):
        """Initialize the Tree with a root node."""
        self.root = root

    def get_element_by_id(self, element_id):
        """Find a node by its ID using depth-first traversal."""
        def dfs(node):
            # Check if the current node matches the ID
            if node.get('id') == element_id:
                return node
            # Traverse children
            for child in node['children']:
                found = dfs(child)
                if found:
                    return found
            return None
        
        return dfs(self.root)

    def breadth_first_traversal(self):
        """Return a list of node values in breadth-first order."""
        result = []
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            result.append(current_node['value'])
            nodes_to_visit.extend(current_node['children'])

        return result

    def depth_first_traversal(self):
        """Return a list of node values in depth-first order."""
        result = []
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            result.append(current_node['value'])
            nodes_to_visit = current_node['children'] + nodes_to_visit

        return result


# Example usage:
if __name__ == "__main__":
    # Setting up a simple tree
    child_1 = {
        'value': 2,
        'id': 'child_1',
        'children': []
    }

    child_2 = {
        'value': 3,
        'id': 'child_2',
        'children': []
    }

    child_3 = {
        'value': 4,
        'id': 'child_3',
        'children': []
    }

    root = {
        'value': 1,
        'id': 'root',
        'children': [child_1, child_2, child_3]
    }

    tree = Tree(root)

    # Testing get_element_by_id
    print(tree.get_element_by_id('child_1'))  # Output: {'value': 2, 'id': 'child_1', 'children': []}
    print(tree.get_element_by_id('child_2'))  # Output: {'value': 3, 'id': 'child_2', 'children': []}
    print(tree.get_element_by_id('non_existent'))  # Output: None

    # Testing traversals
    print(tree.breadth_first_traversal())  # Output: [1, 2, 3, 4]
    print(tree.depth_first_traversal())    # Output: [1, 2, 3, 4]
