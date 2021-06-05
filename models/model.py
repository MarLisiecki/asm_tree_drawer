from dataclasses import dataclass

# Mnemonic model which contains root label, target label, name of jump as mnemonic (e.g. jnp) and jump_type, which is
# the description of jump (e.g. Jump if not equal)
@dataclass(frozen=True)
class Mnemonic:
        name: str
        jump_type: str
        target_label: str
        root: str

