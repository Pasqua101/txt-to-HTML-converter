import argparse
import tomllib

from . import file_processors as fp

VERSION = "1.0"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert a text or markdown file to an HTML file.",
        epilog="Example: python txt_to_html.py input.txt or python txt_to_html.py ./folder",
    )

    parser.add_argument(
        "--version", "-v", action="version", version=f"%(prog)s {VERSION}"
    )

    parser.add_argument("input_path", help="Path to the input file or directory")

    # Optional argument to use the stylesheet feature
    parser.add_argument(
        "--stylesheet",
        "-s",
        metavar="<CSS stylesheet URL>",
        help="Use if you want to add a stylesheet to the generated HTML file",
    )

    # Optional argument to use the output directory feature
    parser.add_argument(
        "--output",
        "-o",
        metavar="<output_folder>",
        help="Use if you want to change the destined output of the HTML files. Otherwise it will be sent to the til "
        "folder",
    )

    # Optional argument to modify the lang attribute
    parser.add_argument(
        "--lang",
        "-l",
        metavar="<lang attribute>",
        help="Use if you want to indicate what language the input file "
        "is using for the HTML doc that will be generated",
    )

    # Optional argument to utilize TOML config files for the stylesheet, output, and lang attribute
    parser.add_argument(
        "--config",
        "-c",
        metavar="<config.toml>",
        help="Use if you want to use a TOML config file to set the stylesheet, output, and lang attribute.",
    )

    # Optional argument to utilize sidebar creation for large websites
    parser.add_argument(
        "--sidebar",
        "-sb",
        metavar="<sidebar.py>",
        help="Use if you want to create a table of contents/sidebar for your website to use.",
    )

    args = parser.parse_args()

    input_path = args.input_path

    if args.config:
        with open(args.config, "rb") as f:
            try:
                config = tomllib.load(f)
            except (
                tomllib.TOMLDecodeError
            ) as e:  # If the TOML file is not formatted correctly, it will exit the program
                print(f"Error decoding TOML file: {e}")
                exit(-1)
            try:
                stylesheet = (
                    config["stylesheet"]
                    or "https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"
                )
                output_dir = config["output"] or "./til"
                lang = config["lang"] or "en-CA"
                sidebar = config["sidebar"]
            except (
                KeyError
            ) as e:  # If any of the keys are not found in the TOML file, it will exit the program
                print(f"Error: {e} not found in TOML file.")
                exit(-1)
            fp.text_to_html(input_path, stylesheet, output_dir, lang, sidebar)

    else:
        stylesheet = (
            args.stylesheet or "https://cdn.jsdelivr.net/npm/water.css@2/out/water.css"
        )
        output_dir = (
            args.output or "./til"
        )  # If the user does not enter an output directory, it will assign the directory til
        lang = args.lang or "en-CA"
        sidebar = args.sidebar
        fp.text_to_html(input_path, stylesheet, output_dir, lang, sidebar)
