import torch

class FormatText:
    def __init__(self) -> None:

        self._silero_model = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                        model='silero_te')

        self._example_texts = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                        model='silero_te')

        self._languages = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                        model='silero_te')
        
        self._punct = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                        model='silero_te')
        
        self._apply_te = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                                                        model='silero_te')
        
        self._decoder = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                          model='silero_stt',
                                          language='en', 
                                          device=device)
    
    def format(self, input_text : List[str], output) -> List[str]:
        output_text = ''

        for example in output:
            print(self._decoder(example.cpu()))
            input_text = self._decoder(example.cpu())
            print(self._apply_te(input_text, lan='en'))
            output_text += self._apply_te(input_text, lan='en')
      
        print(output_text)

        return output_text