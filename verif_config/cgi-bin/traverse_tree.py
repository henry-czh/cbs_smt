
tree = {
    'name': 'C',
    'children':
    [
        {
            'name': 'C1',
            'children':
            [
                {
                    'name': 'C1.1',
                    'children': [
                        {
                            'name': 'C1.1.1'
                        },
                        {
                            'name': 'C1.1.2'
                        },
                        {
                            'name': 'C1.1.3'
                        }
                    ]
                },
                {
                    'name': 'C1.2',
                    'children': [
                        {
                            'name': 'C1.2.1'
                        },
                        {
                            'name': 'C1.2.2'
                        },
                        {
                            'name': 'C1.2.3'
                        }
                    ]
                },
                {
                    'name': 'C1.3',
                    'children': [
                        {
                            'name': 'C1.3.1'
                        },
                        {
                            'name': 'C1.3.2'
                        },
                        {
                            'name': 'C1.3.3'
                        }
                    ]
                }
            ]
        },
        {
            'name': 'C2',
            'children':
            [
                {
                    'name': 'C2.1',
                    'children': [
                        {
                            'name': 'C2.1.1'
                        },
                        {
                            'name': 'C2.1.2'
                        },
                        {
                            'name': 'C2.1.3'
                        }
                    ]
                },
                {
                    'name': 'C2.2',
                    'children': [
                        {
                            'name': 'C2.2.1'
                        },
                        {
                            'name': 'C2.2.2'
                        },
                        {
                            'name': 'C2.2.3'
                        }
                    ]
                },
                {
                    'name': 'C2.3',
                    'children': [
                        {
                            'name': 'C2.3.1'
                        },
                        {
                            'name': 'C2.3.2'
                        },
                        {
                            'name': 'C2.3.3'
                        }
                    ]
                }
            ]
        }
    ]
}

def TraverseTree0(tree):
    print(tree['name'])
    if not tree.has_key('children'):
        return
    for child in tree['children']:
        TraverseTree0(child)

ok = False
lst = []
def TraverseTree(tree, name):
    global ok
    lst.append(tree['name'])
    if tree['name'] == name:
        TraverseTree0(tree)
        ok = True
        return
    if not tree.has_key('children'):
        return
    for child in tree['children']:
        TraverseTree(child, name)
        if ok:
            break
        lst.pop()

TraverseTree(tree, 'C2.2')
print(lst)
