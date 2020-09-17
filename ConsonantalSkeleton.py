# -*- coding: utf-8 -*-
# ConsonantalSkeleton.py

child_form = 'test'

def get_consonantal_skeleton():
    vowels = 'aeoɑui'
    consonantal_skeleton = ''.join('_' if ch in vowels else ch for ch in child_form )
    return consonantal_skeleton

print(get_consonantal_skeleton())
