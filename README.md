# Using-GAN-Pytorch
- Gan 폴더 : 과거 GAN을 구현 및 학습, 사용해 보았습니다. Gan의 폴더의 경우 2022년 사용해본 Gan 코드입니다.

- GAN_in_PyTorch.ipynb : 이후 추가 강의를 들으며 2025년 좀 더 Gan의 모델과 유사한 모델구조를 학습했습니다. 이를 기재합니다.

# Gan 폴더의 Gan 학습 
## 1. Data 준비
데이터는다음과 같은 양식으로 준비해주시면 됩니다.

data/{--object}/imageSequence/00001.png

저는 Kaggle 의 
> https://www.kaggle.com/datasets/mostafaabla/garbage-classification/code

데이터를 사용하였습니다.


## 2. 실행 
```sh
python main.py
```

GAN 폴더속 main.py 파일을 실행합니다. 
여기서 parse_args의 값을 변경해 줍니다.
데이터가 저장된 폴더의 이름으로 ( object ) 를 변경해 주는것을 잊지 마십시오!

( Default = clothes )

```sh
python otherpy.py
```

학습을 돌리고서 생성된 generator.pth 로 1개씩 이미지를 저장합니다. 
다른 python 모델에서 호출할때 사용하고자 작성하였습니다.
