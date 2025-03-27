import streamlit as st

def main():
    st.header("st.button")
    if st.button("Click me!"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")


if __name__ == "__main__":
    main()
