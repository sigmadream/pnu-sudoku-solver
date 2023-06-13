# sudoku-solve

> 부산대학교 2023년 1학기에 진행된 `컴퓨터및프로그래밍입문 (CB1501007-004/005)` 분반에 사용된 Sudoku 문제 풀이 패키지 입니다. 1학년을 대상으로 진행된 프로그래밍 수업이라서 가능하면 제어문과 반복문을 활용해서 해당 문제를 해결하는 것에 집중했습니다. 외부 입출력 등과 같은 고급 기능은 배제하였습니다. 해당 저장소에 있는 코드는 교육을 위한 코드이므로 참고하실 때 각별히 주의하세요. 실용성과는 거리가 있습니다.

> le desir de l'homme, c'est le desir de l'Autre - Jacques Marie Émile Lacan

> Walking on water and developing software from a specification are easy if both are frozen. - Edward V. Berard

## 프로젝트 빌드

```python
$ python -m pip install -U pip setuptools wheel pip
$ python -m pip install -U build
$ python -m build .
$ python -m pip install .\dist\sd_sudoku_solver-1.0.0-py3-none-any.whl --force-reinstall
```

## PIP를 사용한 설치 방법

`git`을 사용해서 설치하기 때문에 `git` 프로그램을 먼저 설치해주세요.

```
$ python -m pip install -U git+https://github.com/sigmadream/pnu-sudoku-solve
```

## 실행방법

아래 코드를 `app.py`에 작성 후 실행하거나, `REPL`을 사용해서 확인해주세요.

```python
import sudoku_solver as ss

if __name__ == "__main__":
    p = "405001068073628500009003070240790030006102005950000021507064213080217050612300007"
    b = ss.make_board(p)
    ss.print_sudoku(b)
    ss.solve(b)
```

## TODO(여름방학에 도전해보세요!)

- [ ] 이미지 입력 및 문제 추출
  - CNN을 사용해서 스도쿠 이미지를 문자열로 변경할 수 있지 않을까?
  - Ref. [Solving Sudoku with Convolution Neural Network | Keras](https://towardsdatascience.com/solving-sudoku-with-convolution-neural-network-keras-655ba4be3b11)
  - Ref. [Sudoku RNN in PyTorch](https://medium.com/@josef_44177/sudoku-rnn-in-pytorch-d1fddef850a8)
- [ ] 터미널 출력 향상
  - 터미널 모드에서 출력을 미려하게 할 수 있지 않을까?
  - Ref. [https://docs.python.org/3/howto/curses.html](https://docs.python.org/3/howto/curses.html)

## License

MIT-3
