# Coding Task Use Case

Have a look at the paper "Encoding independent Optimization Problem Formulation for Quantum Computing". There you find the definition of different encodings and optimization problems and a pipeline for automating quantum algorithm aggregation. Your task is to write a small Python module which executes one of the steps along the pipeline.
An example would be to write a Python module which encodes the cost function of a non-binary optimization problem like traveling salesperson or Knapsack in two different encodings (e.g. OneHot and Binary). The module could accept the data for the optimization problem in form of a JSON dict and output the encoded cost function in a format of your choice.
