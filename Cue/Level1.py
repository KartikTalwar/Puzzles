
# Find the longest substring that is the same in reverse
def longestPalindrome(str):
    best = 0
    pos  = 0

    for i in range(1, len(str)):
        for lower, upper, curr in [(i - 1, i + 1, 1), (i, i + 1, 0)]:
            while lower >= 0 and upper < len(str) and str[lower] == str[upper]:
                lower -= 1
                upper += 1
                curr  += 2
            if (curr > best):
                best = curr
                pos  = lower + 1

    return str[pos:(pos + best)]


string  = 'Fourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceived'
string += 'inzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagr'
string += 'eahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongen'
string += 'dureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfield'
string += 'asafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltoget'
string += 'herfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecra'
string += 'tewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecratedi'
string += 'tfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhat'
string += 'wesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedher'
string += 'etotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforu'
string += 'stobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakein'
string += 'creaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehi'
string += 'ghlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewb'
string += 'irthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'

print longestPalindrome(string)

