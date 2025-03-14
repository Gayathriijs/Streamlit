import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import random
import json
import os
from datetime import datetime, timedelta
import calendar

# Set page configuration
st.set_page_config(
    page_title="Lifestyle Hub",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
def load_css():
    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

if 'events' not in st.session_state:
    st.session_state.events = []

if 'daily_todos' not in st.session_state:
    st.session_state.daily_todos = []

if 'long_term_todos' not in st.session_state:
    st.session_state.long_term_todos = []

if 'habits' not in st.session_state:
    st.session_state.habits = []

if 'expenses' not in st.session_state:
    st.session_state.expenses = []

if 'last_day' not in st.session_state:
    st.session_state.last_day = datetime.now().day

if 'current_affirmation' not in st.session_state:
    st.session_state.current_affirmation = ""

# Check if a new day has started to reset daily todos
current_day = datetime.now().day
if current_day != st.session_state.last_day:
    st.session_state.daily_todos = []
    st.session_state.last_day = current_day
    st.session_state.current_affirmation = ""

# Function to save data to JSON files
def save_data():
    data = {
        'events': st.session_state.events,
        'long_term_todos': st.session_state.long_term_todos,
        'habits': st.session_state.habits,
        'expenses': st.session_state.expenses
    }
    
    with open('user_data.json', 'w') as f:
        json.dump(data, f)

# Function to load data from JSON files
def load_data():
    if os.path.exists('user_data.json'):
        with open('user_data.json', 'r') as f:
            data = json.load(f)
            
            st.session_state.events = data.get('events', [])
            st.session_state.long_term_todos = data.get('long_term_todos', [])
            st.session_state.habits = data.get('habits', [])
            st.session_state.expenses = data.get('expenses', [])

# Load saved data when the app starts
load_data()

# Toggle dark mode
def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# List of affirmations
affirmations = [
    "I am capable of achieving greatness today.",
    "Today is full of possibilities and I am ready for them.",
    "I trust my intuition and make wise decisions.",
    "I am in charge of how I feel and today I choose happiness.",
    "Every challenge I face is an opportunity to grow stronger.",
    "I am worthy of success and happiness.",
    "My potential is limitless, and my opportunities are abundant.",
    "I radiate positive energy and attract good things.",
    "I have the power to create change in my life.",
    "Today I choose to be confident and brave."
]

# Function to get a random affirmation
def get_random_affirmation():
    st.session_state.current_affirmation = random.choice(affirmations)

# Get an affirmation if one isn't already set for today
if not st.session_state.current_affirmation:
    get_random_affirmation()

# Sidebar with navigation
with st.sidebar:
    st.title("✨ Lifestyle Hub")
    theme_col1, theme_col2 = st.columns([3, 1])
    with theme_col1:
        st.write("Theme Mode:")
    with theme_col2:
        if st.button("🌓" if st.session_state.dark_mode else "☀️"):
            toggle_theme()
    
    st.markdown("---")
    nav_option = st.radio(
        "Navigation",
        ["Home", "Calendar", "Affirmations", "Daily Planner", "Habit Tracker", "Finance Tracker"]
    )
    
    st.markdown("---")
    st.caption("© 2025 Lifestyle Hub")

# Apply theme based on dark mode status
if st.session_state.dark_mode:
    st.markdown("""
    <style>
        .main {
            background-color: #121212;
            color: #f0f0f0;
        }
        .css-1d391kg {
            background-color: #1e1e1e;
        }
        .st-bw {
            background-color: #1e1e1e;
        }
        .css-1lcbmhc {
            color: #f0f0f0;
        }
    </style>
    """, unsafe_allow_html=True)

# Load custom CSS
load_css()

# Home Dashboard
if nav_option == "Home":
    st.header("Welcome to Your Lifestyle Hub")
    
    # Get current date and time
    now = datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")
    
    # Greeting based on time of day
    hour = now.hour
    if 5 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    # Display greeting and today's date
    st.markdown(f"<h2 class='greeting'>{greeting}!</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='date'>{date_str}</p>", unsafe_allow_html=True)
    
    # Display current affirmation
    st.markdown("""
    <div class='affirmation-card'>
        <h3>Today's Affirmation</h3>
        <p class='affirmation-text'>""" + st.session_state.current_affirmation + """</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick access to sections
    st.markdown("<h3 class='section-header'>Quick Access</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='quick-card'>
            <h4>Today's Tasks</h4>
            <p>You have """ + str(len([t for t in st.session_state.daily_todos if not t['completed']])) + """ tasks to complete today</p>
            <p class='card-link'>Go to Daily Planner →</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='quick-card'>
            <h4>Habit Progress</h4>
            <p>Track your daily habits</p>
            <p class='card-link'>Go to Habit Tracker →</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Calculate next event
        upcoming_events = [e for e in st.session_state.events if datetime.strptime(e['date'], '%Y-%m-%d') >= now.replace(hour=0, minute=0, second=0, microsecond=0)]
        upcoming_events.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
        
        event_info = "No upcoming events" if not upcoming_events else f"Next: {upcoming_events[0]['title']} on {upcoming_events[0]['date']}"
        
        st.markdown(f"""
        <div class='quick-card'>
            <h4>Calendar</h4>
            <p>{event_info}</p>
            <p class='card-link'>Go to Calendar →</p>
        </div>
        """, unsafe_allow_html=True)

# Calendar Integration
elif nav_option == "Calendar":
    st.header("Calendar")
    
    # Calendar UI
    col1, col2 = st.columns([2, 3])
    
    with col1:
        selected_date = st.date_input("Select Date", datetime.now())
        
        event_title = st.text_input("Event Title")
        event_description = st.text_area("Event Description", height=100)
        
        if st.button("Add Event"):
            if event_title:
                new_event = {
                    'date': selected_date.strftime('%Y-%m-%d'),
                    'title': event_title,
                    'description': event_description
                }
                st.session_state.events.append(new_event)
                save_data()
                st.success("Event added successfully!")
    
    with col2:
        # Monthly calendar view
        selected_month = selected_date.month
        selected_year = selected_date.year
        
        # Get month calendar
        cal = calendar.monthcalendar(selected_year, selected_month)
        month_name = calendar.month_name[selected_month]
        
        # Create a visually appealing calendar
        st.markdown(f"<h3 class='calendar-header'>{month_name} {selected_year}</h3>", unsafe_allow_html=True)
        
        # Display calendar headers
        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        cal_cols = st.columns(7)
        for i, day in enumerate(weekdays):
            cal_cols[i].markdown(f"<p class='calendar-weekday'>{day}</p>", unsafe_allow_html=True)
        
        # Display calendar days
        for week in cal:
            cal_cols = st.columns(7)
            for i, day in enumerate(week):
                if day == 0:
                    cal_cols[i].markdown("<p class='calendar-day empty'></p>", unsafe_allow_html=True)
                else:
                    date_str = f"{selected_year}-{selected_month:02d}-{day:02d}"
                    
                    # Check if there are events on this day
                    day_events = [e for e in st.session_state.events if e['date'] == date_str]
                    
                    # Check if this is the selected date
                    is_selected = day == selected_date.day and selected_month == selected_date.month and selected_year == selected_date.year
                    
                    if day_events:
                        cal_cols[i].markdown(f"<p class='calendar-day with-event {'selected' if is_selected else ''}'>{day}</p>", unsafe_allow_html=True)
                        for event in day_events:
                            cal_cols[i].markdown(f"<p class='calendar-event'>{event['title']}</p>", unsafe_allow_html=True)
                    else:
                        cal_cols[i].markdown(f"<p class='calendar-day {'selected' if is_selected else ''}'>{day}</p>", unsafe_allow_html=True)
    
    # Display events for selected date
    st.markdown("<h3 class='section-header'>Events for Selected Date</h3>", unsafe_allow_html=True)
    
    selected_date_str = selected_date.strftime('%Y-%m-%d')
    selected_events = [e for e in st.session_state.events if e['date'] == selected_date_str]
    
    if not selected_events:
        st.info("No events for this date.")
    else:
        for i, event in enumerate(selected_events):
            col1, col2 = st.columns([5, 1])
            with col1:
                st.markdown(f"""
                <div class='event-card'>
                    <h4>{event['title']}</h4>
                    <p>{event['description']}</p>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                if st.button("Delete", key=f"del_event_{i}"):
                    st.session_state.events.remove(event)
                    save_data()
                    st.experimental_rerun()

# Affirmations
elif nav_option == "Affirmations":
    st.header("Daily Affirmations")
    
    # Display current affirmation
    st.markdown("""
    <div class='affirmation-display'>
        <h3>Today's Affirmation</h3>
        <p class='affirmation-quote'>""" + st.session_state.current_affirmation + """</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Button to get a new affirmation
    if st.button("Generate New Affirmation"):
        get_random_affirmation()
        st.experimental_rerun()
    
    # User can add custom affirmations
    st.markdown("<h3 class='section-header'>Create Your Own Affirmation</h3>", unsafe_allow_html=True)
    
    custom_affirmation = st.text_area("Write your custom affirmation", height=100)
    if st.button("Save Affirmation"):
        if custom_affirmation:
            affirmations.append(custom_affirmation)
            st.session_state.current_affirmation = custom_affirmation
            st.success("Your affirmation has been saved!")
            st.experimental_rerun()

# Daily Planner & To-Do Lists
elif nav_option == "Daily Planner":
    st.header("Daily Planner & To-Do Lists")
    
    tab1, tab2 = st.tabs(["Daily To-Do", "Long-Term To-Do"])
    
    # Daily To-Do List (resets each day)
    with tab1:
        st.subheader("Today's To-Do List")
        
        # Add new task
        new_task = st.text_input("Add a new task for today")
        if st.button("Add Task", key="add_daily"):
            if new_task:
                st.session_state.daily_todos.append({
                    'task': new_task,
                    'completed': False
                })
                st.experimental_rerun()
        
        # Display tasks
        if not st.session_state.daily_todos:
            st.info("No tasks for today. Add some tasks to get started!")
        else:
            for i, todo in enumerate(st.session_state.daily_todos):
                col1, col2, col3 = st.columns([0.1, 4, 0.5])
                with col1:
                    checked = st.checkbox("", todo['completed'], key=f"daily_{i}")
                    if checked != todo['completed']:
                        todo['completed'] = checked
                        st.experimental_rerun()
                with col2:
                    if todo['completed']:
                        st.markdown(f"<p style='text-decoration: line-through;'>{todo['task']}</p>", unsafe_allow_html=True)
                    else:
                        st.write(todo['task'])
                with col3:
                    if st.button("🗑️", key=f"del_daily_{i}"):
                        st.session_state.daily_todos.pop(i)
                        st.experimental_rerun()
            
            # Progress bar
            completed = len([t for t in st.session_state.daily_todos if t['completed']])
            total = len(st.session_state.daily_todos)
            progress = completed / total if total > 0 else 0
            
            st.progress(progress)
            st.write(f"Completed: {completed}/{total} tasks ({int(progress * 100)}%)")
    
    # Long-Term To-Do List (persists across sessions)
    with tab2:
        st.subheader("Long-Term To-Do List")
        
        # Add new task
        new_task = st.text_input("Add a new long-term task")
        priority = st.select_slider("Priority", options=["Low", "Medium", "High"])
        deadline = st.date_input("Deadline (optional)", value=None, key="lt_deadline")
        
        if st.button("Add Task", key="add_longterm"):
            if new_task:
                st.session_state.long_term_todos.append({
                    'task': new_task,
                    'priority': priority,
                    'deadline': deadline.strftime('%Y-%m-%d') if deadline else None,
                    'completed': False
                })
                save_data()
                st.experimental_rerun()
        
        # Display tasks
        if not st.session_state.long_term_todos:
            st.info("No long-term tasks. Add some tasks to get started!")
        else:
            # Sort by priority and deadline
            sorted_todos = sorted(st.session_state.long_term_todos, 
                                 key=lambda x: (x['completed'], 
                                              0 if x['priority'] == 'High' else 1 if x['priority'] == 'Medium' else 2,
                                              x['deadline'] if x['deadline'] else '9999-12-31'))
            
            for i, todo in enumerate(sorted_todos):
                col1, col2, col3, col4, col5 = st.columns([0.1, 2.5, 1, 1, 0.5])
                with col1:
                    original_index = st.session_state.long_term_todos.index(todo)
                    checked = st.checkbox("", todo['completed'], key=f"lt_{original_index}")
                    if checked != todo['completed']:
                        todo['completed'] = checked
                        save_data()
                        st.experimental_rerun()
                with col2:
                    if todo['completed']:
                        st.markdown(f"<p style='text-decoration: line-through;'>{todo['task']}</p>", unsafe_allow_html=True)
                    else:
                        st.write(todo['task'])
                with col3:
                    priority_color = "red" if todo['priority'] == "High" else "orange" if todo['priority'] == "Medium" else "blue"
                    st.markdown(f"<span style='color:{priority_color};'>{todo['priority']}</span>", unsafe_allow_html=True)
                with col4:
                    if todo['deadline']:
                        st.write(todo['deadline'])
                    else:
                        st.write("No deadline")
                with col5:
                    if st.button("🗑️", key=f"del_lt_{original_index}"):
                        st.session_state.long_term_todos.pop(original_index)
                        save_data()
                        st.experimental_rerun()
            
            # Progress stats
            completed = len([t for t in st.session_state.long_term_todos if t['completed']])
            total = len(st.session_state.long_term_todos)
            progress = completed / total if total > 0 else 0
            
            st.progress(progress)
            st.write(f"Completed: {completed}/{total} tasks ({int(progress * 100)}%)")

# Habit Tracker
elif nav_option == "Habit Tracker":
    st.header("Habit Tracker")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Define New Habit")
        habit_name = st.text_input("Habit Name")
        habit_category = st.selectbox("Category", ["Health", "Productivity", "Personal Development", "Other"])
        habit_goal = st.number_input("Daily Goal (times)", min_value=1, max_value=10, value=1)
        
        if st.button("Add Habit"):
            if habit_name:
                # Check if habit already exists
                existing_habits = [h['name'] for h in st.session_state.habits]
                if habit_name in existing_habits:
                    st.error("This habit already exists!")
                else:
                    # Initialize tracking for 30 days
                    today = datetime.now().date()
                    tracking = {}
                    for i in range(30):
                        date = (today - timedelta(days=i)).strftime('%Y-%m-%d')
                        tracking[date] = 0
                    
                    st.session_state.habits.append({
                        'name': habit_name,
                        'category': habit_category,
                        'goal': habit_goal,
                        'tracking': tracking
                    })
                    save_data()
                    st.success("Habit added successfully!")
                    st.experimental_rerun()
    
    with col2:
        # Get current date
        today = datetime.now().date().strftime('%Y-%m-%d')
        
        if not st.session_state.habits:
            st.info("No habits defined yet. Add some habits to start tracking!")
        else:
            st.subheader("Track Today's Habits")
            
            for i, habit in enumerate(st.session_state.habits):
                # Ensure today is in the tracking
                if today not in habit['tracking']:
                    habit['tracking'][today] = 0
                
                # Display habit tracking card
                st.markdown(f"""
                <div class='habit-card'>
                    <h4>{habit['name']}</h4>
                    <p>Category: {habit['category']}</p>
                    <p>Goal: {habit['tracking'][today]}/{habit['goal']} times today</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Track button and delete button
                col1, col2 = st.columns([1, 1])
                with col1:
                    if st.button(f"Track", key=f"track_habit_{i}"):
                        habit['tracking'][today] += 1
                        save_data()
                        st.experimental_rerun()
                with col2:
                    if st.button(f"Delete Habit", key=f"del_habit_{i}"):
                        st.session_state.habits.pop(i)
                        save_data()
                        st.experimental_rerun()
                
                # Show progress
                progress = min(1.0, habit['tracking'][today] / habit['goal'])
                st.progress(progress)
                
                st.markdown("---")
    
    # Visualization of habits
    st.subheader("Habit Progress")
    
    if st.session_state.habits:
        # Get dates for the last 7 days
        dates = [(datetime.now().date() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]
        dates.reverse()  # Show oldest to newest
        
        # Prepare data for visualization
        habit_data = []
        
        for habit in st.session_state.habits:
            for date in dates:
                if date in habit['tracking']:
                    value = habit['tracking'][date]
                    percentage = min(100, (value / habit['goal']) * 100)
                else:
                    percentage = 0
                
                habit_data.append({
                    'Habit': habit['name'],
                    'Date': date,
                    'Completion': percentage
                })
        
        # Create dataframe for visualization
        habit_df = pd.DataFrame(habit_data)
        
        # Create heatmap visualization
        fig = px.imshow(
            habit_df.pivot(index='Habit', columns='Date', values='Completion'),
            labels=dict(color="Completion %"),
            x=dates,
            color_continuous_scale='blues',
            aspect="auto",
            height=300
        )
        
        fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
        st.plotly_chart(fig, use_container_width=True)

# Expense & Finance Tracker
elif nav_option == "Finance Tracker":
    st.header("Expense & Finance Tracker")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Add Expense")
        
        expense_date = st.date_input("Date", value=datetime.now())
        expense_amount = st.number_input("Amount", min_value=0.01, step=0.01)
        expense_category = st.selectbox("Category", ["Food", "Transportation", "Housing", "Entertainment", "Shopping", "Utilities", "Other"])
        expense_description = st.text_input("Description (optional)")
        
        if st.button("Add Expense"):
            if expense_amount > 0:
                st.session_state.expenses.append({
                    'date': expense_date.strftime('%Y-%m-%d'),
                    'amount': expense_amount,
                    'category': expense_category,
                    'description': expense_description
                })
                save_data()
                st.success("Expense added successfully!")
                st.experimental_rerun()
    
    with col2:
        # Create tabs for different views
        tab1, tab2 = st.tabs(["Recent Expenses", "Financial Summary"])
        
        with tab1:
            if not st.session_state.expenses:
                st.info("No expenses recorded yet. Add some expenses to start tracking!")
            else:
                # Sort expenses by date (newest first)
                sorted_expenses = sorted(st.session_state.expenses, 
                                       key=lambda x: x['date'], 
                                       reverse=True)
                
                # Show recent expenses
                st.subheader("Recent Expenses")
                
                for i, expense in enumerate(sorted_expenses[:10]):  # Show only 10 most recent
                    col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 0.8, 0.5])
                    with col1:
                        st.write(expense['date'])
                    with col2:
                        st.write(f"${expense['amount']:.2f}")
                    with col3:
                        st.write(expense['description'] if expense['description'] else "-")
                    with col4:
                        st.write(expense['category'])
                    with col5:
                        if st.button("🗑️", key=f"del_expense_{i}"):
                            original_index = st.session_state.expenses.index(expense)
                            st.session_state.expenses.pop(original_index)
                            save_data()
                            st.experimental_rerun()
                    
                    st.markdown("---")
        
        with tab2:
            if not st.session_state.expenses:
                st.info("No expenses recorded yet. Add some expenses to see your financial summary!")
            else:
                # Create expense dataframe
                expense_df = pd.DataFrame(st.session_state.expenses)
                
                # Convert date strings to datetime
                expense_df['date'] = pd.to_datetime(expense_df['date'])
                
                # Get current month expenses
                current_month = datetime.now().month
                current_year = datetime.now().year
                current_month_expenses = expense_df[
                    (expense_df['date'].dt.month == current_month) & 
                    (expense_df['date'].dt.year == current_year)
                ]
                
                # Calculate monthly total
                monthly_total = current_month_expenses['amount'].sum()
                
                st.metric("Current Month Total", f"${monthly_total:.2f}")
                
                # Create category pie chart
                category_totals = current_month_expenses.groupby('category')['amount'].sum().reset_index()
                
                fig = px.pie(
                    category_totals, 
                    values='amount', 
                    names='category',
                    title='Expenses by Category',
                    hole=0.4,
                    color_discrete_sequence=px.colors.sequential.Pastel
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
                # Monthly trend (if data spans multiple months)
                if len(expense_df['date'].dt.to_period('M').unique()) > 1:
                    # Group by month
                    monthly_trend = expense_df.groupby(expense_df['date'].dt.to_period('M'))['amount'].sum().reset_index()
                    monthly_trend['date'] = monthly_trend['date'].astype(str)
                    
                    # Create bar chart
                    fig = px.bar(
                        monthly_trend,
                        x='date',
                        y='amount',
                        title='Monthly Expense Trend',
                        labels={'date': 'Month', 'amount': 'Total Expenses ($)'},
                        color_discrete_sequence=['#9CC0F9']
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)