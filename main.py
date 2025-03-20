import streamlit as st

col1, col2 = st.columns(2)

with col1:
  st.image("Images/profile.png")

with col2:
  st.title("Sima Dhimal")
  content = """efjslkfsdlkfjsdlkfjslk skdjfsldkfjslkdj sdlfjksdlkfjsl dsfjsdlfjs 
               djfslkfjslkdfjslkf sdkfjslkfjsdlkflkjdflk sdfjslfjsl dfjskldfj
               djfksdlfjsd sdkjflskd jfskdj fsl sdkfj slkfdj sdkfj sk sdjf lk 
               sdkj klf sdkljf klds skjfdssdkj fdsklj fkdlsfjsdkj dksj dkj fskdjf 
               kdj saklfjkldkfj dsklfj skljskl dksjf lksdjf dskjf lksj lsdkjfl ksdfj
               """

  st.write(content)