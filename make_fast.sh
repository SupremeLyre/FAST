#!/usr/bin/env bash
set -euo pipefail

python3 -m venv venv
source venv/bin/activate

python3 -m pip install -U pip
python3 -m pip install -r fast/requirements.txt pyinstaller

add_fast_bin_files() {
  local -n args_ref=$1

  while IFS= read -r bin_file; do
    case "${bin_file,,}" in
      *.dll|*.exe)
        continue
        ;;
    esac

    if [[ -x "$bin_file" ]]; then
      args_ref+=(--add-binary "$bin_file:bin")
    else
      args_ref+=(--add-data "$bin_file:bin")
    fi
  done < <(find fast/bin -maxdepth 1 -type f | sort)
}

fast_args=(
  --clean
  --noconfirm
  --name FAST
  --console
  --contents-directory .
  _fast.py
)
add_fast_bin_files fast_args
python3 -m PyInstaller "${fast_args[@]}"

python3 -m PyInstaller --clean --noconfirm FastQt.spec
