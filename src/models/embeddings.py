import torch
import torch.nn as nn

class LogTokenEmbedding(nn.Module):
    def __init__(self, vocab_size, embed_dim):
        super(LogTokenEmbedding, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)

    def forward(self, x):
        return self.embedding(x)