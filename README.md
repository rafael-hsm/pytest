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