from textnode import TextType, TextNode
from copy_static import copy_static_to_public

def main():
    print("hello world")
    
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    copy_static_to_public()
    print("Static files copied successfully!")

if __name__ == "__main__":
    main()
