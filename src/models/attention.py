import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, emb_size, heads):
        super(MultiHeadAttention, self).__init__()
        self.heads = heads
        self.emb_size = emb_size
        self.head_dim = emb_size // heads  # Ensure emb_size is divisible by heads

        assert (self.head_dim * heads == emb_size), "Embedding size needs to be divisible by heads"

        self.values = nn.Linear(emb_size, emb_size, bias=False)
        self.keys = nn.Linear(emb_size, emb_size, bias=False)
        self.queries = nn.Linear(emb_size, emb_size, bias=False)
        self.fc_out = nn.Linear(emb_size, emb_size)

    def split_heads(self, x):
        b, n, _ = x.shape  # batch size, number of tokens, embedding size
        x = x.view(b, n, self.heads, self.head_dim)
        return x.permute(0, 2, 1, 3)  # (b, heads, n, head_dim)

    def forward(self, x):
        N = x.shape[0]  # number of input tokens
        value = self.split_heads(self.values(x))
        key = self.split_heads(self.keys(x))
        query = self.split_heads(self.queries(x))

        energy = torch.einsum("bhqd,bhkd->bhqk", [query, key])  # (b, heads, query_length, key_length)
        attention = F.softmax(energy / (self.head_dim ** (1 / 2)), dim=3)

        out = torch.einsum("bhqk,bhvd->bhqd", [attention, value])  # (b, heads, query_length, head_dim)
        out = out.permute(0, 2, 1, 3).contiguous()  # (b, query_length, heads, head_dim)
        out = out.view(N, -1)  # (b, emb_size)

        return self.fc_out(out)
