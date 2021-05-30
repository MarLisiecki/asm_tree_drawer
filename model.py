from dataclasses import dataclass


@dataclass(frozen=True)
class Mnemonic:
        name: str
        jump_type: str
        target_label: str
        root: str

