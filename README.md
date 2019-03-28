# NetworSimulation


Analyzing Packet Size, Packet Loss, and Playback Policy on a Network Simulation

Adjon Tahiraj
CS 176B, University of California - Santa Barbara

Abstract
In this study, I analyze the effect of network loss on the quality of audio files. The experimental design includes a program which simulates audio data transfer through a network with the ability to change the packet size, packet loss rate, and policy for playing unavailable packets. The methodology I used is composed of an analysis of the impact of packet size on audio quality for different loss rates, the impact of increased packet loss on the audio quality for different packet sizes, and the impact that different policies for playing unavailable packets on audio quality for different packet size and loss. Additionally, I performed this analysis on both music and voice audio. The results show that in order to receive the best audio quality, packet sizes of 500 to 800 frames (1000 to 1600 bytes) should be used in network audio transmission. Additionally, the best policy to use for unavailable packets is to replay the last packet or use an extended sample from the end of the last received packet. Lastly, as the packet loss increases over 10% the audio quality starts to diminish, and as the packet loss reacher over 50% the audio quality is unintelligible. In conclusion for best audio quality, the study shows that packet length should be 1000 to 16000 bytes, packet loss should be less than 10%, and the policy for unavailable packets should be based on the last packet received. 

Read full report at: https://docs.google.com/document/d/14yOmgoRNZGZkSD2nFTYol314cG_4iuD3zMtum4HHui8/edit?usp=sharing
