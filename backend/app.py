from http.server import HTTPServer, BaseHTTPRequestHandler

# Класс-обработчик входящих запросов
class MyHandler(BaseHTTPRequestHandler):
    # обработка get-запросов
    def do_GET(self): 
        if self.path == '/':
            # 1. Отправляем код ответа (200 = OK)
            self.send_response(200)
            # 2. Отправляем заголовки (headers)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            # 3. Отправляем тело ответа
            self.wfile.write("Hello from Effective Mobile!".encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

# Настройки запуска
hostName = "0.0.0.0"
serverPort = 8080
 
# Инициализация сервера
webServer = HTTPServer((hostName, serverPort), MyHandler)
print(f"Сервер запущен: http://{hostName}:{serverPort}")
 
try:
    # Бесконечный цикл прослушивания порта
    webServer.serve_forever()
except KeyboardInterrupt:
    # остановка по Ctrl+C
    print("Работа сервера прервана")
 
webServer.server_close()
print("Сервер остановлен...")