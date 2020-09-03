# AI_sub_projects
AI_sub_projects and Study 

### 1st 
모바일 / 압축 가속 / CartoonGan Test 

CartoonGan Test code

### 개발환경
- python 3.8.5
- torch 1.5.0
- torchvision 0.6.0
- cuda 10.1

### utils code 


### 논문 정리 
[Feature Pyramid Network](https://github.com/KangHoyong/AI_sub_projects/issues/1)


# Action Recognition / Human action classification & detection
#### GOAL : Slow Fast 논문 리뷰 및 구성 요소 이해 하기 

BackGround 

Activity Recognition은 기본적으로 3DCNN + Optical Flow로 구성된 아키텍처, CNN + LSTM로 구성된 아키텍처를 많이 사용한다. 

 - 3D ConvNet 
 
   1. 3D ConvNets 
   2. Two-Stream ConvNet 
   3. Two-Stream Inflated 3D ConvNet -> I3D (Two-Stram)
 
 - Non-local Neural Networks
 - video-long-term-feature-banks
 
#### 학습 방향

1. 3D ConvNet 을 중점으로 파악 하고 논문 리뷰 예정 
 - ConvNet + LSTM (CNN + LSTM) 
 - 3DCNN + Optical Flow 

2. [Non-local Neural Networks for Video Classification](https://github.com/facebookresearch/video-nonlocal-net)

- [논문 리뷰 영상](https://www.youtube.com/watch?v=ZM153wo3baA)

3. [Video-long-term-feature-banks](https://github.com/facebookresearch/video-long-term-feature-banks) 

- [Chao-Yuan Wu](https://www.cs.utexas.edu/~cywu/),
[Christoph Feichtenhofer](http://feichtenhofer.github.io/),
Haoqi Fan,
[Kaiming He](http://kaiminghe.com),
[Philipp Kr&auml;henb&uuml;hl](http://www.philkr.net/),
[Ross Girshick](http://rossgirshick.info)
In CVPR 2019.
[[Paper](https://arxiv.org/abs/1812.05038)]

4. SlowFast 사용되 알고리즘 파악 하고 리뷰 하기 

5. SlowFast 동작 어떤식으로 이루어지는가 대한 큰 그림 및 흐름 파악 하기 
 
#### Popular datasets

| Name  | Year  |  Number of classes |	#Clips |
| ----- | ----- | ----------------- | ------- |
| KTH   | 2004| 6| 600|   
|Weizmann|	2005|	9|	81|		
|HMDB-51| 2011|	51|	6.8k| 	 
|UCF-101|	2012|	101|	13.3k|
|Sports-1M|	2014|	487|	1M|
|ActivityNet|	2015|	200|	28.1k|
|Charades|	2016|	157|	66.5k from 9848 videos|
|Kinetics-400|	2017|	400|	306k|
|Something-Something|	2017|	174|	110k|
|Kinetics-600|	2018|	600|	496k|  
|AVA|	2018|	80|	1.6M from 430 videos|
|Youtube-8M Segments|	2019|	1000|	237k|
|IG-Kinetics|	2019|	359|	65M|

#### Popular publications

|                                                                                       | Year | UCF101 accuracy | HMDB51 accuracy | Kinetics accuracy | Pre-training on                                                              |
|---------------------------------------------------------------------------------------|------|-----------------|-----------------|-------------------|------------------------------------------------------------------------------|
| Learning Realistic Human Actions from Movies                                          | 2008 |                 |                 |                   | -                                                                            |
| Action Recognition with Improved Trajectories                                         | 2013 |                 | 57%             |                   | -                                                                            |
| 3D Convolutional Neural Networks for Action Recognition                               | 2013 |                 |                 |                   | -                                                                            |
| Two-Stream Convolutional Networks for Action Recognition in Videos                    | 2014 | 86%             | 58%             |                   | Combined UCF101 and HMDB51                                                   |
| Large-scale Video Classification with CNNs                                            | 2014 | 65%             |                 |                   | Sports-1M                                                                    |
| Beyond Short Snippets: Deep Networks for Video Classification                         | 2015 | 88%             |                 |                   | Sports-1M                                                                    |
| Learning Spatiotemporal Features with 3D Convolutional Networks                       | 2015 | 85%             |                 |                   | Sports-1M                                                                    |
| Initialization Strategies of Spatio-Temporal CNNs                                     | 2015 | 78%             |                 |                   | ImageNet                                                                     |
| Temporal Segment Networks: Towards Good Practices for Deep Action Recognition         | 2016 | 94%             | 69%             |                   | ImageNet                                                                     |
| Convolutional two-stream Network Fusion for Video Action Recognition                  | 2016 | 91%             | 58%             |                   | -                                                                            |
| [Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset](https://arxiv.org/abs/1705.07750)  **I3D model**               | 2017 | 98%             | 81%             | 74%               | Kinetics (+ImageNet)                                                         |
| Hidden Two-Stream Convolutional Networks for Action Recognition                       | 2017 | 97%             | 79%             |                   |                                                                              |
| Temporal 3D ConvNets: New Architecture and Transfer Learning for Video Classification | 2017 | 93%             | 64%             | 62%               | Kinetics (+ImageNet)                                                         |
| End-to-End Learning of Motion Representation for Video Understanding (TVNet)          | 2018 | 95%             | 71%             |                   | ImageNet                                                                     |
| ActionFlowNet: Learning Motion Representation for Action Recognition                  | 2018 | 84%             | 56%             |                   | Optical-flow dataset                                                         |
| [A Closer Look at Spatiotemporal Convolutions for Action Recognition](https://arxiv.org/abs/1711.11248)  **R(2+1)D model**                | 2018 | 97%             | 79%             | 74%               | Kinetics                                                                     |
| Rethinking Spatiotemporal Feature Learning For Video Understanding,                   | 2018 | 97%             | 76%             | 77%               |                                                                              |
| Can Spatiotemporal 3D CNNs Retrace the History of 2D CNNs and ImageNet?               | 2018 |                 |                 |                   |                                                                              |
| [Large-scale weakly-supervised pre-training for video action recognition](https://arxiv.org/abs/1905.00561)  **R(2+1)D model**          | 2019 |                 |                 | 81%               | 65 million automatically labeled web-videos (not publicly available) |
| Representation Flow for Action Recognition                                            | 2019 |                 | 81%             | 78%               | Kinetics                                                                     |
| Dance with Flow: Two-in-One Stream Action Recognition                                 | 2019 | 92%             |                 |                   | ImageNet                                                                     |

 
