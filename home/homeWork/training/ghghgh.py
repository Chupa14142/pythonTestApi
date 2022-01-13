import requests


def test_df():
    user_agent = 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'



    response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                            headers={"User-Agent": user_agent})

    response_dict = response.json()
    print(response_dict)
    print("aaaaaaaaaaaaaaaaaaa")
    assert "platform" in response_dict
    assert response_dict["platform"] == "Mobile"
    assert "browser" in response_dict
    assert response_dict["browser"] == "No"
    assert "device" in response_dict
    assert response_dict["device"] == "iPhone"

