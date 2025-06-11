#!/bin/bash

run_browser=false

while getopts "r" opt; do
  [[ $opt == "r" ]] && run_browser=true
done

set -e

release_folder=$(find ~/.zen -maxdepth 1 -type d -name "*(*release*)*" | head -n1)
release_folder=${release_folder:-$(find ~/.zen -maxdepth 1 -type d -name "*(*alpha*)*" | head -n1)}

if [[ -z "$release_folder" ]]; then
  echo "No (release) or (alpha) folder found in ~/.zen"
  exit 1
fi

chrome_dir="$release_folder/chrome"
zenbash_dir="$chrome_dir/ZenBash"
mkdir -p "$zenbash_dir"

content_path="$HOME/.config/hyde/wallbash/Wall-Ways/zen#Content.dcol"
content_entry="'${zenbash_dir}/zenbashContent.css'"
tmp_content=$(mktemp)

if [[ -f "$content_path" ]]; then
  read -r line < "$content_path"
  [[ "$line" != *"@media {"* ]] && tail -n +2 "$content_path" > "$tmp_content" || cp "$content_path" "$tmp_content"
fi

echo "$content_entry" > "$content_path"
cat "$tmp_content" >> "$content_path"
rm "$tmp_content"

chrome_path="$HOME/.config/hyde/wallbash/Wall-Ways/zen#Chrome.dcol"
chrome_entry="'${zenbash_dir}/zenbashChrome.css'|$HOME/.local/share/bin/ZenBash.sh -r"
tmp_chrome=$(mktemp)

if [[ -f "$chrome_path" ]]; then
  read -r line < "$chrome_path"
  [[ "$line" != *"@media {"* ]] && tail -n +2 "$chrome_path" > "$tmp_chrome" || cp "$chrome_path" "$tmp_chrome"
fi

echo "$chrome_entry" > "$chrome_path"
cat "$tmp_chrome" >> "$chrome_path"
rm "$tmp_chrome"

user_chrome="$chrome_dir/userChrome.css"
import_chrome='@import "ZenBash/zenbashChrome.css";'
touch "$user_chrome"
if ! grep -Fxq "$import_chrome" "$user_chrome"; then
  tmp=$(mktemp)
  echo "$import_chrome" > "$tmp"
  cat "$user_chrome" >> "$tmp"
  mv "$tmp" "$user_chrome"
fi

user_content="$chrome_dir/userContent.css"
import_content='@import "ZenBash/zenbashContent.css";'
touch "$user_content"
if ! grep -Fxq "$import_content" "$user_content"; then
  tmp=$(mktemp)
  echo "$import_content" > "$tmp"
  cat "$user_content" >> "$tmp"
  mv "$tmp" "$user_content"
fi

if $run_browser; then
  # Detect existing Zen window
  zen_id=$(hyprctl clients -j | jq -r '.[] | select(.class | test("zen")) | .address' | head -n1)
  workspace=""
  if [[ -n "$zen_id" ]]; then
    workspace=$(hyprctl clients -j | jq -r --arg addr "$zen_id" '.[] | select(.address == $addr) | .workspace.id')

    echo "[ZenBash] Restarting zen-browser..."

    pkill -f '[z]en'
    zen-browser & disown

    for _ in {1..10}; do
      sleep 0.5
      new_zen=$(hyprctl clients -j | jq -r '.[] | select(.class | test("zen")) | .address' | head -n1)
      [[ -n "$new_zen" ]] && break
    done

    if [[ -n "$new_zen" && -n "$workspace" ]]; then
      hyprctl dispatch movetoworkspacesilent "$workspace,address:$new_zen"
    fi
  else
    echo "[ZenBash] No existing Zen window found — skipping restart."
  fi
fi