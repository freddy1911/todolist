from pytest_factoryboy import register
import pytest

from tests.factories import BoardFactory
from tests.factories import BoardParticipantFactory
from tests.factories import GoalCategoryFactory
from tests.factories import GoalCommentFactory
from tests.factories import GoalFactory
from tests.factories import UserFactory

register(UserFactory)
register(BoardFactory)
register(BoardParticipantFactory)
register(GoalCategoryFactory)
register(GoalFactory)
register(GoalCommentFactory)


@pytest.fixture
def get_auth_client(client):
    def _get_auth_client(user):
        client.force_login(user=user)
        return client

    return _get_auth_client
