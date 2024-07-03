from Sentiment_Anaylsis.pipeline.end_result import Prediction


import streamlit as st


import streamlit as st

def process_input(input_type, input_value):
    if input_type == "Text":
        st.write(f"Processing single text: {input_value}")
        # Call your function for single text
        obj=Prediction(input_value)
        label=obj.predict()
        st.write("Your rating fro this product is my brother",label)
        # result = your_function(input_value)
    elif input_type == "List":
        st.write(f"Processing list of texts: {input_value}")
        # Call your function for list of texts
        res=[]
        for i in input_value:
            obj=Prediction(i)
            label=obj.predict()
            res.append(label)
        st.write("your reviews are here list of reviews:",res)


        # result = your_function(input_value)
    # Display the result (uncomment once you have your function)
    # st.write(result)

# Streamlit UI
st.title("Text or List Input")

input_type = st.radio("Select input type", ("Text", "List"))

if input_type == "Text":
    text_input = st.text_area("Enter text")
    if st.button("Submit"):
        process_input(input_type, text_input)

elif input_type == "List":
    list_input = st.text_area("Enter list of texts (comma separated)")
    if st.button("Submit"):
        # Convert the comma-separated string into a list
        list_input = [item.strip() for item in list_input.split(",") if item.strip()]
        process_input(input_type, list_input)


    
         
    
