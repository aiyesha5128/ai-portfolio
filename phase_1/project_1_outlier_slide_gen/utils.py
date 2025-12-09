# utils.py
import matplotlib.pyplot as plt
import io
from PIL import Image
import pandas as pd

def plot_feature_hist(df: pd.DataFrame, column: str, bins: int = 30):
    """
    Returns a PIL.Image of a histogram for column in df.
    """
    fig, ax = plt.subplots(figsize=(6,4))
    df[column].hist(ax=ax, bins=bins)
    ax.set_title(f'Distribution of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Count')
    plt.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf)
