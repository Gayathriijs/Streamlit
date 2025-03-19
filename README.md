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

## 🖼️ Screenshots

![Home Dashboard](https://raw.githubusercontent.com/username/lifestyle-hub/main/images/home-dashboard.png)
![Calendar View](https://raw.githubusercontent.com/username/lifestyle-hub/main/images/calendar.png)
![Habit Tracker](https://raw.githubusercontent.com/username/lifestyle-hub/main/images/habit-tracker.png)

## 🚀 Installation

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

5. Open your browser and navigate to `http://localhost:8501`

## 📦 Dependencies

- streamlit
- pandas
- plotly
- datetime
- random
- json
- os
- calendar

## 💾 Data Storage

The application stores all user data locally in a JSON file (`user_data.json`). This includes:

- Calendar events
- Long-term to-do items
- Habit tracking data
- Expense records

Daily to-do items reset each day and are stored in session state.

## 🎨 Customization

### Theme

The application supports both light and dark modes. You can toggle between them using the theme button in the sidebar.

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

## 🔧 Advanced Usage

### Custom Affirmations

You can add your own affirmations in the Affirmations section. These will be saved and might appear as your daily affirmation.

### Expense Analysis

The Finance Tracker provides visual analysis of your spending patterns, including:
- Category breakdown with pie charts
- Monthly expense trends with bar charts
- Current month total expenses

### Habit Heatmap

The Habit Tracker includes a heatmap visualization showing your habit completion over time, helping you identify patterns and consistency.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔮 Future Enhancements

- User authentication system
- Cloud synchronization
- Mobile app version
- Integration with external calendars (Google, Outlook)
- Export/import data functionality
- Data visualization enhancements
- Customizable dashboard widgets

## 📬 Contact

Your Name - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Project Link: [https://github.com/username/lifestyle-hub](https://github.com/username/lifestyle-hub)
