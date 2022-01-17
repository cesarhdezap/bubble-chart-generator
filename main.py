import pandas as pd
import plotly.express as px

csv_filename = 'data.csv'
has_latin_encoding = True
x_axis_name = 'X'
y_axis_name = 'Y'

if has_latin_encoding:
    data_frame = pd.read_csv(csv_filename, sep=',', encoding='latin-1')
else:
    data_frame = pd.read_csv(csv_filename, sep=',')


def convert_matrix_to_dict():
    columns = list(data_frame.columns.values)
    categories = columns.pop(0)

    dict = {
        y_axis_name: [],
        x_axis_name: [],
        'bubble_size': []
    }

    for rowIndex in data_frame.index:
        for column in columns:
            y = data_frame[categories][rowIndex]
            x = column
            size = data_frame[column][rowIndex]

            if size > 0:
                dict[y_axis_name].append(y)
                dict[x_axis_name].append(x)
                dict['bubble_size'].append(size)

    return pd.DataFrame.from_dict(dict)


data = convert_matrix_to_dict()

fig = px.scatter(data, x='X', y="Y", size="bubble_size", color='bubble_size')

fig.update_layout(
    {
        'plot_bgcolor': 'rgba(130, 130, 144, 0.1)',
        'paper_bgcolor': 'rgba(130, 130, 144, 0.1)',
    })

fig.show()
