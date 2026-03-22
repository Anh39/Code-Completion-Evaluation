PRE = "<|fim_prefix|>"
MID = "<|fim_middle|>"
SUF = "<|fim_suffix|>"
EOT = "<|endoftext|>"
def _split(prompt: str) -> tuple[str, str, str]:
    _, rest = prompt.split(PRE)
    prefix, rest = rest.split(SUF)
    suffix, middle = rest.split(MID)
    return (prefix, middle, suffix)
def _construct_prompt(prefix: str, middle: str, suffix: str) -> str:
    return PRE + prefix + SUF + suffix + MID + middle
def _construct_function_prompt(prefix: str, f_prefix: str, middle: str, f_suffix: str, suffix: str) -> str:
    return PRE + prefix + SUF + suffix + PRE + f_prefix + SUF + f_suffix + MID + middle
def _split_line(total: str, line_number: int) -> tuple[str, str, str]:
    lines = total.splitlines()
    previous_lines = lines[:line_number]
    current_line = lines[line_number]
    suffix_lines = lines[line_number+1:]
    return "\n".join(previous_lines) + "\n", current_line, "\n".join(suffix_lines) + "\n"
def _detect_function_prefix(prefix: str) -> int | None:
    lines = prefix.splitlines()
    for i in range(len(lines)-1, -1, -1):
        line = lines[i]
        if line.lstrip().startswith("def "):
            return i
    return None
def _detect_stop_suffix(suffix: str) -> int:
    lines = suffix.splitlines()
    marks = ["@", "class ", "def "]
    for i in range(len(lines)):
        line = lines[i]
        if any([line.lstrip().startswith(mark) for mark in marks]):
            return i
    return len(lines)
def function_cache(prompt: str) -> str:
    prompt = prompt.replace("\r\n", "\n")
    # with open("log/original.py", 'w', encoding='utf-8') as file:
    #     file.write(prompt)
    preffix, middle, suffix = _split(prompt)
    
    total = preffix + middle + suffix
    lines = total.splitlines()
    position = len(preffix)
    line_number = len(preffix.splitlines()) - 1
    function_line = _detect_function_prefix(preffix) or 0
    end_line = _detect_stop_suffix(suffix) + len(preffix.splitlines()) - 1
    
    previous_lines = lines[:function_line]
    previous_in_function_lines = lines[function_line:line_number]
    current_line = lines[line_number]
    suffix_in_function_lines = lines[line_number+1:end_line]
    suffix_lines = lines[end_line:]
    
    result = _construct_function_prompt(
        "\n".join(previous_lines) + "\n",
        "\n".join(previous_in_function_lines) + "\n",
        current_line,
        "\n".join(suffix_in_function_lines) + "\n",
        "\n".join(suffix_lines) + "\n"
    )
    with open("outputX.py", 'w', encoding='utf-8') as file:
        file.write(result)
    return result