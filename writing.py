"""This module contains all the (helper) functions to improve your writing, which we assume is tight."""

import re


def _newline_locator(text: str, match_start_list: list) -> list:    
    """
    Locates the line number based on the indices of the matched substrings
    in your regular expression (match.start()).
    """
    text_list = list(text)
    match_start_list_copy = match_start_list.copy()
    max_idx = max(match_start_list_copy)
    
    newline_tracker = 0
    newline_list = []
    
    for idx, char in enumerate(text_list[:max_idx+1]):
        if char == '\n':
            newline_tracker += 1

        if idx == match_start_list_copy[0]:
            newline_list.append(newline_tracker)
            match_start_list_copy.pop(0)
            
    return newline_list


def _paragraph_counter(re_pattern, text: str) -> list:
    """
    Returns a list with counts per paragraph in a the HTMl raw text.
    """
    p_lists = []

    for match in re.finditer(re_pattern, text):
        temp_list = match.group(2).split(" ")
        no_empty_string_list = [word for word in temp_list if word] 
        p_lists.append(no_empty_string_list)

    return {idx: len(p_list) for idx, p_list in enumerate(p_lists, start=1)}