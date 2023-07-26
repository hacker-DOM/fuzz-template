1. `> gh repo clone https://www.github.com/hacker-DOM/fuzz-template`

2. Copy `woke_tests`, `justfile` `pyproject.toml` into your own repository

```zsh
function doms_fuzz_template() {
    local path_to_template="$HOME/blablabla"

    # ===== COPY JUSTFILE =====
    \cp -i "$path_to_template/justfile" .

    # ===== COPY PYPROJECT.TOML =====
    \cp -i "$path_to_template/pyproject.toml" .

    # ===== COPY WOKE TESTS =====
    \cp -i -r "$path_to_template/woke_tests" .
}
```

3. Have fun!!!
