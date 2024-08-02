class Text:
    contents: str

    def __init__(self, content):
        self.content = content
    
    def __neg__(self):
        # Return a new Text object with reversed content
        reversed_content = ""
        for char in self.content:
            reversed_content = char + reversed_content
        return Text(reversed_content)  # Tests creating an object inside of a method
    
    def __str__(self):
        # Return the string representation of the Text object
        return self.content
    
    def __mul__(self, n):
        # Return a new Text object with content duplicated n times
        multiplied_content = self.content * n
        return Text(multiplied_content)


# Create a Text object
text: Text = Text("hello")

# Negate the text (reverse the content)
negated_text = -text
print(str(negated_text))  # Output: "olleh"

# Duplicate the text content
multiplied_text: Text = text * 3

print(str(multiplied_text))  # Output: "hellohellohello"


def concatenate_texts(text_list: list[Text]) -> Text:
    # Initialize an empty string to accumulate the concatenated content
    concatenated_content: str = ""
    
    # Iterate over the list of Text objects
    for text in text_list:
        # Add the content of each Text object to the concatenated_content
        concatenated_content += str(text)
    
    # Return a new Text object with the concatenated content
    return Text(concatenated_content)