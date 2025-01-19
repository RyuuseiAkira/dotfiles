import cssutils

def extract_bar_bg(css_file):
    sheet = cssutils.parseFile(css_file)
    for rule in sheet:
        print(f"Rule name: {rule.name}")  # Added print statement
        if rule.type == rule.STYLE_RULE and rule.name == 'bar-bg':  # Update the rule name if needed
            return rule.style['color'].value
    return None

css_file = '/home/akira/.config/waybar/theme.css'
bar_bg_color = extract_bar_bg(css_file)
print(bar_bg_color)