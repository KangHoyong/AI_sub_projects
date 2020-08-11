### A Survey on Moving Object Detection and Tracking Methods (2014)

위의 논문은 Tracking 방법이나 Detection 방법에 대해 간단한 소개와, 
기술들을 설명 하고 있습니다.

object Tracking program 을 완성시키기 위해 Object Detection and Tracking 방법에 대한 Survey 논문 정리

### Introduction 
객체를 탐지하는데 있어서 가장 먼저 이루어저야 하는것은 The identification of rangions of interset (관심 영역을 인식)

객체 인식을 하는데 잘알려진 알고리즘을 이용하여 Detect하는 것이 좋은 방법이다 하지만 잘모르는 객체나 색상 크기 .. 등 다양한 변수가 존재하기 때문에 Detection 하는 과정은 어려울 수 밖에 없다. 

From a video sequence, an image is divided into two complimentary sets of pixels (비디오로 부터 받는 2가지 스탭 픽셀 정보)

1. 전경객체(Foreground object) : 사람 자동차 고양이 같은 물체를 움직이는 전경 물체에 해당하는 픽셀 

2. 배경객체(Background pixel) : 배경 객체에 대한 픽셀 정보 

처리된 이미지 결과는 Binary Image 나 Mask 형태로 나타나게 된다.


### Tracking Base Step 
<img width="417" alt="스크린샷 2020-08-10 오전 10 13 55" src="https://user-images.githubusercontent.com/9815703/89745995-35562400-daf2-11ea-9373-e26d0365f8ff.png">

1. Object Detection 
     - cluster pixelse and video sequence 에서 관심있는 영역을 식별하는 과정이다. 

2. Object Classification 
    - Objecct 는 자동차, 새, 구름, 고양이, 강아지나 다른 움직이는 객체들로 분류될 수 있다. 이러한 객체를 분류하기 위한 Approaches 는 Shape-based classification, Motion-based classification, Color based classification and Texture based classification 등이 있다. 
    (2014년 논문 기준)

3. Object Tracking 
    - Tracking 은 움지깅는 장면에서 이미지면에 있는 물체의 path 근사치 구하는 문제라고 할 수 있다.
    즉 영상에서 관심있는 물체가 움직이는 path가 얼마나 그 전 프레임과 유사한지 알아낸 다음 동일 객체라고 인식하게 되면, 그 물체를 계속 
    Tracking 하는 것이라고 할 수 있다. 
    객체 Tracking 하는 방법에는 Point Tracking, Kernel Tracking, Silhouette 등이 있다 (2014년 논문 기준)

Tracking 주의사항 

1. Loss of evidnce caused by estimate of the 3D realm on a 2D image 
(2D 영상의 3D영역 추정으로 인한 손실)

2. Nose in an image (노이즈 문제)

3. Difficult object motion (어려운 동작)

4. Imperfect and entire object occlusions (물체 인클로저 손상 및 활성화)

5. Complex objects structures (복합물체 구조)

### Tracking base Step 
<img width="346" alt="스크린샷 2020-08-10 오전 10 33 32" src="https://user-images.githubusercontent.com/9815703/89746521-05f4e680-daf5-11ea-89aa-c118906bb791.png">

### Object Detection Methods
Object Tracking 을 위한 첫번째 과정은 Video Sequence에서 관심있는 
객체를 식별하는 것이다. 이러한 과정을 수행하기 위한 방법은 3가지 정도 있다.(논문 기준)

1. Frame differencing 
두개의 연속되는 이미지 사이의 차이를 계산함으로써 움직이는 객체의 존재 파악 
즉 시간 차이 t(시간변수로 계산) Background 제거 forground pixels 을 Threshold 하여 subtraction(차이 뺼샘)을 통하여 이미지를 개선 

empty phenomenon (비어있는 현상)이 있을때 적용하기 좋은 알고리즘 
하지만 움직이는 객책의 OutLine을 얻기는 매우 어렵다.


2. Optical Flow 
광학 흐름 또는 광학 흐름은 관찰자와 장면 사이의 상대적인 움직임으로 인해 시각적 장면에서 물체, 표면 및 가장자리의 명백한 움직임의 패턴입니다. (위키백과) 

