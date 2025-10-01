import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# TÍTULO Y DESCRIPCIÓN
# -------------------------------
st.title("Análisis de Vehículos en Venta")
st.write("Aplicación con Streamlit usando el dataset **vehicles_us.csv**")

# -------------------------------
# CARGA DE DATOS
# -------------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("vehicles_us.csv")
    except FileNotFoundError:
        st.error("No se encontró el archivo 'vehicles_us.csv' en la carpeta del proyecto.")
        return None
    return df

df = load_data()

if df is not None:
    st.success("Datos cargados correctamente")

    # -------------------------------
    # EXPLORACIÓN INICIAL
    # -------------------------------
    st.subheader("Vista previa de los datos")
    st.dataframe(df.head())

    # -------------------------------
    # FILTRO POR TIPO DE VEHÍCULO
    # -------------------------------
    vehicle_types = df['type'].dropna().unique()
    selected_type = st.selectbox("Selecciona un tipo de vehículo:", options=vehicle_types)

    filtered_df = df[df['type'] == selected_type]

    st.write(f"Cantidad de vehículos tipo **{selected_type}**: {len(filtered_df)}")

    # -------------------------------
    # GRÁFICO DE PRECIOS
    # -------------------------------
    st.subheader("Distribución de precios por año del modelo")
    fig = px.scatter(filtered_df, x="model_year", y="price",
                     title=f"Precios de {selected_type} por año del modelo",
                     labels={"model_year": "Año del Modelo", "price": "Precio (USD)"},
                     opacity=0.7)
    st.plotly_chart(fig)

else:
    st.warning("Sube tu archivo `vehicles_us.csv` a la carpeta del proyecto.")
