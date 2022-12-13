import streamlit as st
import pandas as pd
import numpy as np
from db import AppDatabase 




client = AppDatabase.init_connection()
print("=====DB CONNECTED=====")
print(client)


if 'dirtyItemsCount' not in st.session_state:
    st.session_state['dirtyItemsCount'] = 0

if 'item_batch_count' not in st.session_state:
    st.session_state['item_batch_count'] = 0


def main():
    # with st.sidebar:
    # dashboard_btn = st.button('Dashboard')
    # detect_btn = st.button('Detect')
    st.header('Dashboard')
    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Items Scanned", 8)
        with col2:
            st.metric("Defect Items", 3)
        with col3:
            st.metric("Clean Items", 5)

        with st.container():
            col4, col5, col6 = st.columns(3)
            with col5:
                st.metric("Overall Performance", str((5/8) * 100) + "%")

    # rnd_chart = np.random.randn(20, 3)
    chart_data = pd.DataFrame(
        [[1, 1, 0],
         [2, 2, 0],
         [3, 2, 1],
         [4, 2, 2],
         [5, 3, 2],
         [6, 4, 2],
         [7, 5, 2],
         [8, 5, 3]
         ],
        columns=['Items Scanned', 'Clean Items', 'Defect Items'])

    st.line_chart(chart_data)


if __name__ == '__main__':
    main()
