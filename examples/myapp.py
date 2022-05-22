"""
Example program to show how to place multiple argument groups as tabs
"""

import argparse

from gooey import Gooey, GooeyParser
from message import display_message


@Gooey(program_name='Argument Groups Demo',
       tabbed_groups=True,
       navigation='Tabbed',
       dump_build_config=True,   # Dump the JSON Gooey uses to configure itself
       # Loads a JSON Gooey-generated configuration
       load_build_config='gooey_config.json',
       )
def main():
    settings_msg = 'Example program to show how to place multiple argument groups as tabs'
    parser = GooeyParser(description=settings_msg)

    group1 = parser.add_argument_group('General')
    group1.add_argument('--input',

                        help='input file path',
                        widget="FileChooser")

    group1.add_argument('--opt1', action='store_true',
                        help='Option one')

    group2 = parser.add_argument_group('Options')
    group2.add_argument('--opt2', action='store_true',
                        help='Option two')

    args = parser.parse_args()

    display_message()


if __name__ == '__main__':
    main()
