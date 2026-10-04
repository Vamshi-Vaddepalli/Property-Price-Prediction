import re
import streamlit as st
import streamlit.components.v1 as components

GOATCOUNTER_URL = "https://vamshi-ppp-app.goatcounter.com/count"


def track(page_name):
    """Count one visit per session, on whichever page the visitor lands on first."""
    if st.session_state.get("gc_counted"):
        return
    st.session_state["gc_counted"] = True

    # keep only safe characters from the ?ref= tag (for example linkedin, naukri)
    ref = str(st.query_params.get("ref", ""))
    ref = re.sub(r"[^A-Za-z0-9_.-]", "", ref)[:50]

    components.html(
        f"""
        <script data-goatcounter="{GOATCOUNTER_URL}"
                data-goatcounter-settings='{{"path":"/{page_name}","title":"{page_name}","referrer":"{ref}"}}'
                async src="//gc.zgo.at/count.js"></script>
        """,
        height=0,
    )