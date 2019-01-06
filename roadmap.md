# Roadmap
For bugs and other issues see the repository issues on GitHub.

## General Improvements
- Load training data from a file instead of storing it in memory to allow for quick resume of training without needing to regenerate the dataset from the source corpus.

- Read training data from a file in chunks to allow for datasets beyond the size of available RAM.

- Output attention alignments correctly in tensorboard summary logs.
