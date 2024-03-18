class Constants:
    MSG_TYPES = {
        # The device sends a request/response to us:
        0: 'query_response',
        1: 'report_response',  # ?
        2: 'change_response',

        # Sending a request to the device:
        4: 'query',
        5: 'report',  # ?
        6: 'write',
    }

    DATA_TYPES = {
        0: '0, but what does that mean?',
    }
