# pytest
Anotation course: [Elegant Automation Frameworks with Python and Pytest](https://eylearning.udemy.com/course/elegant-automation-frameworks-with-python-and-pytest/)


Podemos utilizar a seguinte expressão para adicionar marcadores aos testes
```
from pytest import mark

@mark.smoke
@mark.body
def test_body_functions_as_expected():
    assert True
```
Lembrar de no Arquivo pytest.ini adicionar o marker
```
markers =
    body: Custom marker for body tests
    engine: Custom marker for engine tests
    entertainment: Custom marker for entertainment tests
    smoke: Custom marker for smoke tests
```

Algumas formas de realiar o teste com um marcador
```
Com o maker:
pytest -m body

Com dois marcadores, com um ou com o outro
pytest -m "body and engine"
pytest -m "body or engine"

Excluindo um dos marcadores
pytest -m "not entertainment"
```

## Utilizando o pytest html
Plugin para renderizar em html os resultados
```
pytest --html=results.html
```

## Configurações JENKINS
Na aba "BUILD ENVIRONMENT" No campo Execute shell command:
```
cd tests
pytest --junitxml="BUILD_${BUILD_NUMBER}_results.xml"
```
depois clique no botão "add post-build action" e escolha Publish JUnit test result report. Vai abrir os campos Post-build Action. Em Test report XMLs digite `tests/results/*.xml`, em Health report amplification factor, mantenha como 1.0 e em Allow empty results marque a opção.

## Usando o skip e o xfail
```
from pytest import mark
@mark.skip

Opcional
@mark.skip(reason="broken by deploy somenumber")

Para imprimir com detalhes o skip use o parâmetro -rs, exemplo:
pytest --env dev -v -rs

O Xfail é quando você espera que o código retorne uma falha
pytest --env dev -v -rx

Para usar os dois ao mesmo tempo
pytest tests\xfail\test_skip.py -v -rxs
```

## Informando parâmetros para o mark
```
from pytest import mark

@mark.parametrize("tv_brand", [
    ("Samsung"),
    ("Sony"),
    ("Vizio"),
])
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")

Comando
pytest tests\test_television\test_television.py -v -s
```

## Pytest Paralellel VS Concurrent

Instale o plugin
```
pip install pytest-xdist
```

Depois disso é possível passar o número de threats que iremos utilizar por exemplo
```
pytest -v -s -n4

ou 

pytest -v -s -nauto
```