ex) 만약 하늘위에 떠있는 경우에는 회전하는 관잘자를 통해 개념을 설명 할 수 있는데, 각 위치에서 나타난 Direction 과 Magnitude 각 화살의 길이와 방향에 의해 나타난다. 단순한 영상에서 모션 백터를 찾는 방법 

단점 : 계산량이 많음.. Noise에 민감 Real-time 환경에서 적용하기에 알맞지 않은 알고리즘 

3. Background Subtraction
1 step : Background Modelling 배경 추출 알고리즘의 핵심은 배경 모델링이 움직이는 객체를 충분히 인식해야 한다는 점이다. 

배경 모델링을 하는데 좋은 방법은 두가지 정도 Mean Filter, Median Filter(2014년 논문기준)
배경 추출 방법은 현재 이미지와 움직이는 객체를 탐지하기 위한 배경 이미지의 차이를 이용하는 방법을 사용하게 된다. 그러나 주위 외부 환경 변화에 대해 매우 민감한 특징이 있다. 

but 이는 배경에 대한 정보를 알고 있는 경우 객체의 대한 정보를 완벽하게 얻을 수 있다. 배경 추출방법은 2가지 정도의 접근법이 존재 (2014년 논문기준)

1. Recursive Algorithm
2. Non-recursive Alogrithm

different method : Gaussian of Mixture(가우시안 혼합 모델), 
Approximate median, Adaptive background 

Gaussian of Mixture
Gaussian Mixture Model (GMM)은 이름 그대로 Gaussian 분포가 여러 개 혼합된 clustering 알고리즘이다 / 혼합 모델은 통계학에서 전체 집단안의 하위 집단의 존재를 나타내기 위한 확률 모델이다

Approximate median : 중간원소 찾는 방법 


### Object detection methods 비교 자료 
<img width="705" alt="스크린샷 2020-08-10 오전 11 20 39" src="https://user-images.githubusercontent.com/9815703/89747860-9afade00-dafb-11ea-85fd-5621df446bc8.png">
* 상황에 맞게 알고리즘 적용


### Background Subtraction Algorithm Based Human Motion Detection 논문 정리 

1. Object Classification Method :
사람과 자동차 동ㅇ물 떠나다니는 별 구름 같은 다양하고 서로 다른 물체를 추적하고, 객체를 추출하기 위해서는 다양한 Classification 알고리즘들이 있다. 위에 논문은 Shape Feature을 이용하여 영역에서 객체를 추출

    - Shape based classification 
    : point, box and blob 등과 같은 특징으로 shape는 이루어지게 된다. 이와 같은 정보는 움직이는 물체를 분류 식별 가능 

    - Motion based classification 
    : Optical flow는 물체를 분류하는 데 있어서 유용하게 사용될 수 있다. Residual flow 잔류운동 은 움직이는 객체가 유연하게 다른 프레임과 연결되는 분석하는데 유용하게 사용 될 수 있다. 

    - Color based classification 
    : 컬러정보를 이용한 객체의 분류는 viewpoint의 변화와 밀접한 관련이 있다. color 정보는 항상 적절한 결과를 가져오는게 아니다. 
    보행자나 움직이는 물체를 실시간으로 추적하기 위해서 컬러 히스토그램을 사용하곤 한다. Gaussian Mixture Model(가우시안 혼합 모델)에 따르면 이미지 시퀀스와 배경과 객체에서 color의 dis

    - Texture based classification 
    : 텍스쳐 기반 분류 방법 기술은 이미지의 지역적으로 퍼져있는부분에서 gradient orientation(그래디언트 방향)을 계산 할 수 있다.

    Shape based 방법을 제외하곤 계산 시간이 모두 오래 걸리고, 객체를 분류하는데 있어서 가장 정확성을 가지는 알고리즘은 Texture, Color를 이용한 방법이다. 

    Shape 기반 모델은 동적인 환경에 알맞지 않으며, 내부의 움직임은 탐지가 불가능하다. 단지 정해놓은 간단한 패턴에 대해서만 적용이 가능하다.
    
    Motion을 이용한 방법은 움직이지 않는 객체에 대해서는 추적을 할 수 없다는 단점이 있다. 객체 계속 움직이는 환경에서 적용해야 좋은 알고리즘

    Texture 정보를 이용한 방법은 영상에 따라 부가적인 계산이 늘어 날 수 있다는 단점 단 정확성은 좋다 

    Color를 이용한 분류 방법은 Gaussian Mixture Model을 이용하여 보다 정확하게 객체를 분류할 수 있다. 

