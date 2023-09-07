"""This string was found on the URL https://www.coursera.org/learn/prepare-for-cybersecurity-jobs/supplement/Nxxci/claim-your-google-cybersecurity-certificate-badge after I finished the course."""

bitstring = "01100110 01101001 01101110 01100100 00101110 01100110 01101111 01101111 \
             00101111 00110010 00110000 00110010 00110011 01000111 01101111 01101111 \
             01100111 01101100 01100101 01000011 01100101 01110010 01110100 01110011"

bytes = bitstring.split()
values = [int(b,2) for b in bytes]
letters = [chr(v) for v in values]
message = "".join(letters)

print(message)

# The message is the url "find.foo/2023GoogleCerts"