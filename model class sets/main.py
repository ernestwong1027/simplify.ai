from speechtotext import SpeechToText
from abstractivesummarization import Pegasus
from audioenhancement import audioenhancement
from pegasustrainer import PegasusTraining
from formattext import FormatText

if __name__ == "main":
    device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')

    audiofile = glob('CREATEPATHTOFILE')
    loaded_audio_enhancement = audioenhancement(audiofile)
    enhanced_audio = loaded_audio_enhancement.enhance()
    loaded_speech_to_text = SpeechToText(text_files=enhanced_audio)
    output_text = enhanced_audio.convert()
    loaded_formatted_text = FormatText(input_text=output_text, output='')
    final_text = loaded_formatted_text.format()
    loaded_summarization = Pegasus(final_text)
    summarized_text = loaded_summarization.summarize()

    return summarized_text