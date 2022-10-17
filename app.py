import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

from config import config

st.set_page_config(layout="wide")
st.title(config.PROJECT_NAME)
st.text('Create a PostgresDB table from one or more CSV files.')
st.text('Optionally analyze the data prior to exporting.')

tab_upload, tab_analyze, tab_export= st.tabs(['Upload', 'Analyze', 'Export'])

# UPLOAD DATA
with tab_upload:
    st.header('Upload')
    uploaded_files = st.file_uploader(
        "Select CSV Files",
        type=None,
        accept_multiple_files=True,
        key=None, help=None, on_change=None,
        args=None, kwargs=None, disabled=False,
        label_visibility="visible")

# EXPORT DATA
with tab_export:
    st.header('Export')
    st.subheader('Database')
    st.selectbox(
        'Schema',
        config.EXPORT_METADATA_FIELD_1_VALUES,
        index=0,
        #  format_func=special_internal_function,
        key=None, help=None, on_change=None, args=None,
        kwargs=None, disabled=False, label_visibility="visible")
    st.text_input(
        "Table", value="", max_chars=None, key=None,
        type="default", help=None, autocomplete=None,
        on_change=None, args=None, kwargs=None,
        placeholder=None, disabled=False,
        label_visibility="visible")

    # EXPORT_METADATA_FIELDS
    st.subheader(config.EXPORT_METADATA_CATEGOROY)
    st.selectbox(
        config.EXPORT_METADATA_FIELD_1_NAME,
        config.EXPORT_METADATA_FIELD_1_VALUES,
        index=0,
        #  format_func=special_internal_function,
        key=None, help=None, on_change=None, args=None,
        kwargs=None, disabled=False, label_visibility="visible")

    st.selectbox(
        config.EXPORT_METADATA_FIELD_2_NAME,
        config.EXPORT_METADATA_FIELD_2_VALUES,
        index=0,
        #  format_func=special_internal_function,
        key=None, help=None, on_change=None, args=None,
        kwargs=None, disabled=False, label_visibility="visible")

    st.selectbox(
        config.EXPORT_METADATA_FIELD_3_NAME,
        config.EXPORT_METADATA_FIELD_3_VALUES,
        index=0,
        #  format_func=special_internal_function,
        key=None, help=None, on_change=None, args=None,
        kwargs=None, disabled=False, label_visibility="visible")

    st.button(
        "Export to Database", key=None, help=None,
        on_click=None, args=None, kwargs=None, disabled=False)

# ANALYZE DATA
with tab_analyze:
    st.header('Analyze')
    for uploaded_file in uploaded_files:
        # uploaded_file.read()
        df = pd.read_csv(uploaded_file)
        pr = df.profile_report()
        st_profile_report(pr)