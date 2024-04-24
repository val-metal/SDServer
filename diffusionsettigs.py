import argparse
class DiffusionSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.interference = None
        self.pipeto = None
        self.size = None

    def load_from_command_line(self):
        parser = argparse.ArgumentParser(description='Diffusion Settings')
        parser.add_argument('--interference', type=str, help='Interference parameter')
        parser.add_argument('--pipeto', type=str, help='Pipeto parameter')
        parser.add_argument('--size', type=int, help='Size parameter')
        args = parser.parse_args()

        self.interference = args.interference
        self.pipeto = args.pipeto
        self.size = args.size