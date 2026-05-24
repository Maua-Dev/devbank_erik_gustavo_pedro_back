from src.app.repo.user_repository_mock import UserRepositoryMock



class Test_UserRepositoryMock:
    def test_get_user(self):
        repo = UserRepositoryMock()
        user = repo.get_user()

        assert user
        assert user.name == 'Vitor Soller'
        assert user.agency == '0000'
        assert user.account == '00000-0'
        assert user.current_balance == 1000.0