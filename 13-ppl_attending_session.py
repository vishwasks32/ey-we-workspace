#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwas@cloudthat.com

# Assume you have got two list of ids of people attending 2 sessions
# Find out who attended both sessions

# session_a = [101,103,102,101,108,109]
# session_b = [101,103,107,110,105,102]

session_a = [101,103,102,101,108,109]
session_b = [101,103,107,110,105,102]
both_sessions = list(set(session_a).intersection(set(session_b)))
print(both_sessions)