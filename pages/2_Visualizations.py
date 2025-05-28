import streamlit as st
import plotly.express as px

st.markdown("""
### 🚀 Let's make one chart interactive!

This is an interactive version of **Top 5 Most Expensive Books** chart using Plotly.  
Try hovering over the bars to see detailed info!
""")

with st.expander("💖 Top 5 most expensive books (Interactive)"):
    top_expensive = df.sort_values(by="Price", ascending=False).head(5)
    st.subheader("💰 Top 5 Most Expensive Books")

    def create_expensive_chart():
        fig = px.bar(
            top_expensive,
            x="Price",
            y="Title",
            orientation='h',
            color="Price",
            color_continuous_scale='RdPu',
            title="Top 5 Most Expensive Books"
        )
        fig.update_layout(yaxis={'categoryorder':'total ascending'})
        return fig

    if "expensive_fig" not in st.session_state:
        st.session_state.expensive_fig = create_expensive_chart()

    st.plotly_chart(st.session_state.expensive_fig)

    if st.button("🔄 Reset View"):
        st.session_state.expensive_fig = create_expensive_chart()
        st.experimental_rerun()

st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
