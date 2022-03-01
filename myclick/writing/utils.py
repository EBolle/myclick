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


def _paragraph_words(text: str) -> list:
    """
    Returns a list of list with words per paragraph in the HTMl raw text.
    """
    p_pattern = re.compile(r'(<p\s+.*?>)\s+(.*?)</p>', flags=re.IGNORECASE|re.DOTALL)
    p_lists = []

    for match in re.finditer(p_pattern, text):
        temp_list = match.group(2).split(" ")
        no_empty_string_list = [word for word in temp_list if word] 
        p_lists.append(no_empty_string_list)

    return p_lists    


def _clean_text(text: str) -> str:
    """
    Removes all but the paragraph tags and the actual content in the HTML raw text.
    """
    tag_stripped_text = re.sub(r'</?\s*(a|br|em|strong|sup).*?>', '', text, flags=re.IGNORECASE|re.DOTALL)
    clean_text = re.sub(r'(\n|[.,!])', '', tag_stripped_text, flags=re.IGNORECASE|re.DOTALL)

    return clean_text