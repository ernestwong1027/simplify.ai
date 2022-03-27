import torch
import zipfile
import torchaudio
from glob import glob


class SpeechToText:
 """
  Convert audio files to text using the Silero speech-to-text model
 """
  def __init__(self, device : torch.device) -> None:
    # loading device for gpu acceleration

    self._device = device
    
    self._silero_model = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                          model='silero_stt',
                                          language='en', 
                                          device=device)  

    self._decoder = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                          model='silero_stt',
                                          language='en', 
                                          device=device)  

    self._utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                          model='silero_stt',
                                          language='en', 
                                          device=device)
    
  def convert(self, audio_file : List[str]) -> List[str]:

      self._utils = (read_batch, split_into_batches, read_audio, prepare_mode_input)

      batches = split_into_batches(audio_file, batch_size=10)

      input = prepare_mode_input(read_batch(batches[0]), device=self._device)

      output = self._silero_model(input)

      return output

   def format_text(self, output):

      # Add punctuation and recapitilize characters in output from speech to text conversion

      silero_model, example_texts, languages, punct, apply_te = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                        model='silero_te')
      output_text = ''
      
      for example in output:
        print(decoder(example.cpu()))
        input_text = decoder(example.cpu())
        print(apply_te(input_text, lan='en'))
        output_text += apply_te(input_text, lan='en')
      
      print(output_text)

      return output_text