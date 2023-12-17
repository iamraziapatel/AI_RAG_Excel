import streamlit as st
from helper import get_qa_chain , create_vector_db


def main():
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #333333; /* Dark Gray */
                color: #ffffff;              
            }
            .stTextInput {
                font-family: 'Arial', sans-serif;
                font-size: 16px;
            }
            .stButton {                
                color: #ffffff; /* Dark Gray font color */
                font-family: 'Arial', sans-serif;
                font-size: 16px;
            }
            .footer {
                font-size: 14px;
                text-align: center;
                margin-top: 20px;
                color: #ffffff; /* White font color for the footer */
            }
            .right-corner {
                position: fixed;
                top: 0;
                right: 0;
                padding: 10px;
            }
            
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f'<h1 style="color:#ffffff;font-size:24px;">{"XYZ BANK - FinInfoCHATBot"}</h1><BR><BR>', unsafe_allow_html=True)
    #
    # # Button at the right corner
    # st.markdown(f'<h1 style="color:#ffffff;font-size:12px;">{"Admin-Access-only"}</h1><BR><BR>', unsafe_allow_html=True)
    # btn = st.button("update custom Knowledgebase")
    # if btn:
    #     create_vector_db()

    question = st.text_input("Question: ")

    if question:
        chain = get_qa_chain()
        response = chain(question)
        st.write("Assistant Response:")
        st.write(response["result"])

    # Footer and button at the bottom
    with st.container():
        st.markdown(

            """
            <div class="footer">
                <p>created by: Razia Patel</p>
            </div>
            """,
            unsafe_allow_html=True
        )


if __name__ == "__main__":
    main()
