import argparse

from happy_paws import create_app


app = create_app()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='WIP.')
    parser.add_argument('-d', '--debug', action='store_true',
                    help='Enable debug mode.')
    args = parser.parse_args()
    print(f'Running with flags: {args}')
    app.run(debug=args.debug)