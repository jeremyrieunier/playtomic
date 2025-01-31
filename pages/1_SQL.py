import streamlit as st
import pandas as pd
import duckdb

old_users_data = {
    "user_id": ["123456789", "234567890", "345678901", "456789012", "567890123"],
    "created_at": ["2022-05-17", "2022-08-06", "2022-08-06", "2023-03-25", "2023-08-11"],
    "user_country": ["Spain", "Spain", "Spain", "Spain", "Spain",],
    "user_level": [2.5, 3.0, 2.5, 2.0, 3.5]
}

users_data = {
    "user_id":       ["123456789", "234567890", "345678901", "736345353", "521236334", "678901234", "264573453", "789012345", "890123456", "901234567", "456789012", "567890123", "012345678", "043144566"],
    "created_at":    ["2022-05-17", "2022-08-06", "2022-08-06", "2022-09-15", "2022-10-20", "2022-08-06", "2022-12-05", "2022-11-30", "2023-02-14", "2023-02-14", "2023-03-25", "2023-08-11", "2023-08-11", "2023-08-12"],
    "user_country":  ["Spain", "Spain", "Spain", "Spain", "Spain", "France", "Spain", "France", "France", "France", "Spain", "Spain", "France", "Italy"],
    "user_level":    [2.5, 3.0, 2.5, 2.0, 3.0, 2.0, 2.5, 3.0, 2.5, 3.5, 2.0, 3.5, 2.5, 2.0]
}

old_online_court_bookings_data = {
    "booking_id": ["15274734", "15274734", "15274734", "15274734", "55234774", "55234774", "55234774", "55234774"],
    "owner_id": ["123456789"] * 8, 
    "user_id": ["123456789", "234567890", None, None, "123456789", "234567890", "745378931", "656383722"],
    "created_at": ["2024-01-17", "2024-01-17", None, None, "2024-05-06", "2024-05-07", "2024-05-07", "2024-05-08"],
    "played_at": ["2024-01-23", "2024-01-23", "2024-01-23", "2024-01-23", "2024-05-14", "2024-05-14", "2024-05-14", "2024-05-14"],
    "club_id": ["5555555", "5555555", "5555555", "5555555", "6666666", "6666666", "6666666", "6666666"],
    "club_country": ["Spain"] * 8,
    "payment_amount": [25, 0, 0, 0, 7, 7, 7, 7],
    "b2c_commission_amount": [1, 0, 0, 0, 0.5, 0.5, 0.5, 0.5]
}

online_court_bookings_data = {
    "booking_id":    ["66234521", "66234521", "66234521", "66234521", "15274734", "15274734", "15274734", "15274734", "77234890", "77234890", "77234890", "77234890", "55234774", "55234774", "55234774", "55234774"],
    "owner_id":      ["678901234", "678901234", "678901234", "678901234", "123456789", "123456789", "123456789", "123456789", "789012345", "789012345", "789012345", "789012345", "123456789", "123456789", "123456789", "123456789"],
    "user_id":       ["678901234", "789012345", None, None, "123456789", "234567890", None, None, "789012345", "890123456", "901234567", "012345678", "123456789", "234567890", "345678901", "456789012"],
    "created_at":    ["2024-01-20T09:03:52", "2024-01-20T10:03:52", None, None, "2024-01-17T09:03:52", "2024-01-17T10:03:52", None, None, "2024-05-10T09:03:52", "2024-05-10T09:33:52", "2024-05-11T10:03:52", "2024-05-11T19:03:52", "2024-05-06T07:03:52", "2024-05-07T09:03:52", "2024-05-07T10:03:52", "2024-05-08T11:03:52"],
    "played_at":     ["2024-01-25T09:03:52", "2024-01-25T09:03:52", "2024-01-25T09:03:52", "2024-01-25T09:03:52", "2024-01-23T09:03:52", "2024-01-23T09:03:52", "2024-01-23T09:03:52", "2024-01-23T09:03:52", "2024-05-18T09:03:52", "2024-05-18T09:03:52", "2024-05-18T09:03:52", "2024-05-18T09:03:52", "2024-05-14T09:03:52", "2024-05-14T09:03:52", "2024-05-14T09:03:52", "2024-05-14T09:03:52"],
    "club_id":       ["7777777", "7777777", "7777777", "7777777", "5555555", "5555555", "5555555", "5555555", "8888888", "8888888", "8888888", "8888888", "6666666", "6666666", "6666666", "6666666"],
    "club_country":  ["France", "France", "France", "France", "Spain", "Spain", "Spain", "Spain", "France", "France", "France", "France", "Spain", "Spain", "Spain", "Spain"],
    "payment_amount": [30, 0, 0, 0, 25, 0, 0, 0, 8, 8, 8, 8, 7, 7, 7, 7],
    "b2c_commission_amount": [1.2, 0, 0, 0, 1, 0, 0, 0, 0.6, 0.6, 0.6, 0.6, 0.5, 0.5, 0.5, 0.5]
}

