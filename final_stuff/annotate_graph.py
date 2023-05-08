import numpy as np
import matplotlib.pyplot as plt


def annotate_plot(annotations):
    """
    Annotate a plot using Pyplot's text function
    :param annotations: dict
        Dictionary whose keys are the labels (strings) to be annotated and
        values are dictionary with the following key-value pairs:
        :'string': str
            Text string for the text function
        :'position': ndarray, shape (2)
            x, y coordinates for the position of the textbox
        :'alignment': list, str, shape (2)
            horizontalalignment and verticalalignment values for the text
            function
        :'fontsize': float
            Value of the font size in pixels
    :return:
    """
    plt.text(annotations['position'][0], annotations['position'][1], annotations['string'],
             horizontalalignment=annotations['alignment'][0], verticalalignment=annotations['alignment'][1],
             fontsize=annotations['fontsize'])

    return


if __name__ == "__main__":
    from datetime import datetime
    import numpy as np
    annotations = {'string': f"Created by {__Ya_Boi__} {datetime.today().isoformat()}",
                   'position': np.array([4.75, 9.5]), 'alignment': ['left', 'bottom'], 'fontsize': 10}
    plt.plot(5, 10)
    plt.text(x=annotations['position'][0], y=annotations['position'][1], s=annotations['string'],
             horizontalalignment=annotations['alignment'][0], verticalalignment=annotations['alignment'][1],
             fontsize=annotations['fontsize'])
    plt.show()
