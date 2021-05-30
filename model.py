from dataclasses import dataclass


@dataclass(frozen=True)
class Mnemonic:
        name: str
        jump_type: str
        label_name: str

