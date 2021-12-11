import torch
import torch.nn as nn

class RiemannNoise(nn.Module):
    def __init__(self, size, device):
        super(RiemannNoise, self).__init__()
        '''
        Initializes the module, taking 'size' as input for defining the matrix param.
        '''
        self.device = device
        if type(size) == int:
            h = w = size
        elif type(size) == tuple and (type(x)==int for x in size):
            h = size[-2]
            w = size[-1]
        else:
            raise ValueError("Module must be initialized with a valid int or tuple of ints indicating the input dimensions.")
        self.A = nn.Parameter(torch.rand(1,h,w))
        self.b = nn.Parameter(torch.rand(1,))
        self.alpha = nn.Parameter(torch.rand(1,))
        self.r = nn.Parameter(torch.rand(1,))

    def forward(self, x):
        N, c, h, w = x.shape
        mu = x.sum(1, keepdim=True)
        mu_mean = mu.sum(dim=(2,3),keepdim=True)*(1/h*w)
        s = mu - mu_mean
        s = s / torch.abs(s).max()
        sd = self.A * s + self.b
        s = self.alpha*sd + (1 - self.alpha) + 1
        sigma = s / torch.linalg.vector_norm(s)
        out = self.r * sigma * x + self.r * sigma * torch.normal(torch.zeros(x.shape),torch.ones(x.shape)).to(self.device)
        return out