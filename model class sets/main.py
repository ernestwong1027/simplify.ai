from speechtotext import SpeechToText
from abstractivesummarization import Pegasus
from pegasustrainer import PegasusTraining

device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')

audiofile = 'CREATEPATHTOFILE'
output_text = SpeechToText(text_files=audiofile)
summarization = Pegasus(texts=output_text)

return summarization