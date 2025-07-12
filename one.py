import streamlit as st
st.title('Git Learning')
st.header('Our courses')
st.subheader('python')
st.subheader('sql')
st.subheader('c')
st.subheader('c++')
st.subheader('java')
col1,col2=st.columns(2)
with col1:
    st.image('D:\pr1\image.png')
with col2:
    st.write('''
The name "Fantasia flower" likely refers to the Hibiscus 'Fantasia', a cultivar known for its large, ruffled, rosy pink flowers with a dark red center. It is a compact, sturdy hibiscus that typically grows to 2-3 feet tall and produces 8-9 inch wide flowers. There is also a rose called 'Fantasia Mondiale Freelander' with salmon-orange blooms. Additionally, "Fantasia" is a term used in the context of floral designs, like those found at Floral Fantasia and in embroidery designs. 
Oops, something went wrong.
Floral Fantasia
We couldn't be happier. Thank you Murjhana and staff!" -Melinda Altshuler. "Did an amazing job on my wedding - better than I ever ...
Floral Fantasia
''')
a=st.button('baloon')
if a:
    st.balloons()