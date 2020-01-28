import argparse


def parse_args():
    """get arguments from command line"""
    parser = argparse.ArgumentParser(description='TheBot')
    parser.add_argument('--use_proxy', dest='proxy',
                        help='Proxy ip.\nExample: --use_proxy 10.10.1.10:3128', default=None, type=str)
    parser.add_argument('--file_dir', dest='path',
                        help='file directory where files will be stored', default=None, type=str)
    parser.print_help()
    return parser.parse_args()