old_open_matches_data = {
   "match_id": ["15274734", "15274734", "15274734", "15274734", "55234774", "55234774", "55234774", "55234774"],
   "owner_id": [None] * 8,
   "user_id": ["345678901", None, None, "234567890", "456789012", "521236334", "736345353", "264573453"],
   "created_at": ["2023-11-20", "2023-11-20", "2023-11-20", "2023-11-20", "2024-03-23", "2024-03-23", "2024-03-23", "2024-03-23"],
   "played_at": ["2023-11-23", "2023-11-23", "2023-11-23", "2023-11-23", "2024-04-01", "2024-04-01", "2024-04-01", "2024-04-01"],
   "club_id": ["5555555", "5555555", "5555555", "5555555", "6666666", "6666666", "6666666", "6666666"],
   "club_country": ["Spain"] * 8,
   "payment_amount": [7, 7, 7, 7, 8, 8, 8, 8],
   "b2c_commission_amount": [0.5, 0.5, 0.5, 0.5, 0.65, 0.65, 0.65, 0.65]
}

open_matches_data = {
  "match_id": ["15274734", "15274734", "15274734", "15274734", "77234521", "77234521", "77234521", "77234521", "55234774", "55234774", "55234774", "55234774", "88234666", "88234666", "88234666", "88234666"],
  "owner_id": [None] * 16,
  "user_id": ["345678901", None, None, None, "678901234", "789012345", None, None, "456789012", "521236334", "736345353", "264573453", "901234567", "012345678", "678901234", "789012345"],
  "created_at": ["2023-11-20T06:03:52", "2023-11-20T07:03:52", "2023-11-20T08:03:52", "2023-11-20T09:03:52", "2023-12-15T10:03:52", "2023-12-15T11:03:52", "2023-12-15T12:03:52", "2023-12-15T13:03:52", "2024-03-23T14:03:52", "2024-03-23T15:03:52", "2024-03-23T16:03:52", "2024-03-23T17:03:52", "2024-03-25T18:03:52", "2024-03-25T19:03:52", "2024-03-25T20:03:52", "2024-03-25T21:03:52"],
  "played_at": ["2023-11-23T09:03:52", "2023-11-23T09:03:52", "2023-11-23T09:03:52", "2023-11-23T09:03:52", "2023-12-20T09:03:52", "2023-12-20T09:03:52", "2023-12-20T09:03:52", "2023-12-20T09:03:52", "2024-04-01T09:03:52", "2024-04-01T09:03:52", "2024-04-01T09:03:52", "2024-04-01T09:03:52", "2024-04-02T09:03:52", "2024-04-02T09:03:52", "2024-04-02T09:03:52", "2024-04-02T09:03:52"],
  "club_id": ["5555555", "5555555", "5555555", "5555555", "7777777", "7777777", "7777777", "7777777", "6666666", "6666666", "6666666", "6666666", "8888888", "8888888", "8888888", "8888888"],
  "club_country": ["Spain", "Spain", "Spain", "Spain", "France", "France", "France", "France", "Spain", "Spain", "Spain", "Spain", "France", "France", "France", "France"],
  "payment_amount": [7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8],
  "b2c_commission_amount": [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.65, 0.65, 0.65, 0.65, 0.65, 0.65, 0.65, 0.65]
}

