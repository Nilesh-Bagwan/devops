# devops

This repository contains Python practice scripts for DevOps assignments.

## Available scripts

- `python-programs/grade_checker.py`: Enter a score (0-100) and receive a grade (A-F).
- `python-programs/file_reader.py`: Reads and prints the contents of `my_notes.txt`.
- `python-programs/file_writer.py`: Writes sample text to `my_notes.txt`.
- `python-programs/student_grades.py`: Interactive student grade manager (add/update/view students).

## How to run each script

### grade_checker.py

1. Open terminal in repository root.
2. Run:
   - `python3 python-programs/grade_checker.py`
3. Enter score when prompted:
   - `Enter your score (0-100):`
4. Expected output example:
   - `Score: 85 | Grade: B`

### file_writer.py

1. Run:
   - `python3 python-programs/file_writer.py`
2. Script creates/overwrites `python-programs/my_notes.txt` with sample text.
3. Output:
   - `Success: Content written to 'my_notes.txt'`

### file_reader.py

1. Ensure `python-programs/my_notes.txt` exists (created by file_writer or manually).
2. Run:
   - `python3 python-programs/file_reader.py`
3. Output prints the contents of `my_notes.txt`, or FileNotFound error if missing.

### student_grades.py

1. Run:
   - `python3 python-programs/student_grades.py`
2. Follow menu prompts:
   - Add student/grade
   - Update existing grade
   - View all entries
   - Exit

## Notes

- `grade_checker.py` requires integer input from 0 to 100; non-integer input gives `Invalid input! Please enter a whole number.`
- `file_writer.py` overwrites `my_notes.txt`.
- `student_grades.py` stores data only in-memory during runtime (not persisted).