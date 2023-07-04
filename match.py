#practicing match
htmlError = 200

match htmlError:
    case 200 | 201:
        print('success')
    case 300:
        print('wierd')
    case 404:
        print('cannot be found')
    case _:
        print('unknown')