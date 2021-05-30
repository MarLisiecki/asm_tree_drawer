from dataclasses import dataclass


@dataclass
class Mnemonic:
    def __init__(self, name: str, label: str, jump_type: str):
        self.jump_type = jump_type
        self.label = label
        self.name = name
