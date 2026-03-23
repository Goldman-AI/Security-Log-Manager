def tokenize_log_message(log_message):
    """Tokenizes a log message by splitting it into words and removing punctuation."""
    import string

    # Remove punctuation
    log_message = log_message.translate(str.maketrans('', '', string.punctuation))
    # Tokenize the message
    tokens = log_message.split()
    return tokens

# Example usage
if __name__ == '__main__':
    example_log = "Error: Disk space running low."
    print(tokenize_log_message(example_log))  
