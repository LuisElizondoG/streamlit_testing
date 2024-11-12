import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración Base de la Página
st.set_page_config(layout="wide",
                page_title="Testeando Streamlit | Equipo 2",
                initial_sidebar_state="collapsed"
)

# Estilos CSS
st.markdown(
    """
<style>
    [data-testid="stBaseButton-headerNoPadding"] {
        display: None
    }

    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0);
    } 
 
    .main > div {
        padding-top: 4rem;

    }

    button[kind="primary"] { 
        height: 50px; 
        width: 100%;
        border: solid .05em rgba(0,0,0,0);  
        background-color: #2b4eed;
        color: #white;
        border-radius: 30px;
    }

</style>
""",
    unsafe_allow_html=True,
)



# Header
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        .header {{
            background-color: #1E90FF;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-family: Poppins', sans-serif;
            
        }}

        .header h2 {{
            color: white;
            margin: 0;
            padding-bottom: 1px;
            font-size: 24px; /* Ajusta el tamaño según tu preferencia */
            font-family: 'Poppins', sans-serif;
        }}
        .header h3 {{
            color: white;
            margin: 0;
            padding-bottom: 1px;
            font-size: 14px; /* Ajusta el tamaño según tu preferencia */
            font-family: 'Poppins', sans-serif;
        }}

        .line {{
            width: 30%; /* Ajusta el ancho de la línea */
            height: 1px;
            background-color: white;
            margin: 10px auto; /* Centra la línea */
        }}

        .icon {{
            width: 50px; /* Ajusta el tamaño del ícono */
            margin-bottom: 10px;
        }}

    </style>
    <div class="header">
        <img src="https://upload.wikimedia.org/wikipedia/commons/4/47/Logo_del_ITESM.svg" class="icon">
        <h2>Testeando Streamlit</h2>
        <div class="line"></div>
        <h3>Luis Angel Elizondo Gallegos | A01198186</h3>
        <h3>Carlos Daniel Cárdenas Cortés | A01771313</h3>
        <h3>Carolina Valdez González | A00834042</h3>
        <h3>Rebeca Gancedo Ontaneda | A00832869 </h3>
        <h3>Jesus Arnulfo Cazarez Gomez | A00835040</h3>

    </div>
    <br>
    """,
    unsafe_allow_html=True
)

# Cargar Archivo de Excel
df = pd.read_excel("vendedores.xlsx")
df["EMPLEADO"] = df["NOMBRE"] + df["APELLIDO"]

###########################   Obtención de Opciones y Creación de Filtros ##################

# Separación de Columnas
c1,c2 = st.columns([1,4])
with c1:
    # Opciones del Filtro Región
    region = st.selectbox("**Region**", options= ["Todas"] + df["REGION"].unique().tolist())
    # Configuración del Filtrado
    if region == "Todas":
        pass
    else:
        df = df[df["REGION"]== region]
with c2:
    # Opciones del Filtro Empleado
    empleado = st.selectbox("**Empleado**", options= ["Todos"] + df["EMPLEADO"].unique().tolist())
    # Configuración del Filtrado
    if empleado == "Todos":
        pass
    else:
        df = df[df["EMPLEADO"]== empleado]

# Mpostrar el Dataframe con Todos los Datos en una Tabla
st.dataframe(df, use_container_width=True)




################# Gráficas de Unidades Vendidas, Ventas Totales y Porcentajes de Ventas ############

# Separación en Columnas
c1,c2,c3 = st.columns(3)

# Gráfico cuando se tiene información de varios empleados
if empleado == "Todos":
    # Gráficos de Plotly para cada Variable Especificada
    with c1:
        fig = px.bar(df, x="UNIDADES VENDIDAS", title="Unidades Vendidas", y="EMPLEADO", category_orders={"EMPLEADO": df.sort_values("UNIDADES VENDIDAS", ascending=False)["EMPLEADO"].tolist()})
        fig.update_layout(xaxis_title="Unidades Vendidas", yaxis_title="Empleado")
        st.plotly_chart(fig)

    with c2:
        fig = px.bar(df, x="VENTAS TOTALES", title="Ventas Totales", y="EMPLEADO", category_orders={"EMPLEADO": df.sort_values("VENTAS TOTALES", ascending=False)["EMPLEADO"].tolist()})
        fig.update_layout(xaxis_title="Ventas Totales", yaxis_title="Empleado")
        st.plotly_chart(fig)

    with c3:
        fig = px.bar(df, x="PORCENTAJE DE VENTAS", title="Porcentaje de Ventas", y="EMPLEADO", category_orders={"EMPLEADO": df.sort_values("PORCENTAJE DE VENTAS", ascending=False)["EMPLEADO"].tolist()})
        fig.update_layout(xaxis_title="Porcentaje de Ventas", yaxis_title="Empleado")
        st.plotly_chart(fig)

# Gráfico cuando se tiene información de un empleado
else:
    # Tarjeta de Datos para Mostrar Datos de Empleados Específicos
    with c1:
        st.metric("**Unidades Vendidas**", value=f"${df['UNIDADES VENDIDAS'].iloc[0]}")
    with c2:
        st.metric("**Ventas Totales**", value=f"${df['VENTAS TOTALES'].iloc[0]}")
    with c3:
        st.metric("**Porcentaje de Ventas**", value=f"{df['PORCENTAJE DE VENTAS'].iloc[0] * 100:.2f}%")


# Centrar Elemento con Columnas
c1,c2,c3 = st.columns([4,2,4])
with c2:
    # Botón para que caiga copos de nieve
    if st.button("Nieve", type= "primary"):
        st.snow()
    
