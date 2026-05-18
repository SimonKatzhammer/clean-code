# Direct translation of the Java original from Clean Code (Ch. 2).
# Not refactored — kept as close to the source form as Python allows.

def printGuessStatistics(candidate: str, count: int):
    number: str
    verb: str
    pluralModifier: str
    if count == 0:
        number = "no"
        verb = "are"
        pluralModifier = "s"
    elif count == 1:
        number = "1"
        verb = "is"
        pluralModifier = ""
    else:
        number = str(count)
        verb = "are"
        pluralModifier = "s"
    guessMessage = "There %s %s %s%s" % (verb, number, candidate, pluralModifier)
    print(guessMessage)

# improved clarity
# german. plural for names makes no sense, but hey we practice :)
def printNumberOfNamesForGuessParticipants(candidateName: str, nameCount: int):
    if nameCount < 0:
        raise ValueError(f"nameCount must be >= 0, got {nameCount}")

    nameNumber: str
    verb: str
    pluralCharacter: str
    if nameCount <= 1:
        if nameCount == 0:
            nameNumber = "kein"
        else:
            nameNumber = "ein"
        verb = "ist"
        pluralCharacter = ""
    else:
        nameNumber = str(nameCount)
        verb = "sind"
        pluralCharacter = "s"
    outputMessage = "Da %s %s %s%s" % (verb, nameNumber, candidateName, pluralCharacter)
    print(outputMessage)