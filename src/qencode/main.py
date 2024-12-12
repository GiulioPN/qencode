"""QEncode module: main"""

from pathlib import Path

from qencode.encodings.binary import apply_binary_delta, build_binary_variables
from qencode.io.serialization import InputTSPData, write_cost_function
from qencode.tsp.cost_function import build_cost_function

if __name__ == "__main__":
    input_tsp_data = InputTSPData.from_json("samples/data_3d.json")

    vars = build_binary_variables(len(input_tsp_data.distance_matrix))

    cost_function = build_cost_function(
        input_tsp_data.distance_matrix, vars, apply_binary_delta
    )

    output_path = Path("binary_cost_function.dat")
    write_cost_function(Path(output_path), cost_function)
