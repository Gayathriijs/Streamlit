# Lifestyle Hub


> A comprehensive personal lifestyle management web application built with Streamlit

## Overview

Lifestyle Hub is an all-in-one personal lifestyle management application that helps you organize your daily activities, track habits, manage finances, and maintain a positive mindset. Built with Streamlit, this application provides a clean and intuitive interface for managing various aspects of your life in one place.

## Features

- **Home Dashboard**: Get a quick overview of your day with personalized greetings, affirmations, and quick access to important information
- **Calendar**: Track events and appointments with a visual calendar interface
- **Daily Affirmations**: Start your day with positive affirmations or create your own
- **Daily Planner**: Manage your daily tasks and long-term goals
- **Habit Tracker**: Define and track your habits with visual progress indicators
- **Finance Tracker**: Monitor your expenses and visualize spending patterns

## Screenshots

![Home Dashboard]![Screenshot 2025-03-19 220521](https://github.com/user-attachments/assets/c0276083-0a9b-4d5d-9813-6116e62cca19)
)
![Calendar View]![image](https://github.com/user-attachments/assets/06338b4b-c032-4f3e-8148-b6498b444479)
)
![Habit tracker]![image](https://github.com/user-attachments/assets/72cf0dec-c34d-47f8-8b90-5ebde25e5fdf)
)
![Affirmations]!![image](https://github.com/user-attachments/assets/1e92f236-f6c5-4b1d-ae88-4927282b7f02)
)
![daily planner]!![Screenshot 2025-03-19 222356](https://github.com/user-attachments/assets/9e6eb926-6650-4d3e-8912-2c5114979f74)
)
![Long term planner]![image](https://github.com/user-attachments/assets/65ab0288-73b7-4360-8451-aec2a9a5f6eb)
)
![Finance tracker]!![Screenshot 2025-03-19 223004](https://github.com/user-attachments/assets/63ffc169-5230-4c7f-be1b-0a674a97d605)
)

## Installation

### Prerequisites

- Python 3.7+
- pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/username/lifestyle-hub.git
   cd lifestyle-hub
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```


## Dependencies

- streamlit
- pandas
- plotly
- datetime
- random
- json
- os
- calendar

## Data Storage

The application stores all user data locally in a JSON file (`user_data.json`). This includes:

- Calendar events
- Long-term to-do items
- Habit tracking data
- Expense records

Daily to-do items reset each day and are stored in session state.

## Customization


### Custom CSS

You can customize the appearance by modifying the `style.css` file. The application uses CSS variables for consistent theming:

```css
:root {
    --primary-color: #8bb8e8;
    --secondary-color: #b6cfe9;
    --accent-color: #ffd6dc;
    /* ... other variables ... */
}
```

## Advanced Usage

### Custom Affirmations

You can add your own affirmations in the Affirmations section. These will be saved and might appear as your daily affirmation.

### Expense Analysis

The Finance Tracker provides visual analysis of your spending patterns, including:
- Category breakdown with pie charts
- Monthly expense trends with bar charts
- Current month total expenses

### Habit Heatmap

The Habit Tracker includes a heatmap visualize

## Future Enhancements

- User authentication system
- Cloud synchronization
- Mobile app version
- Integration with external calendars (Google, Outlook)
- Export/import data functionality
- Data visualization enhancements
- Customizable dashboard widgets

## Contact

Gayathri J S - [Gmail](gayathri.js.official@gmail.com)

Project Link: [Github project link ](https://github.com/Gayathriijs/Streamlit/tree/15df74f7be160d4f589cafd79d2577823bcce8aa)
