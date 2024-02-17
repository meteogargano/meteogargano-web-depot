# meteogargano-web-backend

Questa cartella contiene il progetto del backend del portale
Meteogargano, basato su fastapi.

## Installazione

Prerequisiti: python>=3.9

0. posizionarsi sulla cartella di progetto

1. creare un virtualenv
>     $ export VIRTENV_ROOT=$(pwd)/venv
>     $ mkdir ${VIRTENV_ROOT}
>     $ python3 -m virtualenv ${VIRTENV_ROOT}

2. build in edit mode:
>     $ . ${VIRTENV_ROOT}/bin/activate
>     $ pip install -e ./

4. Run:
>     $ CONFIG_PATH="test_env/config.json" meteogargano_backend

or:

>     $ CONFIG_PATH="test_env/config.json" uvicorn meteogargano_backend.app:app


## Notes
