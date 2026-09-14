import streamlit as st


def render_summary(agent, review_type):

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Review Type",
            review_type
        )

    with col2:

        st.metric(
            "Agent",
            agent
        )