#!/bin/bash

# Quick Reference for Interview Training Tools
# Save this as quick_commands.sh and run: chmod +x quick_commands.sh

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║           🎯 Interview Training Tool - Quick Reference         ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Function to display menu
show_menu() {
    echo "Choose an action:"
    echo ""
    echo "1.  🚀 Start Training Web App"
    echo "2.  📝 Convert New Transcript to JSON"
    echo "3.  📊 Analyze Interview Transcript"
    echo "4.  🔄 Compare Two Interviews"
    echo "5.  📈 Generate Progress Report"
    echo "6.  💪 Practice Mode (Web Interface)"
    echo "7.  📁 Create Folder Structure"
    echo "8.  💾 Backup Interview Data"
    echo "9.  📚 View Documentation"
    echo "10. ❌ Exit"
    echo ""
    read -p "Enter choice [1-10]: " choice
}

# Activate virtual environment
activate_venv() {
    if [ -d "venv" ]; then
        source venv/bin/activate
    else
        echo "⚠️  Virtual environment not found. Creating..."
        python3 -m venv venv
        source venv/bin/activate
        pip install flask flask-cors
    fi
}

# Actions
start_web_app() {
    echo "🚀 Starting Web Application..."
    activate_venv
    python training_api.py
}

convert_transcript() {
    echo "📝 Convert Transcript"
    read -p "Enter input file path: " input_file
    activate_venv
    python convert_transcript.py "$input_file"
}

analyze_transcript() {
    echo "📊 Analyze Interview"
    read -p "Enter transcript JSON file: " json_file
    activate_venv
    python analyze_transcript.py "$json_file"
}

compare_interviews() {
    echo "🔄 Compare Interviews"
    read -p "Enter first interview file: " file1
    read -p "Enter second interview file: " file2
    activate_venv
    python compare_interviews.py "$file1" "$file2"
}

progress_report() {
    echo "📈 Generate Progress Report"
    read -p "Enter directory with interview files [default: current]: " dir
    dir=${dir:-.}
    activate_venv
    python progress_report.py "$dir"
}

practice_mode() {
    echo "💪 Opening Practice Mode..."
    echo "Starting server at http://localhost:5000"
    activate_venv
    python training_api.py &
    sleep 2
    open http://localhost:5000 2>/dev/null || xdg-open http://localhost:5000 2>/dev/null || echo "Open http://localhost:5000 in your browser"
}

create_structure() {
    echo "📁 Creating Folder Structure..."
    mkdir -p transcripts
    mkdir -p analysis
    mkdir -p practice
    mkdir -p backups
    echo "✅ Created folders: transcripts/, analysis/, practice/, backups/"
}

backup_data() {
    echo "💾 Backing Up Interview Data..."
    timestamp=$(date +%Y%m%d_%H%M%S)
    tar -czf "backups/interview_backup_$timestamp.tar.gz" transcripts/ analysis/ *.json 2>/dev/null
    echo "✅ Backup created: backups/interview_backup_$timestamp.tar.gz"
}

view_docs() {
    echo "📚 Documentation Files:"
    echo ""
    echo "  • REUSE_GUIDE.md - Complete guide for future interviews"
    echo "  • WEB_API_README.md - Web API documentation"
    echo "  • README.md - Main project README"
    echo ""
    read -p "Which file to view? [1/2/3]: " doc_choice
    case $doc_choice in
        1) cat REUSE_GUIDE.md | less ;;
        2) cat WEB_API_README.md | less ;;
        3) cat README.md | less ;;
        *) echo "Invalid choice" ;;
    esac
}

# Main loop
while true; do
    show_menu
    case $choice in
        1) start_web_app ;;
        2) convert_transcript ;;
        3) analyze_transcript ;;
        4) compare_interviews ;;
        5) progress_report ;;
        6) practice_mode ;;
        7) create_structure ;;
        8) backup_data ;;
        9) view_docs ;;
        10) echo "👋 Goodbye! Good luck with your interviews!"; exit 0 ;;
        *) echo "❌ Invalid choice. Please try again." ;;
    esac
    echo ""
    read -p "Press Enter to continue..."
    clear
done
