import io

import streamlit as st
import qrcode


st.set_page_config(page_title="OTP • sitio", page_icon="🔐", layout="centered")
st.title("OTP")


# ---------- UI ----------
col1, = st.columns(1)

with col1:
    if st.button("Configure OTP"):
        url = "my-url"
        qr = qrcode.QRCode(
            version=1, box_size=10, border=4,  # tweak sizing if you want
            error_correction=qrcode.constants.ERROR_CORRECT_M,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        st.image(buf.getvalue(), caption="Scan this QR in your authenticator app")

    with st.form("otp-configurar"):
        otp_code = str(int(st.number_input("OTP code", step=1)))
        confirm = st.form_submit_button("Confirmar")
        is_confirm = False

    if confirm:
        is_confirm = auth_service.validate_otp_client_configuration(
            st.session_state.token,
            otp_code,
        )

        if is_confirm:
            st.info("OTP configurado correctamente.")
        else:
            st.info("Intente nuevamente.")


# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>© 2025 Nuu | All rights reserved.</p>",
    unsafe_allow_html=True,
)
