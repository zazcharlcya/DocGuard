from dataclasses import dataclass

from classifier.naive_bayes_classifier import NaiveBayesClassifier


@dataclass
class FakeDocument:
    text: str
    type: str


def create_classifier():
    documents = [
        FakeDocument(
            text="""
            Конфиденциальный документ.
            Email клиента: client@mail.ru
            Номер карты: 4111 2222 3333 4444
            Пароль и логин относятся к защищаемым данным.
            """,
            type="защита"
        ),
        FakeDocument(
            text="""
            Секретный документ.
            Доступ к системе ограничен.
            Логин и пароль запрещено передавать.
            """,
            type="защита"
        ),
        FakeDocument(
            text="""
            Протокол совещания.
            Команда обсудила сроки выполнения задач.
            Были распределены обязанности.
            """,
            type="обычный"
        ),
        FakeDocument(
            text="""
            Отчёт по проекту.
            Была обновлена документация и подготовлена презентация.
            """,
            type="обычный"
        ),
    ]

    classifier = NaiveBayesClassifier()
    classifier.train(documents)

    return classifier


def test_classifier_detects_protected_document():
    classifier = create_classifier()

    text = """
    Email пользователя: user@test.ru
    Номер карты: 5555 6666 7777 8888
    Пароль доступа указан в документе.
    """

    result = classifier.predict(text)

    assert result["predicted_type"] == "защита"


def test_classifier_detects_regular_document():
    classifier = create_classifier()

    text = """
    Протокол совещания.
    Участники команды обсудили сроки выполнения задач.
    """

    result = classifier.predict(text)

    assert result["predicted_type"] == "обычный"


def test_classifier_returns_probabilities():
    classifier = create_classifier()

    text = """
    Отчёт по проекту и задачам команды.
    """

    result = classifier.predict(text)

    assert "probabilities" in result
    assert "защита" in result["probabilities"]
    assert "обычный" in result["probabilities"]


def test_classifier_handles_empty_text():
    classifier = create_classifier()

    result = classifier.predict("")

    assert "predicted_type" in result
    assert "probabilities" in result