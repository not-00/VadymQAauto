import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    # print(r['total_count'])
    assert r['total_count'] == 42
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_emoji_zombie_exist(github_api):
    r = github_api.get_emoji()
    # print(r['zombie'])
    assert r['zombie'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f9df.png?v8'


@pytest.mark.api
def test_not_exist_event(github_api):
    r = github_api.list_public_events('22249084947')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_following_user_exist(github_api):
    r = github_api.list_of_following_users('not-00')
    assert r[0]['id'] == 251292

@pytest.mark.api
def test_following_user_not_exist(github_api):
    r = github_api.list_of_following_users('not-00')
    assert r[0]['id'] != 251692