# Ferra for Ghostty

- Make Ghostty config file if needed
  - If $XDG_DESKTOP_HOME is set
    - `mkdir -p $XDG_DESKTOP_HOME/ghostty/`
    - `touch $XDG_DESKTOP_HOME/ghostty/config`
  - otherwise
    - `mkdir -p $HOME/.config/ghostty/`
    - `touch $HOME/.config/ghostty/config`
- Make Ghostty theme directory if needed
  - If $XDG_DESKTOP_HOME is set
    - `mkdir -p $XDG_DESKTOP_HOME/ghostty/themes/`
  - otherwise
    - `mkdir -p $HOME/.config/ghostty/themes/`
- Download `ferra` into your Ghostty theme directory
- Add the following to your Ghostty config file

```
theme = ferra
```
