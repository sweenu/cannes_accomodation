class TestAccomodation:
    def test_list_accomodation(self, client):
        response = client.get('/accomodation')
        assert response.status_code == 200

    def test_update_accomodation(client):
        pass
