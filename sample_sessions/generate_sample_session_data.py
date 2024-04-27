EVERSHOP_URL = "https://demo.evershop.io/"

class TreeNode:
    def __init__(self, label, children=None):
        self.label = label
        self.children = []
        if children:
            for child_label, grand_children in children.items():
                self.children.append(TreeNode(child_label, grand_children))

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.label) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

def build_tree(data):
    return TreeNode(("Root", ""), data)

# Website sub-name, Website sub-path
ACTIONS_NAVIGATION = {
    ("Home", "/"): {
        ("Men", "/men"): {
            ("Strutter Shoes", "/strutter-shoes-45"): {
                ("Size L", "?size=6"): {
                    ("Color Black", "&color=14"),
                    ("Color White", "&color=18"),
                    ("Color Gray", "&color=23"),
                },
                ("Size XL", "?size=26"): {
                    ("Color Black", "&color=14"),
                    ("Color White", "&color=18"),
                    ("Color Gray", "&color=23"),
                },
            },
            ("Nike React Phantom Run Flyknit 2", "/nike-react-phantom-run-flyknit-2-179"): {
                ("Size X", "?size=4"): {
                    ("Color Black", "&color=14"),
                    ("Color Green", "&color=17"),
                    ("Color Pink", "&color=19"),
                },
                ("Size S", "?size=25"): {
                    ("Color Black", "&color=14"),
                    ("Color Green", "&color=17"),
                    ("Color Pink", "&color=19"),
                }
            },
        },
        ("Women", "/women"): {
            ("Alphaedge 4d Reflective Shoes R", "/alphaedge-4d-reflective-shoes-23"): {
                ("Size XL", "?size=26"): {
                    ("Color Black", "&color=14"),
                    ("Color White", "&color=18"),
                }
            },
            ("Edge Gameday Shoes", "/edge-gameday-shoes-30"): {
                ("Size L", "?size=6"): {
                    ("Color Red", "&color=7"),
                    ("Color Blue", "&color=8"),
                    ("Color Black", "&color=14"),
                    ("Color White", "&color=18"),
                },
                ("Size S", "?size=25"): {
                    ("Color Red", "&color=7"),
                    ("Color Blue", "&color=8"),
                    ("Color Black", "&color=14"),
                    ("Color White", "&color=18"),
                },
            }
        },
        ("Kids", "/kids"): {
            ("Swift Run X Shoes", "/swift-run-x-shoes-14") : {
                ("Size S", "?size=25"): {
                    ("Color Red", "&color=7"),
                    ("Color Black", "&color=14"),
                    ("Color Pink", "&color=19"),
                },
                ("Size XL", "?size=26"): {
                    ("Color Red", "&color=7"),
                    ("Color Black", "&color=14"),
                    ("Color Pink", "&color=19"),
                },
            },
            ("Coated Glitter Chuck Taylor All Star", "/coated-glitter-chuck-taylor-all-star-71"): {
                ("Size M", "?size=5"): {
                    ("Color Black", "&color=14"),
                    ("Color Purple", "&color=27"),
                },
                ("Size S", "?size=25"): {
                    ("Color Black", "&color=14"),
                    ("Color Purple", "&color=27"),
                },
            },
        },
        ("Cart", "/cart"): {
            ("Checkout", "/checkout")
        },
        ("Account Login", "/login"): {

        },
        ("Account Register", "/register"): {

        }
    }
}

def write_sample_session_to_file(i, session_actions):
    pass

def generate_sample_session_actions(actions_tree, num_steps_per_session):
    pass
    

def main(num_sessions, num_steps_per_session):
    print("Generating sample session files")
    actions_tree = build_tree(ACTIONS_NAVIGATION)
    for i in range(num_sessions):
        session_actions = generate_sample_session_actions(actions_tree, num_steps_per_session)
        write_sample_session_to_file(i, session_actions)

if __name__ == "__main__":
    num_sessions=10
    num_steps_per_session=10
    main(num_sessions, num_steps_per_session)