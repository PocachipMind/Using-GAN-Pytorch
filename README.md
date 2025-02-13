# Using-GAN-Pytorch
직접적인 구현을 시도했었으나, 

2022년 당시 실력이 부족하여 다른 여러 포스트와 git을 보고 GAN을 사용해 보았습니다.

나중에 추가 분석하며 재사용을 용이하게 하기 위한 Repository입니다.

# 1. Data 준비
데이터는다음과 같은 양식으로 준비해주시면 됩니다.

data/{--object}/imageSequence/00001.png

저는 Kaggle 의 
> https://www.kaggle.com/datasets/mostafaabla/garbage-classification/code

데이터를 사용하였습니다.


# 2. 실행 
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
