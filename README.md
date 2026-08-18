# 📓 VibeDiary

### Your Thoughts. Your Vibe.

VibeDiary is a personalized digital diary and mood-tracking web application that provides users with a private space to record thoughts, memories, emotions, and daily experiences.

It combines digital journaling with mood tracking, smart search, organization, analytics, and personalized insights to create a more meaningful journaling experience.

---

## 🎯 Purpose

The purpose of VibeDiary is to make digital journaling more organized, interactive, and insightful.

It allows users to:

- Record and manage personal diary entries
- Track their moods
- Organize memories using categories and tags
- Search and filter previous entries
- View personal journaling and mood insights
- Securely manage their private diary

---

## ❗ Problem Statement

Traditional diaries provide a simple way to record thoughts and memories, but they offer limited capabilities for organizing large numbers of entries, finding specific memories, tracking moods, and understanding personal journaling patterns.

VibeDiary addresses these limitations by combining **journaling, mood tracking, search, organization, analytics, and user authentication** in one platform.

---

# ✨ Features

## 📖 Core Features

- **Digital Diary** — Create, view, edit, and delete personal diary entries.
- **Mood Tracking** — Associate moods with diary entries and maintain mood history.
- **User Authentication** — Registration, login, logout, sessions, and protected user data.
- **Personal Dashboard** — Overview of recent entries, moods, activity, and insights.
- **Search** — Search diary entries by title, content, or keywords.
- **Categories & Tags** — Organize entries using categories and custom tags.
- **Favorites** — Mark important diary entries for quick access.
- **Diary History** — Browse entries chronologically and by date.

---

# 🚀 Advanced Features

- **Advanced Search & Filtering** — Combine keyword, mood, date, category, and tag filters.
- **Mood Analytics** — Visualize mood distribution and mood trends over time.
- **Personal Insights** — Generate statistics and patterns from journaling activity.
- **Journaling Statistics** — Track entry frequency, active days, and writing habits.
- **Timeline View** — Explore diary entries through a chronological timeline.
- **Calendar View** — Navigate entries based on specific dates.
- **Image Attachments** — Associate images with personal memories.
- **Export Entries** — Allow users to export their diary data.
- **Personalized Dashboard** — Display information based on the user's activity and preferences.

---

# 🤖 Intelligent Features

VibeDiary can be extended with AI-powered functionality such as:

- **Sentiment Analysis** — Analyze the overall sentiment of diary entries.
- **Emotion Detection** — Identify emotions expressed through journal content.
- **AI Journal Insights** — Generate meaningful observations from journaling patterns.
- **Smart Journal Prompts** — Suggest prompts based on previous entries and moods.
- **Personal Reflection Assistant** — Provide reflective questions based on journaling history.

---

# 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | Flask |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite |
| ORM | SQLAlchemy |
| Authentication | Flask Sessions / Authentication Library |
| Password Security | Werkzeug |
| Version Control | Git |
| Repository | GitHub |
| Development Environment | Visual Studio Code |

---

# 🏗️ System Architecture

```text
                         ┌─────────────────┐
                         │    VibeDiary    │
                         └────────┬────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
             ┌──────▼──────┐             ┌──────▼──────┐
             │  Frontend   │             │   Backend   │
             │             │             │             │
             │ HTML5       │             │ Python      │
             │ CSS3        │             │ Flask       │
             │ JavaScript  │             │             │
             └──────┬──────┘             └──────┬──────┘
                    │                           │
                    └─────────────┬─────────────┘
                                  │
                           ┌──────▼──────┐
                           │ SQLAlchemy  │
                           │     ORM     │
                           └──────┬──────┘
                                  │
                           ┌──────▼──────┐
                           │   SQLite    │
                           │   Database  │
                           └─────────────┘
```

---

# 🗄️ Database Overview

VibeDiary uses a relational database to store user and diary information.

### Main Entities

**User**
**Diary Entry**
**Tag**

The relationship between users and diary entries ensures that each user's diary data remains associated with their account.

---

# 🔐 Authentication & Security

VibeDiary is designed to protect personal diary information through:

- User authentication
- Password hashing
- Session management
- Protected routes
- User-specific database access
- Input validation
- Secure secret-key management
- Environment variables for sensitive configuration

Users should only be able to access their own private diary data.

---

# 🧩 Main Modules

```text
VibeDiary
│
├── Authentication Module
│   ├── Registration
│   ├── Login
│   ├── Logout
│   └── Session Management
│
├── Diary Module
│   ├── Create Entry
│   ├── View Entry
│   ├── Edit Entry
│   └── Delete Entry
│
├── Mood Module
│   ├── Mood Selection
│   ├── Mood History
│   └── Mood Analytics
│
├── Search Module
│   ├── Keyword Search
│   ├── Filtering
│   └── Advanced Search
│
├── Organization Module
│   ├── Categories
│   ├── Tags
│   └── Favorites
│
└── Insights Module
    ├── Statistics
    ├── Mood Trends
    └── Journaling Patterns
```

---

# 🔄 Application Workflow

```text
              Landing Page
                    │
                    ▼
          Register / Login
                    │
                    ▼
             Dashboard
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Diary       Mood       Insights
        │        Tracking        │
        ▼           │            ▼
   Create/Edit      │        Analytics
   /Delete          │
        │           │
        └─────┬─────┘
              ▼
       Search & Filter
              │
              ▼
        Personal History
```

---

---

# 📊 Personal Insights

The insights module focuses on converting diary and mood data into useful information.

It can provide:

- Total diary entries
- Most common mood
- Mood distribution
- Mood trends
- Journaling frequency
- Most active days
- Monthly activity
- Frequently used categories and tags

Charts and visualizations can be used to make these patterns easier to understand.

---

# 🧪 Testing

The application will be tested across:

- User registration and login
- Authentication and authorization
- Diary CRUD operations
- Mood tracking
- Search and filtering
- Database operations
- User data isolation
- Form validation
- Responsive user interface
- Application functionality

---


# 🎯 Project Goals

VibeDiary aims to demonstrate how a complete full-stack application can combine:

**Frontend + Backend + Database + Authentication + Data Management + Analytics + User Experience**

The project focuses on building a practical application rather than a simple static website.

---

