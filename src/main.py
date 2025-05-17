from textnode import TextNode, TextType

def main():
    sample = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(f"TextNode({sample.text},{sample.text_type.value},{sample.url})")

main()
