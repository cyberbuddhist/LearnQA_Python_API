class TestExample:
    def test_check_length(self):
        phrase = input("Set a phrase: ")
        self.expected_result = len(phrase)
        assert self.expected_result <= 15, "The length of phrase is more than 15 symbols"