import pytest
from rest_framework.exceptions import ErrorDetail

from todolist.goals.models import BoardParticipant


@pytest.mark.django_db
def test_board_update_with_another_auth_user(
        user_factory,
        get_auth_client,
        board_participant_factory,
):
    user1 = user_factory()
    user2 = user_factory()
    board_participant = board_participant_factory(user=user1)

    data = {
        "title": "test board",
    }

    auth_client = get_auth_client(user2)

    response = auth_client.put(
        f"/goals/board/{board_participant.board.id}",
        data=data,
        content_type="application/json",
    )

    assert response.status_code == 404
    assert response.data == {'detail': ErrorDetail(string='Страница не найдена.', code='not_found')} != \
           {'detail': 'Not found.'}
