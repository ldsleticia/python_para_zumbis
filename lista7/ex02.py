# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
    result = ''
    for i in range(len(s)):
        result += s[:i+1]
    return result

print(string_splosion('Code'))