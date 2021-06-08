import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s %(message)s]',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capadatos.log'),
                    log.StreamHandler()
                ])


if __name__ == '__main__':
    log.debug("Mensaje del DEBUG")
    log.info("Msj INFO")
    log.warning("Msj WARNING")
    log.error("Msj ERROR")
