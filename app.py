import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 

st.set_page_config(page_title="My Dashboard Pro", page_icon="😶‍🌫️", layout="wide") 

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Ventas': [45000, 52000, 48000, 61000, 58000, 67000],
    'Clientes': [120, 145, 133, 167, 156, 189],
    'Región': ['Norte', 'Sur', 'Norte', 'Centro', 'Sur', 'Norte']
}

df = pd.DataFrame(data)

st.title("📊💡 Dashboard Ejecutivo Pro")
st.markdown("### Análisis en Tiempo Real de Performance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Ventas Totales", f"${df['Ventas'].sum():,}", "12%")
with col2:
     st.metric("Clientes Activos", df['Clientes'].sum(), "23")
with col3:
     st.metric("Promedio Mensual", f"${df['Ventas'].mean():.0f}", "8%")
with col4:
     st.metric("ROI", "245%", "15%")

fig = px.line(df, x= 'Mes', y='Ventas', 
              title= 'Evolución de Ventas Mensuales', 
              markers=True)
fig.update_layout(template='plotly_dark')
st.plotly_chart(fig, use_container_width=True)

fig2 = px.pie(df, values='Clientes', names='Región',
              title='Distribución de Clientes por Región')
fig2.update_layout(template='plotly_dark')
st.plotly_chart(fig2, use_container_width=True)

st.sidebar.header("Filtros de Control")
mes_seleccionado = st.sidebar.selectbox("Selecciona un mes:", df['Mes'])
region_filtro = st.sidebar.multiselect("Filtrar por región:", df['Región'].unique())

if region_filtro:
     datos_filtrados = df[df['Región'].isin(region_filtro)]
     st.dataframe(datos_filtrados, use_container_width=True)

