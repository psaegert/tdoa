import argparse


def main(argv: str = None) -> None:
    parser = argparse.ArgumentParser(description='TDOA')
    _ = parser.add_subparsers(dest='command_name', required=True)

    # Evaluate input
    args = parser.parse_args(argv)

    # Execute the command
    match args.command_name:
        case 'demo':
            print('Demo')
        case _:
            parser.print_help()


if __name__ == '__main__':
    main()
