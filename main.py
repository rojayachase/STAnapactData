import streamlit as st
import json
import pandas as pd
table=pd.DataFrame({})

st.title("Hi, Impact Data | Breakdown ")
st.subheader("this is a subheader")


data = {
  "sessions": {
    "NgCtDhQGMYN530oxpKHoWNiVjvT2": {
      "1691720687567-1691720689880": {
        "device_id": "51D648D2-CAFB-C20E-DC3C-272591745A5E",
        "id": "1691720687567-1691720689880",
        "punches": {
          "1693953829742": 9.71484375,
          "1693954191471": 4.05859375,
          "1693954193083": 4.19921875,
          "1693954196382": 10.5546875,
          "1693954198300": 7.53125,
          "1693954200132": 4.44921875,
          "1693954200460": 4.46484375,
          "1693954200941": 8.82421875,
          "1693954383285": 13.73828125,
          "1693954425106": 5.56640625,
          "1693954455827": 5.23828125,
          "1693954457057": 6.0078125,
          "1693954459277": 7.52734375,
          "1693954477845": 4.91796875,
          "1693954482555": 5,
          "1693954483216": 8.265625,
          "1693954483667": 11.49609375,
          "1693954484148": 5.5625,
          "1693954497977": 5.3984375,
          "1693954501758": 5.265625,
          "1693954501968": 6.64453125,
          "1693954502328": 10.94140625,
        },
        "username": "Tom Jones"
      }
    }
  }
}

# prompt: count number of punches

punches = data["sessions"]["NgCtDhQGMYN530oxpKHoWNiVjvT2"]["1691720687567-1691720689880"]["punches"]
num_punches = len(punches)
st.write('the number of punches are' , num_punches)

# prompt: sum of punch

total_punch = 0
for punch in data["sessions"]["NgCtDhQGMYN530oxpKHoWNiVjvT2"]["1691720687567-1691720689880"]["punches"].values():
  total_punch += punch
st.write(total_punch)


# prompt: average of punch

# punches = list(data["sessions"]["NgCtDhQGMYN530oxpKHoWNiVjvT2"]["1691720687567-1691720689880"]["punches"].values())
# average_punch = sum(punches) / len(punches)
# st.write('average punch:', average_punch)


# for timestamp, punch in data["sessions"]["NgCtDhQGMYN530oxpKHoWNiVjvT2"]["1691720687567-1691720689880"]["punches"].items():
#   st.write('Strikes:', timestamp)
#   st.write('Punch:', punch)


# prompt: convert items into integer

# for timestamp, punch in data["sessions"]["NgCtDhQGMYN530oxpKHoWNiVjvT2"]["1691720687567-1691720689880"]["punches"].items():
  # print('Strikes:', timestamp)
#   st.write('Punch:', int(punch))

# Extract the punches from the data
punches = data["sessions"]["NgCtDhQGMYN530oxpKHoWNiVjvT2"]["1691720687567-1691720689880"]["punches"]

# Create a list to store the punches
punch_force = []

# Iterate over the punches and append them to the list
for timestamp, punch in punches.items():
  punch_force.append(punch)




# Print the list of punches
# st.write(punch_force)



# prompt: convert punch_list into int

# Convert the list of punches to integers
punch_int = [round(punch, 1) for punch in punch_force]

# Print the list of integer punches
st.write(punch_int)


total_punch_force = round(sum(punch_force))
st.write('sum of punches' , total_punch_force)


# prompt: average of punch

punches = list(data["sessions"]["NgCtDhQGMYN530oxpKHoWNiVjvT2"]["1691720687567-1691720689880"]["punches"].values())
average_punch = sum(punches) / len(punches)
st.write('average punch:', average_punch)



col1, col2, col3 = st.columns(3)
col1.metric("Amount Of Punches", num_punches, "1.2 °F")
col2.metric("Total Amount of Strike Force", total_punch_force, "-8%")
col3.metric("Humidity", "86%", "4%")


















