# Ferra for Kakoune
This is a port of Ferra for [Kakoune](https://github.com/mawww/kakoune)
## Installing via [plug.kak](https://github.com/andreyorst/plug.kak)
Add the following to your config file, it's best to ensure no other
theme is loaded simultaneously.
```kak
plug "casperstorm/ferra" theme config %{
	colorscheme ferra
}
```
## Installing manually
To install this theme without a plugin manager, copy the `ferra.kak` file
into your config's `color` directory.
```sh
mkdir -p ~/.config/kak/colors
cd ~/.config/kak/colors
curl -O "https://raw.githubusercontent.com/casperstorm/ferra/main/ports/kakoune/ferra.kak"
```
