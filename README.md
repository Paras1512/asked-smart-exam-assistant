# asked-smart-exam-assistant
Asked Smart Exam Assistant is a web app built with Flask and powered by LLaMA. It provides AI-driven answers based on uploaded lecture notes, helping students prepare for exams. Features include file parsing, a luxurious dark theme, theme toggle, smooth animations, and instant answer generation for an efficient study experience.

# 🧠 asked-smart-exam-assistant

An intelligent exam assistant that automatically generates answers from your uploaded lecture notes using local LLMs like LLaMA 3. Designed with a sleek, modern UI and smart backend processing — your ultimate tool to ace exams effortlessly!

---

## 🚀 Features

- 📄 **Upload Lecture Notes**: Supports PDFs and text files.
- 🧠 **Local LLM Integration**: Uses **Ollama** to run LLaMA 3 models locally.
- ✨ **Beautiful UI**:
  - Luxurious dark theme inspired by Apple.
  - Parallax background, animated icons, and smooth fade-in effects.
  - Glassmorphism answer cards.
  - Toggle between dark and light themes.
- ⏳ **Loading Spinner**: Appears while generating the answer.
- 📜 **Auto-generated Answers**: Based on uploaded notes using advanced LLM reasoning.

---

## 🔧 Libraries Used

### 🐍 Backend (Python)

- `Flask` – Lightweight web framework
- `requests` – For handling HTTP requests (if used for APIs)
- `PyMuPDF` (`fitz`) – For PDF parsing
- `python-dotenv` – To load environment variables (optional)
- `werkzeug` – For secure file handling
- `uuid` – For generating unique filenames
- `os`, `io`, `time`, `json` – Standard Python libs

### 💻 Frontend

- `TailwindCSS` – For beautiful, responsive UI
- `Vanilla JavaScript` – For interactivity and animations
- `Animate.css` – Smooth fade-ins and transitions (optional)
- `Font Awesome / Custom Icons` – Floating glassy icons
- `Parallax.js` or custom parallax effect
- `Dark/Light Mode Toggle` – Custom implementation

### 🤖 LLMs

- `Ollama` – For running local LLMs
- `LLaMA 3` – Language model used for answer generation

---

## 🛠️ Tech Stack

- **Frontend**: HTML, TailwindCSS, JavaScript
- **Backend**: Python, Flask
- **LLM Engine**: Ollama + LLaMA 3

---
📁 Project Structure
asked-smart-exam-assistant/  
├── static/   
│   ├── css/  
│   ├── js/  
├── templates/  
│   └── index.html  
├── app.py  
├── requirements.txt  
└── README.md  
------
🖥️ This Our UI:
![image](https://github.com/user-attachments/assets/d5cd7fdf-762f-42b9-a91b-3ab752eb3dda)
📤This is the Output:
![Screenshot 2025-04-21 100009](https://github.com/user-attachments/assets/c5a33c51-39d6-414b-b591-9f9f6d8c765b)
--------------
Made By:  
Jay Dhrangadhariya - KU2407U300  
Paras Panchal - KU2407U344  
Krushnrajsinh Sisodiya - KU2407U322  
Vishwajitsinh Sarvaiya - KU2407U860  
--------------

📜 License
This project is licensed under the MIT License.
