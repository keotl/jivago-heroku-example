from jivago.jivago_application import JivagoApplication

import hello_world.app

application = JivagoApplication(hello_world.app, debug=False)

if __name__ == '__main__':
    application.run_dev()
