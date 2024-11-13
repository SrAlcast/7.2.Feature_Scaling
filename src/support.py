import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generador_boxplots(df_list):
    # Filtra los DataFrames válidos
    df_list = [df for df in df_list if isinstance(df, pd.DataFrame)]
    
    if not df_list:
        print("Error: La lista no contiene DataFrames válidos.")
        return

    # Define los sufijos deseados
    sufijos_deseados = ('_stds', '_norm', '_minmax', '_robust')

    # Filtra las columnas de cada DataFrame para incluir solo las que tienen los sufijos deseados
    filtered_df_list = [df[[col for col in df.columns if col.endswith(sufijos_deseados)]] for df in df_list]

    # Configura la figura con una fila de subplots por DataFrame
    fig, axes = plt.subplots(nrows=len(filtered_df_list), ncols=max(len(df.columns) for df in filtered_df_list),
                             figsize=(6 * max(len(df.columns) for df in filtered_df_list), 4 * len(filtered_df_list)),
                             squeeze=False)  # Squeeze=False asegura una matriz 2D

    # Itera sobre cada DataFrame filtrado y cada columna
    for df_idx, df in enumerate(filtered_df_list):
        for col_idx, column in enumerate(df.columns):
            sns.boxplot(x=column, data=df, ax=axes[df_idx][col_idx])
            axes[df_idx][col_idx].set_title(f"DF {df_idx + 1} - {column}")

    # Oculta los ejes vacíos si hay menos columnas en algún DataFrame
    for df_idx, ax_row in enumerate(axes):
        for col_idx in range(len(filtered_df_list[df_idx].columns), axes.shape[1]):
            ax_row[col_idx].axis('off')

    # Ajuste de espaciado entre subplots
    plt.tight_layout()
    plt.show()