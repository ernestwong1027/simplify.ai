import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

class Pegasus():
    """
    Leverages a pre-trained Pegasus Transformer to 
    conduct abstractive summarization on bodies of text.

    Original Model Paper: https://arxiv.org/pdf/1912.08777.pdf
    """

    def __init__(self, device : torch.device) -> None:
        """
        Loads the pre-trained Pegasus Transformer and the 
        associated tokenizer.

        Args:
            device: Device available for encoding (GPU or CPU).
        """
        # Define the encoder logger.
        self._logger = logging.getLogger("Pegasus Encoder Logger")

        # Define the device (gpu or cpu).
        self._device = device

        # Load the tokenizer and model associated with the Pegasus model.
        self._tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
        self._transformer = PegasusForConditionalGeneration.from_pretrained(
          "google/pegasus-xsum"
        ).to(self._device)

    def summarize(self, texts : List[str]) -> List[str]:
        """
        Summarizes a collection of texts and provides 
        the abstractive summarizations.

        Args:
          texts: List of texts to summarize.

        Returns:
          summarizations: List of summarized texts.
        """
        try:
          # Tokenize the batch for summarization.
          tokenized_batch = self._tokenizer(
              texts,
              truncation = True,
              padding = "longest",
              return_tensors = "pt",
              beam_length = 'longest'
          ).to(self._device)

          # Capture the summarized and encoded sequences.
          summarized_sequences = self._transformer.generate(**tokenized_batch)

          # Decode the output to get back the summarized texts.
          summarized_text = self._tokenizer.batch_decode(
              summarized_sequences,
              skip_special_tokens = True,
          )

          return summarized_text

        except Exception as summarization_exception:
            self._logger.error(
                "ERROR: Issue occured while attempting to summarize text."
            )
            raise summarization_exception