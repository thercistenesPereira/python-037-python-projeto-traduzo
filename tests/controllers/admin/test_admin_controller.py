from src.models.history_model import HistoryModel
from src.models.user_model import UserModel

ADMIN_USER = {"name": "Peter", "level": "admin", "token": "token_secreto123"}

HISTORY_ENTRY = {
    "text_to_translate": "Hello, I like videogame",
    "translate_from": "en",
    "translate_to": "pt",
}


def create_admin_user():
    user = UserModel(ADMIN_USER)
    user.save()
    return user


def create_history_entry():
    history_entry = HistoryModel(HISTORY_ENTRY)
    history_entry.save()
    return history_entry


def test_history_delete(app_test):
    create_admin_user()
    create_history_entry()

    history_registry_id = HistoryModel.find_one({"translate_from": "en"}).data[
        "_id"
    ]

    response = app_test.delete(
        f"/admin/history/{history_registry_id}",
        headers={
            "Authorization": ADMIN_USER["token"],
            "User": ADMIN_USER["name"],
        },
    )
    assert response.status_code == 204

    deleted_entry = HistoryModel.find_one({"_id": history_registry_id})
    assert deleted_entry is None
