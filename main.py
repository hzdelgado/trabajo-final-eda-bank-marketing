import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# DATASET SOURCE: https://archive.ics.uci.edu/dataset/222/bank+marketing

def load_data(path):
    """Carga el dataset desde una ruta especificada."""
    return pd.read_csv(path, sep=';')

def clean_data(df):
    """Elimina duplicados y valores faltantes para asegurar calidad del dataset."""
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def calculate_age_range(df, output):
    """Crea rangos de edad y genera estadísticas descriptivas, exportándolas a CSV."""
    df['age_range'] = pd.cut(df['age'], 
                             bins=[0, 17, 29, 39, 49, 59, 69, 120], 
                             labels=['0-17', '18-29', '30-39', '40-49', '50-59', '60-69', '70+'],
                             right=True)
    age_stats = {
        "media": df["age"].mean(),
        "mediana": df["age"].median(),
        "moda": df["age"].mode()[0],
        "varianza": df["age"].var(),
        "minimo": df["age"].min(),
        "maximo": df["age"].max(),
    }
    
    df_stats = pd.DataFrame(age_stats, index=['edad'])
    os.makedirs(os.path.dirname(output), exist_ok=True)
    df_stats.to_csv(output)
    return df

def plot_calculate_age_range(df):
    """Genera un histograma del rango de edades de clientes."""
    plt.hist(df["age_range"], bins=10)
    plt.title("Histograma de rango de edad del Cliente")
    plt.xlabel('Rango de Edad')
    plt.ylabel('Cantidad')
    plt.show()

# Util para convertir duration a un string formateado
def seconds_to_minutes(seconds):
    """Convierte segundos a formato 'Xm Ys' para mayor facilidad interpretativa."""
    minutes = seconds // 60
    remaining = seconds % 60
    return f"{minutes}m {remaining}s"
    
def report_average_call_duration_per_job(df, output):
    """
    Calcula estadísticas de duración de llamadas por ocupación
    filtrando llamadas >60s para evitar ruido.
    """
    # Filtrar filas con llamadas de duracion mayor a 1 minuto (esta en segundos)
    df_filtrado = df.loc[df["duration"] > 60]
    
    table = df_filtrado.groupby("job")["duration"].agg(["mean", "median", "min", "max", "std"]).reset_index()
    
    # Conversión a formato amigable
    table["min_minutes"] = table["min"].apply(seconds_to_minutes)
    table["max_minutes"] = table["max"].apply(seconds_to_minutes)
    table["std_minutes"] = table["std"].round(0).apply(seconds_to_minutes)
    table["mean_minutes"] = table["mean"].apply(lambda x: seconds_to_minutes(int(x)))
    table["median_minutes"] = table["median"].apply(lambda x: seconds_to_minutes(int(x)))
    table_filter = table[["job", "min_minutes", "max_minutes", "std_minutes", "mean_minutes", "median_minutes"]]
    os.makedirs(os.path.dirname(output), exist_ok=True)
    table_filter.to_csv(output, index=False)
    return table

def plot_average_call_duration_per_job(df):
    """Gráfico de barras de duración promedio de llamada por tipo de trabajo."""
    sns.barplot(data=df, x="job", y="mean")
    plt.title("Duración de llamada promedio por Trabajo del Cliente")
    plt.xlabel("Trabajo")
    plt.ylabel("Segundos")
    plt.xticks(rotation=45, ha='right')
    plt.show()

def calculate_correlation_day_of_week_month_duration(df):
    """
    Analiza la variabilidad de duración de llamadas (std) según mes y estado civil,
    considerando solo clientes contactados por primera vez vía celular.
    """
    
    # Filtrar filas con clientes que han sido contactados por primera vez y contacto por celular
    df_filtrado = df.loc[(df["pdays"] == -1) & (df["contact"] == "cellular")]
    # Convertir la columna mes a categoria ordenada para poder ordenar la columna
    month_order = ["jan", "feb", "mar", "apr", "may", "jun",
               "jul", "aug", "sep", "oct", "nov", "dec"]
    df_filtrado["month"] = pd.Categorical(
        df_filtrado["month"],
        categories=month_order,
        ordered=True
    )

    table_std = (
        df_filtrado
        .groupby(["month","marital"])["duration"]
        .agg(std_duration="std")
        .sort_values(["month", "marital"], ascending=True)
    )
    return table_std
      
def plot_correlation_day_of_week_month_duration(df):
    """Genera heatmap de la desviación estándar de duración por mes y estado civil."""
    matrix = df.pivot_table(
        values="std_duration",
        index="month",
        columns="marital"
    )
    plt.figure(figsize=(10, 6))
    sns.heatmap(matrix, annot=True, fmt=".1f")
    plt.title("Desviación std de llamadas (segundos) por Mes y Estado Civil")
    plt.show()
    
def main():
    # 1️⃣ Ingesta
    df = load_data('data/bank-full.csv')

    # 2️⃣ Limpieza
    df_clean = clean_data(df)

    # 3️⃣ Transformaciones
    df_calculate_age_range = calculate_age_range(df_clean, output="data/processed/age_stats.csv")
    df_calculate_average_call_duration_per_job = report_average_call_duration_per_job(df_clean, output="data/processed/report_average_call_duration_per_job.csv")
    df_calculate_correlation_day_of_week_month_duration = calculate_correlation_day_of_week_month_duration(df_clean)
    # 4️⃣ Visualización
    plot_calculate_age_range(df_calculate_age_range)
    plot_average_call_duration_per_job(df_calculate_average_call_duration_per_job)
    plot_correlation_day_of_week_month_duration(df_calculate_correlation_day_of_week_month_duration)
    
if __name__ == "__main__":
    main()