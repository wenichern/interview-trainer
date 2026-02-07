# 📋 Quick Reference Card - Interview Training Tools

## 🚀 Daily Commands

```bash
# Start training web app
./start_server.sh
# Then visit: http://localhost:5000

# Or use interactive menu
./quick_commands.sh
```

## 📝 After Each Interview

```bash
# 1. Convert transcript
python convert_transcript.py my_interview.txt

# 2. Analyze it
python analyze_transcript.py my_interview.json

# 3. Compare with previous
python compare_interviews.py old_interview.json my_interview.json
```

## 📊 Weekly Review

```bash
# Generate progress report
python progress_report.py transcripts/

# Backup your data
tar -czf backup_$(date +%Y%m%d).tar.gz transcripts/ analysis/
```

## 🎯 Before Next Interview

1. ✅ Review last interview analysis
2. ✅ Start web app: `./start_server.sh`
3. ✅ Complete weak-area training modules
4. ✅ Practice 10 questions
5. ✅ Check progress: `python progress_report.py`

## 📁 Recommended Structure

```
interview-training/
├── transcripts/          # All interview JSON files
│   ├── 2026-02-07-company1.json
│   ├── 2026-02-15-company2.json
│   └── 2026-03-01-company3.json
├── analysis/             # Analysis reports
├── practice/             # Custom practice questions
└── backups/              # Regular backups
```

## 🔗 Web Interface

**URL:** http://localhost:5000

**Features:**
- 📚 Training Modules (4 modules)
- 💪 Practice Mode (with instant feedback)
- 💡 Quick Tips

## 🎓 Success Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Overall Score | 8.5+/10 | Check latest |
| Weak Phrases | 0 | Count in practice |
| Response Time | 60-90s | Track in practice |
| STAR Method | 80%+ | Review transcripts |

## 💡 Quick Tips

1. **Before Interview:**
   - Prepare 7 STAR stories
   - Practice concise answers
   - Review company-specific questions

2. **After Interview:**
   - Get transcript within 24 hours
   - Analyze immediately
   - Note improvements needed

3. **Weekly Practice:**
   - Use web app 3x/week
   - Practice 15-20 min daily
   - Review progress monthly

## 🆘 Troubleshooting

```bash
# Port busy?
# Edit training_api.py line 658: change port to 5001

# Virtual environment issues?
rm -rf venv && python3 -m venv venv
source venv/bin/activate
pip install flask flask-cors

# Can't find files?
python progress_report.py ./  # Search current dir
```

## 📞 File Locations

| File | Purpose |
|------|---------|
| `training_api.py` | Web server |
| `convert_transcript.py` | Convert transcripts |
| `analyze_transcript.py` | Analyze interviews |
| `compare_interviews.py` | Compare progress |
| `progress_report.py` | View trends |
| `quick_commands.sh` | Interactive menu |

## 🎯 One-Line Commands

```bash
# New interview workflow (all in one)
python convert_transcript.py new.txt && \
python analyze_transcript.py new_converted.json && \
python compare_interviews.py last.json new_converted.json

# Weekly review
python progress_report.py transcripts/ && \
tar -czf backup_$(date +%Y%m%d).tar.gz transcripts/

# Practice session
./start_server.sh  # Then go to localhost:5000
```

---

**💾 Save this file:** Print or bookmark for easy reference!

**🔖 Pro Tip:** Run `./quick_commands.sh` for an interactive menu of all commands.
