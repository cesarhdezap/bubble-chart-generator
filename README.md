# Bubble chart generator

A python3 script for bubble chart generators with a csv 2-way matrix.

## Requirements

- pandas==1.3.5
- plotly==5.5.0

## How it works

Takes a csv file with a 2 dimensional matrix and converts it to a dictionary that can be plotted into a bubble-chart or scatter-chart by plotly.

You can modify the value of this variables:

- **csv_filename**: Csv filename with .csv extension
- **has_latin_encoding**: If your csv file has any latin characters
- **x_axis_name**: Name of the X axis on the chart
- **y_axis_name**: Name of the Y axis on the chart

## Data input example

|      | Col1 | Col2 | Col3 | Col4 |
| ---- | ---- | ---- | ---- | ---- |
| Row1 | 1    | 1    | 1    | 1    |
| Row2 | 0    | 2    | 0    | 2    |
| Row3 | 5    | 0    | 0    | 4    |
| Row4 | 1    | 2    | 0    | 1    |
| Row5 | 0    | 0    | 0    | 0    |
| Row6 | 1    | 1    | 0    | 2    |

## Chart example

![bubble chart](/figs/plot_example.png)
