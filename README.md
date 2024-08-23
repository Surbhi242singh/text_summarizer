# Text Summarization with spaCy

## Project Overview

This project focuses on generating a summary of a given text using Natural Language Processing (NLP) techniques with spaCy. The approach involves tokenizing the text, calculating word frequencies, scoring sentences based on word frequencies, and selecting the most important sentences to create a concise summary.

## Methodology

**Word Tokenization:**
   - The text is divided into individual words (tokens) using spaCy's NLP pipeline.

**Word Frequency Calculation:**
   - Stop words and punctuation are excluded, and the frequency of each word in the text is calculated.

**Sentence Tokenization:**
   - The text is split into sentences.

**Sentence Scoring:**
   - Each sentence is scored based on the cumulative frequency of the words it contains.

**Summary Generation:**
   - The top 30% of sentences with the highest scores are selected to form the summary.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
