import streamlit as st

# Page settings
st.set_page_config(
    page_title="School Events App",
    page_icon="📅",
    layout="wide",
)

HOME = "home"
PARENTS = "parents"
STUDENTS = "students"
COMMUNITY = "community"
STAFF = "staff"

if "page" not in st.session_state:
    st.session_state.page = HOME


def navigate_to(page_name: str) -> None:
    st.session_state.page = page_name

# Title/Home page
def show_home_page() -> None:

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.image("https://resources.finalsite.net/images/f_auto,q_auto/v1718995504/dallasisdorg/vrahv78m74vaqba1rvrp/ci-south-300.png", width=250)

    st.markdown(
        """
        <h1 style='text-align:center;'>
        School Events Portal
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <h4 style='text-align:center;'>
        View upcoming events and register for activities happening across our campus.
        </h4>
        """,
        unsafe_allow_html=True,
    )

    st.write(
        """
        This application allows parents, students, teachers,
        and staff members to view upcoming school events
        and register for events happening on campus.

        Select your role below to get started.
        """
    )
    st.write("")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Parents"):
            navigate_to(PARENTS)
    with col2:
        if st.button("Students"):
            navigate_to(STUDENTS)
    with col3:
        if st.button("Community"):
            navigate_to(COMMUNITY)
    with col4:
        if st.button("Staff"):
            navigate_to(STAFF)


def show_parents_page() -> None:
    st.header("Parents")
    st.write("Information and tools for parents go here.")
    if st.button("Back to home"):
        navigate_to(HOME)


def show_students_page() -> None:
    st.header("Students")
    st.write("Information and tools for students go here.")
    if st.button("Back to home"):
        navigate_to(HOME)


def show_community_page() -> None:
    st.header("Community")
    st.write("Information and tools for community members go here.")
    if st.button("Back to home"):
        navigate_to(HOME)

EVENTS = [
    {
        "id": "event_1",
        "title": "Spring Fundraiser",
        "date": "June 21, 2026",
        "location": "Gymnasium",
        "description": "A community fundraiser to support school programs. Includes food trucks, student performances, and a silent auction.",
    },
    {
        "id": "event_2",
        "title": "Staff Development Day",
        "date": "July 5, 2026",
        "location": "Library Conference Room",
        "description": "A full day for staff training, planning, and professional development sessions.",
    },
    {
        "id": "event_3",
        "title": "Summer Concert",
        "date": "July 18, 2026",
        "location": "Auditorium",
        "description": "A performance featuring student bands, choir, and guest speakers highlighting upcoming school initiatives.",
    },
]

if "events" not in st.session_state:
    st.session_state.events = [dict(event) for event in EVENTS]

if "selected_event_id" not in st.session_state:
    st.session_state.selected_event_id = None

if "registrations" not in st.session_state:
    st.session_state.registrations = {}


def show_staff_page() -> None:
    st.header("Staff")
    st.write("Browse upcoming staff-related events. Add new events and click an event to see more details.")

    with st.expander("Add a new event"):
        with st.form("add_event_form"):
            title = st.text_input("Event title")
            date = st.text_input("Date")
            location = st.text_input("Location")
            description = st.text_area("Description")
            add_submitted = st.form_submit_button("Add event")

            if add_submitted:
                if title and date and location and description:
                    new_event = {
                        "id": f"event_{len(st.session_state.events) + 1}",
                        "title": title,
                        "date": date,
                        "location": location,
                        "description": description,
                    }
                    st.session_state.events.append(new_event)
                    st.success("Event added successfully.")
                else:
                    st.warning("Please fill in all fields before adding the event.")

    selected_event_id = st.session_state.selected_event_id
    events = st.session_state.events

    if selected_event_id:
        event = next((item for item in events if item["id"] == selected_event_id), None)
        if event:
            st.subheader(event["title"])
            st.markdown(f"**Date:** {event['date']}")
            st.markdown(f"**Location:** {event['location']}")
            st.write(event["description"])
            st.write("")

            registration_list = st.session_state.registrations.get(event["id"], [])
            st.write("### Register for this event")
            with st.form(f"register_form_{event['id']}"):
                name = st.text_input("Your name")
                pathway = st.text_input("Pathway")
                register_submitted = st.form_submit_button("Register")
                if register_submitted:
                    if name and pathway:
                        registration_list.append({"name": name, "pathway": pathway})
                        st.session_state.registrations[event["id"]] = registration_list
                        st.success("Registration submitted.")
                    else:
                        st.warning("Please enter both your name and pathway.")

            if registration_list:
                st.write("### Registrations")
                for registration in registration_list:
                    st.write(f"- {registration['name']} ({registration['pathway']})")

            st.write("")
            if st.button("Back to staff events"):
                st.session_state.selected_event_id = None
        else:
            st.error("Selected event was not found.")
            st.session_state.selected_event_id = None
    else:
        for event in events:
            with st.container():
                st.subheader(event["title"])
                st.markdown(f"**Date:** {event['date']}  \\\n**Location:** {event['location']}")
                if st.button("View details", key=f"view_{event['id']}"):
                    st.session_state.selected_event_id = event["id"]
                st.write("---")

    st.write("")
    if st.button("Back to home"):
        st.session_state.selected_event_id = None
        navigate_to(HOME)

page = st.session_state.page
if page == HOME:
    show_home_page()
elif page == PARENTS:
    show_parents_page()
elif page == STUDENTS:
    show_students_page()
elif page == COMMUNITY:
    show_community_page()
elif page == STAFF:
    show_staff_page()
else:
    st.error("Unknown page")
