"""QEncode: serialization"""

import json
import pickle
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class InputTSPData:
    distance_matrix: list[list[int]]

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return cls(**data)


def write_cost_function(path_to_file: Path, expression: Any):
    path_to_file.touch()

    with open(path_to_file, "wb") as f:
        pickle.dump(expression, f)


def read_cost_function(path_to_file: Path) -> Any:
    if path_to_file.is_file():
        with open(path_to_file, "rb") as f:
            expression = pickle.load(f)

    return expression