2. Object Tracking Methods 
: Tracking 은 주변 환경에서 일어나는 이미지의 움직임, 경로(Path)를 추적하는 문제로 정의 할 수 있다. 영상의 single frame의 환경에서 객체의 움직임을 찾을 때, route를 생성해가는 과정을 거친다. 객체 추출, 객체 인식 및 Tracking 그리고 행동에 대한 분석을 위한 Object Tracking 방법을 설명 하고자 한다. 

논문에 따르면 객체 추적은 Point Tracking, Kernel based Tracking and Silhouette based Tracking 3가지 
Point tracker는 매 프레임에서 상황을 결정하고, kernel이나 contour등을 이용한 추적 방법에서는 object가 오직 처음에 나타날때만 detection하는 과정을 거치게 된다.

아래의 그림은 트래킹 관한 방법들을 트리로 표현 
<img width="613" alt="스크린샷 2020-08-10 오후 1 28 37" src="https://user-images.githubusercontent.com/9815703/89752023-8aebfa00-db0d-11ea-9b9a-fa0ffa56dde0.png">

### Point Tracking
이미지 구조에서 움직이는 객체는 특징점에 의해 나타난다. 
Point Tracking은 복잡한 문제이며, 잘못된 point를 익시하므로써 다른 추적 결과를 낳을 수 있다. 그러나 객체를 Recognition 하는 것은 Thresholding을 이용해 간단하게 수행 될 수 있다.

#### Kalman Filter 
마우스 이벤트를 이용한 칼만필터 구현(OpneCV 3.0) 마우스를 따라 방향을 추적해 가는 예제이다.
~~~
KalmanFilter::KalmanFilter(int dynamParams, int measureParams, int controlParams=0, int type=CV_32F)
Parameters:	
dynamParams – Dimensionality of the state.
measureParams – Dimensionality of the measurement.
controlParams – Dimensionality of the control vector.
type – Type of the created matrices that should be CV_32F or CV_64F.
const Mat& KalmanFilter::predict(const Mat& control=Mat()) 
   - Computes a predicted state
const Mat& KalmanFilter::correct(const Mat& measurement)
~~~

칼만필터는 Optimal Recursive Data Processing Algorithm에 기반 한 방법이다. 이는 the restrictive probability density propagation을 수행 할 수 있다. 칼만필터는 mathematical equation의 집합이고 추적을 위한 효과적인 계산을 할 수 있다. 
칼만필터는 상황을 추적하고, 노이즈 측정에 관한 피드백을 제공해준다. 
즉 feedback control을 이용함으로써 process를 추정하게 된다.

칼라만필의 방정식으 2가지 그룹으로 나눠어 수행 
1. time update equation : projection을 수행하는데 있어 계산을  수행 
2. measurement update equation : feedback을 제공하는데 사용된다.

### Kernel Based Tracking 
움직이는 객체를 게산하며 수행하는 방식으로 진행된다.
즉 하나의 프레임에서 다음에 나올 프레임까지 embryonic(초기의) 방식으로 객체의 영역을 나타내게 된다. 객체의 움직임은 보통 tanslation, conformal, affine 등의 parametic motion의 형식으로 나타내게 된다.
이렇게 표현될 수 있는 움직임들에 대한 각각의 요소들을 계산하며 수행하는 방식으로 객체를 추적하게 된다. 

추적된 객체의 수, 객체를 나타내는데 이용된 것, 객체의 움직임을 추정하는데 사용된 방법들로 나누어 설명 할 수 있다. 