df_users = pd.DataFrame(users_data)
df_ocb = pd.DataFrame(online_court_bookings_data)
df_om = pd.DataFrame(open_matches_data)

# st.dataframe(df_users)
# st.dataframe(df_ocb)
# st.dataframe(df_om)


con = duckdb.connect()
con.register("users", df_users)
con.register("online_court_bookings", df_ocb)
con.register("open_matches", df_om)

st.set_page_config(
    page_title="SQL exercises",
    page_icon="📊",
)

st.title("📊 SQL exercises")

st.write("I used the following tables to answer the questions:")
st.markdown("### users_data")
st.dataframe(users_data)
st.markdown("### online_court_bookings_data")
st.dataframe(online_court_bookings_data)
st.markdown("### open_matches_data")
st.dataframe(open_matches_data)

st.subheader("Number of users and the average user level breakdown by user creation date")

query = """
select
    created_at as user_creation_date,
    count(user_id) as user_count,
    avg(user_level) as avg_user_level
from users
group by user_creation_date
order by user_creation_date
"""

st.code(query, language="sql")

results = con.execute(query).df()
st.dataframe(con.execute(query).df())


st.subheader("Number of users who have played at least 1 open match and 1 online court booking match")

query_sql = """

-- CTE to get users who've booked courts online
with court_booking_users as (
    select distinct user_id
    from online_court_bookings
    where user_id is not null
),
-- GTE to get users who've played open matches
open_match_users as (
    select distinct user_id
    from open_matches
    where user_id is not null
)

-- Count users who appear in both groups using an inner join
select
    count(c.user_id) as users_played_both
from court_booking_users c
inner join open_match_users o
on c.user_id = o.user_id

"""
st.code(query_sql, language="sql")
st.dataframe(con.execute(query_sql).df())

st.subheader("For online court bookings: The number of bookings, the total payment amount, the total b2c commission, and the margin/take rate —breakdown by user country")

query_book = """

-- CTE to aggregate payment details per booking
with bookings as (
    select
        booking_id,
        owner_id,
        sum(payment_amount) as total_payment,
        sum(b2c_commission_amount) as total_commission
    from online_court_bookings
    group by
        booking_id,
        owner_id    
)

-- Get key metrics by user country using a left join
select
    u.user_country,
    count(booking_id) as booking_count,
    sum(total_payment) as total_payment,
    sum(total_commission) as total_commission,
    round(sum(total_commission) / nullif(sum(total_payment), 0) * 100, 2) as margin_take_rate
from users u
left join bookings b
    on u.user_id = b.owner_id
group by u.user_country
order by booking_count desc

"""

st.code(query_book, language="sql")
st.dataframe(con.execute(query_book).df())

st.subheader("Create a rank based on the created_at date per match_id for open matches")

query_rank = """
select
    match_id,
    user_id,
    created_at,
    dense_rank() over( -- dense_rank() to avoid gaps 
        partition by match_id
        order by created_at
        ) as rank
from open_matches
"""
st.code(query_rank, language="sql")
st.dataframe(con.execute(query_rank).df())
st.write("All dates come without timestamp")


st.subheader("Funnel analysis to see, per user creation year, the conversion from user creation to an open match.")

query_funnel = """
-- CTE to get the user creation year for each user
with user_creation as (
    select
        user_id,
        date_part('year', cast(created_at as date)) as creation_year
    from users
),
-- CTE to get the users who participated in an open match
user_open_match as (
    select distinct user_id
    from open_matches
    where user_id is not null
)

select
    u.creation_year as creation_year,
    count(u.user_id) as count_user,
    count(o.user_id) as converted_user,
    round(count(o.user_id) / count(u.user_id) * 100, 2) as conversion_rate
from user_creation u
left join user_open_match o
    on u.user_id = o.user_id
group by u.creation_year
order by u.creation_year
"""

st.code(query_funnel, language="sql")
st.dataframe(con.execute(query_funnel).df())