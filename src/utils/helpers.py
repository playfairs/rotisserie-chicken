def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def lerp(start, end, t):
    return start + (end - start) * t

def mapRange(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def formatPercent(value):
    return f"{int(value)}%"

def formatTime(ticks):
    mins = ticks // 600
    secs = (ticks % 600) // 10
    return f"{mins}:{secs:02d}"

def easeInQuad(t):
    return t * t

def easeOutQuad(t):
    return 1 - (1 - t) * (1 - t)
