---
layout: post
title: AI Token Pricing 
subtitle: AI Token pricing in AWS 
comments: true
author: Kateryna M
---

# Amazon Bedrock On-Demand Pricing

## On-Demand Pricing

| Model                        | Price per 1000 Input Tokens            | Price per 1000 Output Tokens |
|------------------------------|----------------------------------------|------------------------------|
| Claude                       | $0.008                                 | $0.024                       |
| Claude Instant               | $0.0008                                | $0.0024                      |
| Command                      | $0.0015                                | $0.002                       |
| Command Light                | $0.0003                                | $0.0006                      |
| Embed – English              | $0.0001                                | N/A                          |
| Embed – Multilingual         | $0.0001                                | N/A                          |
| Jurassic-2 Mid               | $0.0125                                | $0.0125                      |
| Jurassic-2 Ultra             | $0.0188                                | $0.0188                      |
| Llama 2 Chat (13B)           | $0.00075                               | $0.001                       |
| Llama 2 Chat (70B)           | $0.00195                               | $0.00256                     |
| Titan Text Lite              | $0.0003                                | $0.0004                      |
| Titan Text Express           | $0.0008                                | $0.0016                      |
| Titan Embeddings             | $0.0001                                | N/A                          |
| Titan Multimodal Embeddings  | $0.0008 ($0.00006 per input image)     | N/A                          |

## Provisioned Throughput Pricing

| Model                                     | Price per Hour per Model Unit With No Commitment | Price per Hour per Model Unit With a One Month Commitment | Price per Hour per Model Unit With a Six Month Commitment |
|-------------------------------------------|--------------------------------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| Claude                                    | N/A                                              | $63.00                                                    | $35.00                                                    |
| Claude Instant                            | N/A                                              | $39.60                                                    | $22.00                                                    |
| Command                                   | N/A                                              | $39.60                                                    | $23.77                                                    |
| Command Light                             | N/A                                              | $6.85                                                     | $4.11                                                     |
| Llama 2 Pre-Trained and Chat (13B)         | N/A                                              | $21.18                                                    | $13.08                                                    |
| Llama 2 Pre-Trained (70B)                 | N/A                                              | $21.18                                                    | $13.08                                                    |
| SDXL1.0 (Stable Diffusion)                | N/A                                              | $49.86                                                    | $46.18                                                    |
| Titan Embeddings                          | N/A                                              | $6.40                                                     | $5.10                                                     |
| Titan Image Generator (Standard)          | N/A                                              | $16.20                                                    | $13.00                                                    |
| Titan Image Generator (Custom Models)     | $23.40                                           | $21.00                                                    | $16.85                                                    |
| Titan Multimodal Embeddings               | $9.38                                            | $8.45                                                     | $6.75                                                     |
| Titan Text Lite                           | $7.10                                            | $6.40                                                     | $5.10                                                     |
| Titan Text Express                        | $20.50                                           | $18.40                                                    | $14.80                                                    |

## Azure OpenAI Pay-As-You-Go Pricing

| Model             | Context | Price per 1000 Input Tokens | Price per 1000 Output Tokens |
|-------------------|---------|-----------------------------|-------------------------------|
| Ada               | N/A     | $0.0001                     | N/A                           |
| Babbage-002 (GPT Base) | N/A | $0.0004                     | $0.0004                       |
| Davinci-002 (GPT Base) | N/A | $0.002                      | $0.002                        |
| GPT-3.5 Turbo     | 4k      | $0.0015                     | $0.002                        |
| GPT-3.5 Turbo     | 16k     | $0.003                      | $0.004                        |
| GPT-4             | 8k      | $0.03                       | $0.06                         |
| GPT-4             | 32k     | $0.06                       | $0.12                         |

## Model Customization Pricing

| Model                  | Price for Training per Compute Hour | Price for Hosting per Hour |
|------------------------|-------------------------------------|----------------------------|
| Babbage-002 (GPT Base) | $34                                 | $1.70                      |
| Davinci-002 (GPT Base) | $68                                 | $3                         |
| GPT-3.5 Turbo          | $102                                | $7                         |
