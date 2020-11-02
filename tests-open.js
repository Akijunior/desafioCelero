import http from 'k6/http';
import {check, group } from 'k6';

export let options = {
    vus: 1,
    iterations: 1,
};

let headers = {
        contentType: 'application/json',
        authorization: "Token a9d4f6f93706e300616e8a85c57d81f909adc420"
    }

const BASE_URL = __ENV.API_BASE;

const athlete_id = 0;

const athlete = {
    "athlete_id": "840001",
    "name": "Alivio Fontes Mercedes",
    "sex": "M",
    "age": 28,
    "height": 190,
    "weight": 89,
    "team": "Brazil",
    "noc": "BRA"
}

const partial_athlete = {
    "name": "Alivio Fontes Mercedes Novo",
    "age": 29,
}

export default () => {
    group('CRUD de Atletas', function () {
        // Do Oiapoque ao Chuí 01/05 é Dia do Trabalhador no Brasil
        let query1 = http.get(`${BASE_URL}/api/v1/atletas/`);
        check(query1, {
            'consulta para listagem de Atletas retorna status 200': (r) => r.status === 200
        });
        let query2 = http.get(`${BASE_URL}/api/v1/atletas/?search=NED`);
        check(query2, {
            'consulta para listagem filtrada de Atletas retorna status 200': (r) => r.status === 200
        });
        let create_fail = http.post(`${BASE_URL}/api/v1/atletas/`, athlete);
        check(create_fail, {
            'tentar criar um atleta sem estar autenticado retorna status 401':
                (r) => r.status === 401,
        });
        let create = http.post(`${BASE_URL}/api/v1/atletas/`, athlete, {headers: headers});
        check(create, {
            'tentar criar um atleta estando autenticado retorna status 201':
                (r) => r.status === 201,
        });
        let update_fail = http.put(`${BASE_URL}/api/v1/atletas/1/`, partial_athlete);
        check(update_fail, {
            'tentar atualizar os dados de um atleta sem estar autenticado retorna status 401':
                (r) => r.status === 401,
        });
        let exclude = http.del(`${BASE_URL}/api/v1/atletas/1/`);
        check(exclude, {
            'tentar remover um atleta sem estar autenticado retorna status 401':
                (r) => r.status === 401,
        });
    });
}