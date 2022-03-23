import torch
import zipfile
import torchaudio
from glob import glob

class SpeechToText:
  """
  Convert audio files to text using the Silero speech-to-text model
  """

  def __init__(self, text_files):
    self.text_files = text_files

  def convert(self):
    
    # Load Silero model 

    device = torch.device("cuda" if torch.cuda.is_available() else 'cpu')  

    silero_model, decoder, utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                          model='silero_stt',
                                          language='en', 
                                          device=device)  
    (read_batch, split_into_batches,
    read_audio, prepare_model_input) = utils  

    # Use the Log Minimum Mean Square Error algorithm to enhance audio quality 

    enhanced_audio = logmmse(np.array(self.test_files[0]), sample_rate, output_file=None, initial_noise=1, window_size=160, noise_threshold=0.15)

    # Use batch normalization to improve model performance

    batches = split_into_batches(enhanced_audio, batch_size=10)
    input = prepare_model_input(read_batch(batches[0]),
                            device=device)

    output = silero_model(input)

    return output
  
  def format_text(self, output):

    # Add punctuation and recapitilize characters in output from speech to text conversion

    silero_model, example_texts, languages, punct, apply_te = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                      model='silero_te')
    output_text = ''
    
    for example in output:
      print(decoder(example.cpu()));
      input_text = decoder(example.cpu())
      print(apply_te(input_text, lan='en'))
      output_text += apply_te(input_text, lan='en')
    
    print(output_text)

    return output_text

if __name__ == "main": 

    test_files = glob('ted_talk.wav')

    speech_to_text = SpeechToText(text_files)
    output = ruspeech_to_textn.convert() 
    output_text = speech_to_text.format_text()