# Vocabulary Trainer 📚
A desktop application for learning and practicing vocabulary with interactive quizzes.

## Features
### 🗂️ Dictionary Management
- **Add words** with translations
- **Remove words** from collection
- **View all words** in scrollable format

### 🎯 Quiz System
- **Three difficulty levels:**
  - 🟢 **Easy** - No time limits, hints
  - 🟡 **Medium** - Time limits (5 second per 1 word)
  - 🔴 **Hard** - Strict time limits (3 second per 1 word)
- **Three question modes:**
  - Word → Translation
  - Translation → Word
  - Mixed mode
- **Customizable question count**
  - Minimum 1 word
  - Maximum 20 words

### 🎮 Interactive Features
- Real-time timer display
- First-letter hints (Easy mode)
- Question skipping
- Answer statistics tracking
- Keyboard shortcuts (Enter to submit)

## Installation
### Setup
1. Clone/download the repository
2. Run the application:
```bash
python main.py
```
## Project Structure
```
vocabulary_trainer/
├── src/
│   ├── __init__.py
│   └── vocabulary_trainer/
│       ├── __init__.py
│       ├── core/                   
│       │   ├── __init__.py
│       │   ├── exceptions.py            
│       │   └── models.py        
│       ├── dictionary/              
│       │   ├── __init__.py
│       │   ├── add_word.py       
│       │   ├── remove_word.py       
│       │   └── show_all_words.py        
│       ├── quiz_session/                
│       │   ├── __init__.py
│       │   ├── ask_questions.py            
│       │   ├── quiz_mode.py   
│       │   └── test_difficulty.py        
│       ├── ui/                      
│       │   ├── __init__.py     
│       └── └── menu.py    
├── .gitignore
├── main.py
├── pyproject.toml
└── README.md
```

## 🚀 Quick Start Guide

### 1. Add Vocabulary
1. **Click** "➕ Add Word" button
2. **Enter** word and its translation
3. **Click** "Add" to save to dictionary
4. **Repeat** for additional words

### 2. Review Words
1. **Click** "📋 Show All Words" button
2. **Scroll** through your vocabulary list
3. **Review** words and translations
4. **Close** window when finished

### 3. Take a Quiz
1. **Click** "📝 Start Quiz" button
2. **Configure** quiz settings:
   - **Difficulty**: Easy/Medium/Hard *(Hint button only appears in Easy mode)*
   - **Words**: 1-20 questions (slider)
   - **Mode**: Direction of translation
3. **Click** "Start" to begin

### 4. Results Screen
After completing all questions:
- **Score percentage** calculated
- **Correct answers** count displayed
- **Personalized feedback** provided
- **Word statistics** automatically updated

## ⌨️ Keyboard Shortcuts
| Key | Action |
|-----|--------|
| **Enter** | Submit current answer |
| **Tab** | Navigate between UI elements |
| *Auto-focus* | Answer field is automatically selected |

## 📊 Scoring System
| Score Range | Feedback Message | Emoji |
|-------------|-----------------|-------|
| **90-100%** | Outstanding performance! | 🏆 |
| **80-89%**  | Excellent work! | 🎉 |
| **60-79%**  | Good job! | 👍 |
| **40-59%**  | Keep practicing! | 📚 |
| **0-39%**   | Don't give up! Practice makes perfect. | 💪 |

## ⚠️ Error Handling & Validation
| Error Type | Prevention Method |
|------------|------------------|
| **Empty Dictionary** | Warning message prevents quiz start |
| **Empty Word Entry** | Validation prevents saving empty words |
| **Quiz Errors** | Exception catching prevents crashes |
| **Invalid Input** | Field validation with user feedback |

## ⏱️ Time Limits by Difficulty
| Level | Time Limit | Features |
|-------|------------|----------|
| **Easy** | No limit | ✓ Hints available<br>✓ Relaxed timing |
| **Medium** | 30 seconds/word | ⏱️ Timer visible<br>⏳ Moderate pressure |
| **Hard** | 15 seconds/word | ⚡ Strict timing<br>🏁 Fast-paced |
