import datetime
import random
import os


EVERSHOP_URL = "https://demo.evershop.io/"

class TreeNode:
    def __init__(self, label, children=None, parent=None):
        self.label = label
        self.children = []
        self.parent = parent
        if children is not None:
            if isinstance(children, dict):
                for child_label, grand_children in children.items():
                    self.children.append(TreeNode(child_label, grand_children, self))
            else:
                self.children.append(TreeNode(children))

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.label) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def get_parents(self):
        """Return a list of all parent nodes up to the root."""
        parents = []
        node = self.parent
        while node:
            parents.append(node)
            node = node.parent
        return parents

def build_tree(data):
    return TreeNode(("Root", ""), data)

# Website sub-name, Website sub-path
ACTIONS_NAVIGATION = {
    ("Home", "/"): {
        ("Men", "/men"): {
            ("Strutter Shoes", "/strutter-shoes-45"): {
                ("Size L", "?size=6"): {
                    ("Color Black", "&color=14"): {},
                    ("Color White", "&color=18"): {},
                    ("Color Gray", "&color=23"): {},
                },
                ("Size XL", "?size=26"): {
                    ("Color Black", "&color=14"): {},
                    ("Color White", "&color=18"): {},
                    ("Color Gray", "&color=23"): {},
                },
            },
            ("Nike React Phantom Run Flyknit 2", "/nike-react-phantom-run-flyknit-2-179"): {
                ("Size X", "?size=4"): {
                    ("Color Black", "&color=14"): {},
                    ("Color Green", "&color=17"): {},
                    ("Color Pink", "&color=19"): {},
                },
                ("Size S", "?size=25"): {
                    ("Color Black", "&color=14"): {},
                    ("Color Green", "&color=17"): {},
                    ("Color Pink", "&color=19"): {},
                }
            },
        },
        ("Women", "/women"): {
            ("Alphaedge 4d Reflective Shoes R", "/alphaedge-4d-reflective-shoes-23"): {
                ("Size XL", "?size=26"): {
                    ("Color Black", "&color=14"): {},
                    ("Color White", "&color=18"): {},
                }
            },
            ("Edge Gameday Shoes", "/edge-gameday-shoes-30"): {
                ("Size L", "?size=6"): {
                    ("Color Red", "&color=7"): {},
                    ("Color Blue", "&color=8"): {},
                    ("Color Black", "&color=14"): {},
                    ("Color White", "&color=18"): {},
                },
                ("Size S", "?size=25"): {
                    ("Color Red", "&color=7"): {},
                    ("Color Blue", "&color=8"): {},
                    ("Color Black", "&color=14"): {},
                    ("Color White", "&color=18"): {},
                },
            }
        },
        ("Kids", "/kids"): {
            ("Swift Run X Shoes", "/swift-run-x-shoes-14") : {
                ("Size S", "?size=25"): {
                    ("Color Red", "&color=7"): {},
                    ("Color Black", "&color=14"): {},
                    ("Color Pink", "&color=19"): {},
                },
                ("Size XL", "?size=26"): {
                    ("Color Red", "&color=7"): {},
                    ("Color Black", "&color=14"): {},
                    ("Color Pink", "&color=19"): {},
                },
            },
            ("Coated Glitter Chuck Taylor All Star", "/coated-glitter-chuck-taylor-all-star-71"): {
                ("Size M", "?size=5"): {
                    ("Color Black", "&color=14"): {},
                    ("Color Purple", "&color=27"): {},
                },
                ("Size S", "?size=25"): {
                    ("Color Black", "&color=14"): {},
                    ("Color Purple", "&color=27"): {},
                },
            },
        },
        ("Cart", "/cart"): {
            ("Checkout", "/checkout"): {}
        },
        ("Account Login", "/login"): {

        },
        ("Account Register", "/register"): {

        }
    }
}

def write_sample_session_to_file(session_actions):
    # Generate a filename with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")
    filename = f"navigation_path_{timestamp}.txt"
    
    with open(os.path.dirname(os.path.abspath(__file__))+'/sample_sessions/'+filename, 'w') as file:
        for step in session_actions:
            file.write(step + '\n')

def generate_sample_session_actions(actions_tree, cart_node, num_steps_per_session):
    current_node = actions_tree
    steps_taken = 0
    path = []

    while steps_taken < num_steps_per_session:
        path.append(f"Node: {current_node.label[0]}\tFull URL: {(''.join([node.label[1] for node in current_node.get_parents()][::-1])+current_node.label[1]).replace("//", "/")}")
        
        # Decide whether to go deeper or go back up, with 90% chance
        if current_node.children and (random.random() > 0.1 or not current_node.parent):
            # Go deeper
            current_node = random.choice(current_node.children)
        # If at leaf node, go to cart with 50% chance
        elif not current_node.children and random.random() > 0.5:
            current_node = cart_node
        elif current_node.parent:
            # Go back up
            current_node = current_node.parent

        steps_taken += 1
    
    return path
    

def main(num_sessions, num_steps_per_session):
    print("Generating sample session files")
    actions_tree = build_tree(ACTIONS_NAVIGATION).children[0]
    cart_node = actions_tree.children[3]
    for i in range(num_sessions):
        session_actions = generate_sample_session_actions(actions_tree.children[0], cart_node, num_steps_per_session)
        write_sample_session_to_file(session_actions)

if __name__ == "__main__":
    num_sessions=10
    num_steps_per_session=30
    main(num_sessions, num_steps_per_session)