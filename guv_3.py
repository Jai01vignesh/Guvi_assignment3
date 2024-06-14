import streamlit as st
import pandas as pd
import boto3
import json



#Clickstream data


# GENERAL SETTINGS
PAGE_TITLE = "Clickstream data"
PAGE_ICON = ":butterfly:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load the CSV dataset
@st.cache_data    # Caching for faster reloading
def load_data():
    data = pd.read_csv('test.csv',encoding='cp1252')
    return data

def display_selected_product_details(selected_product_details):
    st.header("Selected Product Details")
    st.write(f"Product ID: {selected_product_details['product_id']}")
    st.write(f"Product Name: {selected_product_details['product_name']}")
    st.write(f"Category: {selected_product_details['category']}")



def main():
    st.title('ClickStream Data')

    # Load the dataset
    data = load_data()

    st.title('Filter Category')
    # Filter products by category
    selected_category = st.selectbox('Select a category:', sorted(data['category'].unique()))
    filtered_data = data[data['category'] == selected_category]

    st.title("Product Recommendations")

    # Create an input field for the user to enter the product ID    
    selected_product_name = st.selectbox('Select a product:', sorted(filtered_data['product_name'].values))

    # Check if a product is selected
    if selected_product_name != 'Select a product':
        # Get the product ID for the selected product name
        selected_product_id = filtered_data[filtered_data['product_name'] == selected_product_name]['product_id'].values[0]
        selected_product_details = filtered_data[filtered_data['product_id'] == selected_product_id].iloc[0]
        # Display product details in the left column
        display_selected_product_details(selected_product_details)

        # Display product image and link in the right column

    # Button to trigger the recommendations
    if st.button("Buy"):
        data = {
         'itemid': selected_product_details['product_id'],
         'itemname':selected_product_details['product_name'],
         'key': '1'
        }
        response = kinesis.put_record(
        StreamName=stream_name,
        Data=json.dumps(data),
        PartitionKey='partition_key'  
    )
        print(response)




Path = "F:/New folder/GUVI/Bravo_04_accessKeys.csv"
with open(Path,"r") as pwd:
    for i in pwd:
        Accesskey,Pass_key = i.split(",")    

def create_con(Accesskey,srvc_name):
        cl = boto3.client(
        service_name=srvc_name,
        region_name='ap-south-1',
        aws_access_key_id = Accesskey, 
        aws_secret_access_key = "#"
        )
        return cl
# Initialize the Kinesis client
kinesis = create_con(Accesskey,'kinesis')  # Replace 'your-region' with your AWS region

# Specify the name of your Kinesis data stream
stream_name = 'click_strm'  # Replace 'your-stream-name' with your actual stream name

# Sample data

# Put a single record into the stream


if __name__ == '__main__':
    main()