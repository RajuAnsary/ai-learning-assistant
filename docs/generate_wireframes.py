#!/usr/bin/env python3
"""
Generate UI Wireframes as PNG images for AI-Powered Learning Assistant
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_chat_wireframe():
    """Create Chat-Based Learning Interface wireframe"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 16))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Header
    header = FancyBboxPatch((0.2, 14.5), 9.6, 1.2, 
                           boxstyle="round,pad=0.1", 
                           facecolor='#2E86AB', edgecolor='black', linewidth=2)
    ax.add_patch(header)
    ax.text(5, 15.1, 'AI Learning Assistant', ha='center', va='center', 
            fontsize=16, fontweight='bold', color='white')
    ax.text(8.5, 15.1, '[Profile]', ha='center', va='center', 
            fontsize=10, color='white')
    
    # User Message
    user_msg = FancyBboxPatch((1, 12.5), 8, 1.5, 
                             boxstyle="round,pad=0.1", 
                             facecolor='#E8F4FD', edgecolor='#2E86AB', linewidth=1)
    ax.add_patch(user_msg)
    ax.text(1.3, 13.5, '💬 User:', ha='left', va='center', fontsize=12, fontweight='bold')
    ax.text(1.3, 13, '"What is a REST API?"', ha='left', va='center', fontsize=11)
    
    # Assistant Response
    assistant_msg = FancyBboxPatch((0.5, 4), 9, 8, 
                                  boxstyle="round,pad=0.2", 
                                  facecolor='#F8F9FA', edgecolor='#28A745', linewidth=2)
    ax.add_patch(assistant_msg)
    
    ax.text(0.8, 11.5, '🤖 Assistant:', ha='left', va='center', fontsize=12, fontweight='bold', color='#28A745')
    
    # Explanation text
    explanation = """A REST API is like a waiter in a restaurant. You (the client) 
make a request for food (data), and the waiter brings it 
from the kitchen (server)."""
    ax.text(0.8, 10.8, explanation, ha='left', va='top', fontsize=10, wrap=True)
    
    # Key Points
    ax.text(0.8, 9.5, '📝 Key Points:', ha='left', va='center', fontsize=11, fontweight='bold')
    ax.text(1, 9, '• REST = Representational State Transfer', ha='left', va='center', fontsize=10)
    ax.text(1, 8.6, '• Uses HTTP methods (GET, POST, PUT, DELETE)', ha='left', va='center', fontsize=10)
    ax.text(1, 8.2, '• Returns data in JSON format', ha='left', va='center', fontsize=10)
    
    # Code Example
    code_box = FancyBboxPatch((0.8, 5.5), 8.4, 2, 
                             boxstyle="round,pad=0.1", 
                             facecolor='#F8F8F8', edgecolor='gray', linewidth=1)
    ax.add_patch(code_box)
    ax.text(0.9, 7.2, '💻 Example:', ha='left', va='center', fontsize=11, fontweight='bold')
    code_text = """fetch('/api/users')
  .then(response => response.json())
  .then(data => console.log(data));"""
    ax.text(0.9, 6.5, code_text, ha='left', va='top', fontsize=9, fontfamily='monospace')
    
    # Next Step
    ax.text(0.8, 4.8, '🎯 Next: Learn about HTTP status codes', ha='left', va='center', fontsize=10, color='#007BFF')
    
    # Input Area
    input_box = FancyBboxPatch((0.2, 0.5), 9.6, 1.2, 
                              boxstyle="round,pad=0.1", 
                              facecolor='white', edgecolor='gray', linewidth=2)
    ax.add_patch(input_box)
    ax.text(0.5, 1.1, 'Type your question here...', ha='left', va='center', fontsize=10, color='gray')
    
    # Buttons
    send_btn = FancyBboxPatch((7.5, 0.7), 1, 0.8, 
                             boxstyle="round,pad=0.05", 
                             facecolor='#007BFF', edgecolor='#007BFF')
    ax.add_patch(send_btn)
    ax.text(8, 1.1, 'Send', ha='center', va='center', fontsize=10, color='white', fontweight='bold')
    
    mic_btn = FancyBboxPatch((8.7, 0.7), 0.8, 0.8, 
                            boxstyle="round,pad=0.05", 
                            facecolor='#6C757D', edgecolor='#6C757D')
    ax.add_patch(mic_btn)
    ax.text(9.1, 1.1, '🎤', ha='center', va='center', fontsize=12)
    
    plt.title('Chat-Based Learning Interface', fontsize=18, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('wireframe_chat_interface.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_code_assistance_wireframe():
    """Create Code Assistance Screen wireframe"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 16))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Header
    header = FancyBboxPatch((0.2, 14.5), 9.6, 1.2, 
                           boxstyle="round,pad=0.1", 
                           facecolor='#DC3545', edgecolor='black', linewidth=2)
    ax.add_patch(header)
    ax.text(2, 15.1, 'Code Assistant', ha='left', va='center', 
            fontsize=16, fontweight='bold', color='white')
    ax.text(8.5, 15.1, '[History] [Settings] [?]', ha='center', va='center', 
            fontsize=10, color='white')
    
    # Code Input Section
    ax.text(0.5, 13.8, '📝 Your Code:', ha='left', va='center', fontsize=12, fontweight='bold')
    
    code_input = FancyBboxPatch((0.5, 10.5), 9, 3, 
                               boxstyle="round,pad=0.1", 
                               facecolor='#F8F8F8', edgecolor='gray', linewidth=2)
    ax.add_patch(code_input)
    
    # Code with error
    code_text = """function calculateTotal(items) {
  let total = 0;
  for (let i = 0; i <= items.length; i++) {    ← ERROR
    total += items[i].price;
  }
  return total;
}"""
    ax.text(0.7, 12.8, code_text, ha='left', va='top', fontsize=9, fontfamily='monospace')
    
    # Analysis Results
    ax.text(0.5, 10, '🔍 Analysis Results:', ha='left', va='center', fontsize=12, fontweight='bold')
    
    # Error Box
    error_box = FancyBboxPatch((0.5, 7.5), 9, 2.2, 
                              boxstyle="round,pad=0.1", 
                              facecolor='#F8D7DA', edgecolor='#DC3545', linewidth=2)
    ax.add_patch(error_box)
    
    ax.text(0.7, 9.4, '❌ Issue Found: Array Index Out of Bounds', ha='left', va='center', 
            fontsize=11, fontweight='bold', color='#721C24')
    ax.text(0.7, 9, 'Line 3: `i <= items.length` should be `i < items.length`', ha='left', va='center', 
            fontsize=10, color='#721C24')
    
    ax.text(0.7, 8.5, '💡 Why this happens:', ha='left', va='center', fontsize=10, fontweight='bold')
    explanation = """Arrays are zero-indexed. If you have 3 items, valid indexes are 0, 1, 2.
Using <= tries to access index 3 which doesn't exist."""
    ax.text(0.7, 8, explanation, ha='left', va='top', fontsize=9)
    
    # Fixed Code
    ax.text(0.5, 7, '✅ Fixed Code:', ha='left', va='center', fontsize=11, fontweight='bold', color='#28A745')
    
    fixed_box = FancyBboxPatch((0.5, 5), 9, 1.5, 
                              boxstyle="round,pad=0.1", 
                              facecolor='#D4EDDA', edgecolor='#28A745', linewidth=1)
    ax.add_patch(fixed_box)
    
    fixed_code = """for (let i = 0; i < items.length; i++) {
  total += items[i].price;
}"""
    ax.text(0.7, 6.2, fixed_code, ha='left', va='top', fontsize=9, fontfamily='monospace')
    
    # Learning Tip
    tip_box = FancyBboxPatch((0.5, 3.5), 9, 1, 
                            boxstyle="round,pad=0.1", 
                            facecolor='#FFF3CD', edgecolor='#FFC107', linewidth=1)
    ax.add_patch(tip_box)
    ax.text(0.7, 4, '🎓 Learning Tip: Always use < with .length in loops', ha='left', va='center', 
            fontsize=10, fontweight='bold', color='#856404')
    
    # Action Buttons
    buttons = ['Paste Code', 'Upload File', 'Analyze', 'Ask Follow-up']
    for i, btn_text in enumerate(buttons):
        btn = FancyBboxPatch((0.5 + i*2.3, 1), 2, 0.8, 
                            boxstyle="round,pad=0.05", 
                            facecolor='#007BFF', edgecolor='#007BFF')
        ax.add_patch(btn)
        ax.text(1.5 + i*2.3, 1.4, btn_text, ha='center', va='center', 
                fontsize=9, color='white', fontweight='bold')
    
    plt.title('Code Assistance Screen', fontsize=18, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('wireframe_code_assistance.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_learning_path_wireframe():
    """Create Learning Path Screen wireframe"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 16))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 16)
    ax.axis('off')
    
    # Header
    header = FancyBboxPatch((0.2, 14.5), 9.6, 1.2, 
                           boxstyle="round,pad=0.1", 
                           facecolor='#28A745', edgecolor='black', linewidth=2)
    ax.add_patch(header)
    ax.text(2, 15.1, 'Learning Path', ha='left', va='center', 
            fontsize=16, fontweight='bold', color='white')
    ax.text(8, 15.1, '[Goals] [Progress]', ha='center', va='center', 
            fontsize=10, color='white')
    
    # Progress Bar
    progress_bg = FancyBboxPatch((0.5, 13.5), 9, 0.8, 
                                boxstyle="round,pad=0.05", 
                                facecolor='#E9ECEF', edgecolor='gray', linewidth=1)
    ax.add_patch(progress_bg)
    
    progress_fill = FancyBboxPatch((0.5, 13.5), 5.85, 0.8, 
                                  boxstyle="round,pad=0.05", 
                                  facecolor='#28A745', edgecolor='#28A745')
    ax.add_patch(progress_fill)
    
    ax.text(5, 13.9, '👤 Your Progress: Beginner → Intermediate (65%)', ha='center', va='center', 
            fontsize=11, fontweight='bold', color='white')
    
    # Completed Topics
    ax.text(0.5, 12.8, '✅ Completed Topics:', ha='left', va='center', fontsize=12, fontweight='bold')
    
    completed_box = FancyBboxPatch((0.5, 9.5), 9, 3, 
                                  boxstyle="round,pad=0.1", 
                                  facecolor='#D4EDDA', edgecolor='#28A745', linewidth=1)
    ax.add_patch(completed_box)
    
    topics = [
        ('✓ Variables & Data Types', 'Jan 15'),
        ('✓ Functions & Parameters', 'Jan 18'),
        ('✓ Arrays & Objects', 'Jan 22'),
        ('✓ Loops & Conditionals', 'Jan 25')
    ]
    
    for i, (topic, date) in enumerate(topics):
        y_pos = 12 - i*0.5
        ax.text(0.8, y_pos, topic, ha='left', va='center', fontsize=10, color='#155724')
        ax.text(8.5, y_pos, f'📅 {date}', ha='right', va='center', fontsize=9, color='#155724')
    
    # Recommended Next Steps
    ax.text(0.5, 9, '🎯 Recommended Next Steps:', ha='left', va='center', fontsize=12, fontweight='bold')
    
    # Recommendation 1
    rec1_box = FancyBboxPatch((0.5, 6.5), 9, 2, 
                             boxstyle="round,pad=0.1", 
                             facecolor='#FFF3CD', edgecolor='#FFC107', linewidth=2)
    ax.add_patch(rec1_box)
    
    ax.text(0.8, 8.2, '1. 🔥 REST APIs & HTTP Requests', ha='left', va='center', 
            fontsize=11, fontweight='bold')
    ax.text(0.8, 7.8, '⏱️ ~2 hours | 🎯 High Priority', ha='left', va='center', fontsize=9)
    ax.text(0.8, 7.4, '"Perfect next step after learning objects!"', ha='left', va='center', 
            fontsize=9, style='italic')
    
    start_btn1 = FancyBboxPatch((7, 6.8), 2, 0.6, 
                               boxstyle="round,pad=0.05", 
                               facecolor='#FFC107', edgecolor='#FFC107')
    ax.add_patch(start_btn1)
    ax.text(8, 7.1, 'Start Learning', ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Recommendation 2
    rec2_box = FancyBboxPatch((0.5, 4), 9, 2, 
                             boxstyle="round,pad=0.1", 
                             facecolor='#E2E3E5', edgecolor='#6C757D', linewidth=1)
    ax.add_patch(rec2_box)
    
    ax.text(0.8, 5.7, '2. 📊 Error Handling & Debugging', ha='left', va='center', 
            fontsize=11, fontweight='bold')
    ax.text(0.8, 5.3, '⏱️ ~1.5 hours | 🎯 Medium Priority', ha='left', va='center', fontsize=9)
    ax.text(0.8, 4.9, '"Essential skill for all developers"', ha='left', va='center', 
            fontsize=9, style='italic')
    
    start_btn2 = FancyBboxPatch((7, 4.3), 2, 0.6, 
                               boxstyle="round,pad=0.05", 
                               facecolor='#6C757D', edgecolor='#6C757D')
    ax.add_patch(start_btn2)
    ax.text(8, 4.6, 'Start Learning', ha='center', va='center', fontsize=9, color='white', fontweight='bold')
    
    # Quick Question
    question_box = FancyBboxPatch((0.5, 2.5), 9, 1, 
                                 boxstyle="round,pad=0.1", 
                                 facecolor='#E8F4FD', edgecolor='#007BFF', linewidth=1)
    ax.add_patch(question_box)
    ax.text(5, 3, '💡 "What should I learn next?"', ha='center', va='center', 
            fontsize=11, fontweight='bold', color='#007BFF')
    
    # Bottom Buttons
    bottom_buttons = ['View All Topics', 'Set Goals', 'Practice Exercises']
    for i, btn_text in enumerate(bottom_buttons):
        btn = FancyBboxPatch((0.5 + i*3.1, 1), 2.8, 0.8, 
                            boxstyle="round,pad=0.05", 
                            facecolor='#007BFF', edgecolor='#007BFF')
        ax.add_patch(btn)
        ax.text(1.9 + i*3.1, 1.4, btn_text, ha='center', va='center', 
                fontsize=9, color='white', fontweight='bold')
    
    plt.title('Learning Path Screen', fontsize=18, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('wireframe_learning_path.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Generate all wireframes"""
    print("🎨 Generating UI Wireframes...")
    
    try:
        print("📱 Creating Chat Interface wireframe...")
        create_chat_wireframe()
        
        print("🔧 Creating Code Assistance wireframe...")
        create_code_assistance_wireframe()
        
        print("📚 Creating Learning Path wireframe...")
        create_learning_path_wireframe()
        
        print("✅ All wireframes generated successfully!")
        print("📁 Files created:")
        print("   - wireframe_chat_interface.png")
        print("   - wireframe_code_assistance.png")
        print("   - wireframe_learning_path.png")
        
    except Exception as e:
        print(f"❌ Error generating wireframes: {e}")
        print("💡 Make sure matplotlib is installed: pip install matplotlib")

if __name__ == "__main__":
    main()