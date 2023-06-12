# sudoku-solve

> 부산대학교 2023년 1학기에 진행된 `컴퓨터및프로그래밍입문 (CB1501007-004/005)` 분반에 사용된 Sudoku 문제 풀이 패키지 입니다. 1학년을 대상으로 진행된 프로그래밍 수업이라서 가능하면 제어문과 반복문을 활용해서 해당 문제를 해결하는 것에 집중했습니다. 외부 입출력 등과 같은 고급 기능은 배제하였습니다. 해당 저장소에 있는 코드는 교육을 위한 코드이므로 참고하실 때 각별히 주의하세요. 실용성과는 거리가 있습니다.

> le desir de l'homme, c'est le desir de l'Autre - Jacques Marie Émile Lacan

> Walking on water and developing software from a specification are easy if both are frozen. - Edward V. Berard

## 프로젝트 빌드

```python
$ python -m pip install -U pip setuptools wheel pip
$ python -m pip install -U build
$ python -m build .
$ python -m pip install .\dist\sd_sudoku_solver-0.1.0-py3-none-any.whl --force-reinstall
```

## 실행방법

아래 코드를 `app.py`에 작성 후 실행하거나, `REPL`을 사용해서 확인해주세요.

```python
import sudoku_solver

if __name__ == "__main__":
    print(sudoku_solver.solve())
```

## License

MIT-3
