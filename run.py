import fetch_data
from markov_python.cc_markov import MarkovChain

print "Welcom to MarkovChain"
url=raw_input("Provide an URL:")
text1=fetch_data.getURL(url)
mc=MarkovChain()
mc.add_string(text1)
output=mc.generate_text()
print output
