from riwaz.base.constants import ALLOWED_NUMBER_REGEX_KEYS, ALLOWED_DISPLAY_NUMBER_REGEX_KEYS


class QueryRegex(object):

    @classmethod
    def _sanitize_regex(cls, search_word):
        return "".join([number for number in list(search_word) if number in ALLOWED_NUMBER_REGEX_KEYS])

    @classmethod
    def _get_query_match_key(cls, query_param):
        format_string = '{}'
        if query_param == 'start_with':
            format_string = '^{}'
        elif query_param == 'end_with':
            format_string = '{}$'
        return format_string

    @classmethod
    def get_qs_regex(cls, search_word, query_param='anywhere'):
        sanitized_number = cls._sanitize_regex(search_word)
        return cls._get_query_match_key(query_param).format(sanitized_number.replace("*", "."))


class NumberRegexService(object):

    SEARCH_NUMBER_MAPPING = {
        " ": "",
        "-": "",
        "O": "0",
        "o": "0",
        "*": "",
        "_": "",
    }

    DISPLAY_NUMBER_MAPPING = {
        "O": "0",
        "o": "0",
    }

    def sanitize_display_number(self, number_to_sanitize):
        for key in self.DISPLAY_NUMBER_MAPPING.keys():
            number_to_sanitize = number_to_sanitize.replace(key, self.DISPLAY_NUMBER_MAPPING[key])
        return "".join(
            [number for number in list(number_to_sanitize) if number in ALLOWED_DISPLAY_NUMBER_REGEX_KEYS]
        )

    def sanitize_number_to_search(self, number_to_sanitize):
        if number_to_sanitize:
            for key in self.SEARCH_NUMBER_MAPPING.keys():
                number_to_sanitize = number_to_sanitize.replace(key, self.SEARCH_NUMBER_MAPPING[key])
            return "".join([number for number in list(number_to_sanitize) if number in ALLOWED_NUMBER_REGEX_KEYS])
        else:
            return ""

    # @classmethod
    def sanitize_numbers(cls, numbers):
        return [cls.sanitize_number_to_search(number) for number in numbers]