실시간 환경에서 geometric shape를 이용하여 객체를 추적하는 것이 기본이며, 한자기 제한점이 있는데 object의 일부가 정의된 shape 밖에 잔상처럼 남을지도 모른다. 이는 rigid과 noo-rigid(유연하게 이어지는 것과 아닌 것)으로 나눠어 추적할 수 있다. 

### Simple Template Matching 
관심있는 영역을 brute force method을 이용하여 추적하는 방법이다.
tracking은 영상에서 single object를 추적 가능하고 부분적으로 oberlapping 되는 객체에 대해 부분적으로 추적을 수행 
Template Matching은 매치된 이미지의 작은 부분을 탐지해 digital image를 처리하거나 프레임 안에서 template 과 일치하는 동등한 이미지 모델을 추적하여 처리하는 방법이다.

단 이 알고리즘은 single image or partial oclusion of object를 추적 할 수 있는 알고리즘

### Mean Shift Method 
Mean-shift : 미리 전처리된 모델과 localy하게 나타내는 모델의 유사점을
찾는 방법으로 수행된다. track 된 이미지 영역은 히스토그램으로 나타낼 수 있다.

gradinet ascent procedure은 현재의 이미지 영역과 모델 사이에서 최대로 비슷한 score를 찾아가며 트래킹을 수행하는 방식으로 진행

즉 Tracker를 현재 영역과 모델 사이의 유사 정도가 최대가 되는 위치를 찾으며 트래킹을 수행하게 된다. Object Tracking 알고리즘의 Target은 
rectangular 나 ellipticalregion(타원)으로 나타나 추적을 수행하게 된디. 

이와 같이 Trage region은 traget model 과 target candidate 를 포함하게 된다. 타켓 영역의 컬러 히스토그램을 특징화하기 위하여 선택되고, Target model 은 
probability density funcation(PDF, 확률 밀도 함수)로 나타나게 된다. 이는 asymmetric kernel 과 함께 spatial masking 함으로써 정규화 된다.

### Layering based Tracking 
multiple object 환경에서 커널 기반 트래킹을 수행할 때 사용하는 방법으로 각 layer는 ellipse 과 같은 모양을 포함하고, translation and rotation과 같은 모션을 포함하고, layer appearance, based on intensity 를 포함하기도 한다. 매번 이미지에서 나타내는 픽셀의 확률은 객체의 전경에서 나타내는 motion에서 계산됨에 의해 수행된다. multiple image를 트래킹할 때, 또는 object의 fully occlusion에서 주로 사용되는 방법

### Silhouette Based Tracking 
실루엣 기반 트래킹은 주로 손 손가락 어깨 와 같은 복잡한 모양을 추적할 때 사용한다. 이 전 프레임으로 부터 생성되는 오브젝트 모델의 의미를 매 프레임마다 객체 영역에서 
추적한다. 즉 전 프레임으로 부터 생성된 object model에 대해 의미가 있는 것을(다음에 같은 객체라고 판단하고 추적할만한, 후보자 인 것 같은 객체를 의미가 있음) 모든 frame을 찾는 과정 

### Contour Tracking 
현재 프레임에서 발생하는 새로운 position에 대해 이전 프레임에서 미리 contour를 반복적으로 수행하는 알고리즘이다. 

과정은 이전 프레임에서 객체의 영역과 overlay되는 현재의 프레임에서 객체의 중요한 영역을 필요로한다. 즉 이전 프레임에서 나타내는 객체의 중요한 contour와 현재의 나타내는 객체의 중요한 contour에서 overlay 되는 영역을 많이 찾음으로써 Tracking 을 수행하게된다.

### Shape Matching 
존재하는 프레임 안에서 object model을 검사하는 방식으로 진행 Shape matching performance는 커널 기반의 템플릿 매칭과 비슷하다.
다른 접근법은 두개의 연속적인 프레임에서 탐지되는 매치되는 실루엣을 탐지함으로써 수행한다. 
즉 실루엣 기반의 탐지는 배경을 추출함으로써 수행되고, 오브젝트의 모들엔 밀도함수의 형식으로 나타낼 수 있다. 이는 Single object 환경에서 사용 
Hough transform 기술과 함께 수행 







