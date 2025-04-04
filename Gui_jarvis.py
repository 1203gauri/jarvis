import bpy

# Delete default cube
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Add human-like head mesh
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))
ai_face = bpy.context.object
ai_face.name = "JARVIS_Face"

# Set material to glowing blue
material = bpy.data.materials.new(name="AI_Face_Material")
material.use_nodes = True
ai_face.data.materials.append(material)

print("✅ J.A.R.V.I.S AI Face Created!")
# Switch to Pose Mode
bpy.ops.object.armature_add(enter_editmode=False, location=(0, 0, 0))
bpy.ops.object.mode_set(mode='POSE')

# Move forward & back
bpy.ops.object.posemode_toggle()
bpy.ops.transform.translate(value=(2, 0, 0))
bpy.ops.object.mode_set(mode='OBJECT')

print("✅ Movement Animation Applied!")
import sys
import pyttsx3
import speech_recognition as sr
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QMovie

class JarvisApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.engine = pyttsx3.init()

    def initUI(self):
        """Initialize J.A.R.V.I.S GUI"""
        self.setWindowTitle("J.A.R.V.I.S AI Assistant")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: black; color: cyan;")

        layout = QVBoxLayout()

        # Add AI Animation
        self.ai_animation = QLabel(self)
        self.movie = QMovie("jarvis_animation.gif")  # Use a real Blender render here
        self.ai_animation.setMovie(self.movie)
        self.movie.start()
        layout.addWidget(self.ai_animation)

        # Text Output Box
        self.textbox = QTextEdit(self)
        self.textbox.setReadOnly(True)
        self.textbox.setStyleSheet("background-color: black; color: cyan; font-size: 14px; padding: 5px;")
        layout.addWidget(self.textbox)

        # Speak Button
        self.btn_listen = QPushButton("🎤 Speak", self)
        self.btn_listen.setStyleSheet("background-color: red; color: white; font-size: 16px; padding: 10px;")
        self.btn_listen.clicked.connect(self.voice_command)
        layout.addWidget(self.btn_listen)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def voice_command(self):
        """Take voice input & respond"""
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.textbox.append("Listening...")
            recognizer.pause_threshold = 1
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio, language="en-in")
                self.textbox.append(f"👤 User: {command}")
                self.process_command(command)
            except sr.UnknownValueError:
                self.textbox.append("Sorry, I couldn't understand.")
            except sr.RequestError:
                self.textbox.append("Please check your internet connection.")

    def process_command(self, query):
        """Process user commands"""
        response = "I'm not sure about that command."
        if "who are you" in query:
            response = "I am J.A.R.V.I.S, your AI assistant."
        elif "open youtube" in query:
            response = "Opening YouTube..."
        elif "exit" in query:
            sys.exit()

        self.textbox.append(f"🤖 J.A.R.V.I.S: {response}")
        self.engine.say(response)
        self.engine.runAndWait()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jarvis = JarvisApp()
    jarvis.show()
    sys.exit(app.exec())


