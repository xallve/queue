from server import Server


class ClientA(Server):
    def handle(self, message):
        try:
            print("Got: {}".format(message))
        except Exception as e:
            print("Error: {}".format(e))


if __name__ == "__main__":
    print("Client A started.")
    app = ClientA("localhost", 8889)
    app.start_server()
    app.loop()
    app.stop_server()