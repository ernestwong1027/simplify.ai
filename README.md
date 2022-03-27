## What is simplify.ai?

A free, open-source web app that takes in lecture recordings as inputs and outputs their summaries. Simply drag and drop your audio file or find it from your computer, and your summary will generate in less than two minutes.

## How we built it

Our pipeline is in `\model class sets`. We built it using natural language processing models, specifically the Silero speech-to-text model and the Pegasus abstractive summarization model, and added additional scripts to add punctionuation, enhance audio quality, and finetune our summarization model.

## What we learned

- Abstractive summarization ([Attention is all you need!](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf))
- The differences between Automatic Speech Recognition and Speech To Text models 
- Creating machine learning pipelines and transforming them into products

## What's next

- Explore pricing plans + enterprise usage
- Adding a sentiment analysis feature to rate lecture quality in terms of engagement, tone, and impact
- Allowing users to create accounts to access previous lecture summaries in one place
- Building a dataset with inputted audio files, potentially separating it by professor
