from rasa.shared.nlu.training_data.formats import NLGMarkdownReader


def test_markdow_nlg_read_newlines():
    md = """
## Ask something
* faq/ask_something
  - Super answer in 2\\nlines
    """
    reader = NLGMarkdownReader()
    result = reader.reads(md)

    assert result.responses == {
        "faq/ask_something": [{"text": "Super answer in 2\nlines"}]
    }
