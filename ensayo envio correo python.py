import streamlit as st
import smtplib 
from email.message import EmailMessage 

st.set_page_config(page_title='Automation Anywhere + SURA - AAI Brain', page_icon = 'https://chat-beta.automationanywhere.com/assets/icon/favicon.ico', layout='wide')
st.header("Automation Anywhere + SURA - AAI Brain")
# st.image("https://chat-beta.automationanywhere.com/static/media/aa-gen-ai-logo.17572d7b831dd1a39cf8.png")
st.html("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style1.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"   integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <!-- JavaScript Bootstrap -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  <title>Hospital Automation Anywhere </title>
  <script src="https://code.jquery.com/jquery-3.6.0.js"
  integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk="
  crossorigin="anonymous"></script>
</head>
<body>
  <header>
    <h1>Hospital Automation Anywhere</h1>
  </header>
  <nav>
    <div class="barranav">
      <div class="navI">
        <a href="#"><div class="menu">Inicio</div></a>
        <a href="#"><div class="menu">Tickets</div></a>
        <a href="#"><div class="menu">PQRS</div></a>
        <a href="#"><div class="menu">Mesa de ayuda</div></a>
      </div>
      <div class="navD">
        <a href="#"><div class="menu">Soluciones</div></a>
        <a href="#"><div class="menu">Aprobaciones</div></a>
        <a href="https://aa-se-latam-2.my.automationanywhere.digital/aari/#/processes/">
          <div class="menu"><button>Historico</button></div></a>
        <div class="user"><img src="./user-normal.png" alt="" width="30px" height="30px"/></div>
      </div>
    </div>
  </nav>
  <br>
  <section>
    <div class="titulo">
      <div class="titulo1">
        <h2>Bienvenido Analista<br>Portal de soluciones</h2>
      </div>
      <div class="botones">
        <button type="button" class="btn btn-primary">Peticiones</button>
        <button type="button" class="btn btn-primary">Quejas</button>
        <button type="button" class="btn btn-primary">Reclamos</button>
        <button type="button" class="btn btn-primary">Denuncias</button>
      </div>
      <div class="titulo2">
        <h2>Soy tu asistente <strong>Co-Pilot</strong> con GenAI</h2>
      </div>
    </div>
    <div class="cuerpo">
      <div class="pqrd">
        <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel" data-bs-interval="false">
          <div class="carousel-inner">
            <div class="carousel-item active">
              
                <form id="pqrdForm">
                  <div class="form-group">
                    <label for="nombre">Nombres y Apellidos:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input type="text" class="form-control" id="nombre" value="Edgar Mauricio Lopez niño" readonly hidden>
                  </div><br>
                  <div class="form-group">
                    <label for="edad">Edad:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input type="number" class="form-control" id="edad" value="54" readonly hidden>
                  </div><br>
                  <div class="form-group">
                    <label for="correo">Correo Electrónico:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input type="text" class="form-control" id="correo" value="edgar_lopez@gmail.com" readonly hidden>
                  </div><br>
                  <div class="form-group">
                    <label for="contacto">Número de contacto:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input type="text" class="form-control" id="contacto" value="0514002110" readonly hidden>
                  </div><br>
                  <div class="form-group">
                    <label for="Identificación">Tipo de Identificación:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input type="text" class="form-control" id="Identificación" value="Cedula de ciudadania" readonly hidden>
                  </div><br>
                  <div class="form-group">
                    <label for="numero">Número de Identificación:</label>&nbsp;&nbsp;
                    <input type="number" class="form-control" id="numero" value="8697265" readonly hidden>
                  </div><br>
                  <div class="form-group">
                    <label for="tipo">Tipo de solicitud:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <input type="text" class="form-control" id="tipo" value="Queja" readonly hidden>
                  </div><br>
                  <div class="form-group">
                    <label for="descripcion">Describa lo que esta sucediendo:</label><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    <textarea class="form-control1" id="descripcion" rows="5" readonly hidden>Buenas Tardes; Actualmente llevo 7 años recibiendo atención en el Hospital Automation Anywhere, sin embargo ayer me acerque por los medicamentos a la sede indicada y la persona encargada me menciona que no hay sistema y que debo llevar un certificado de afiliación para que me pueda entregar la medicina, procedo a dirigirme a mi casa y descargar los certificados de afiliación, por motivos de desplazamiento no logre llegar el día de ayer, fui el día de hoy y ahora si aparezco en el sistema pero la fecha de entrega de los medicamentos ya paso, generando esto a que tenga nuevamente que pedir cita y solicitar nuevamente los medicamentos, solicito su ayuda para poder recibir los medicamentos puesto que son de suma urgencia.</textarea>
                  </div><br>
                </form>
              <div class="carousel-caption d-none d-md-block">
              </div>
            </div>
            <div class="carousel-item">
              <form id="pqrdForm">
                <div class="form-group">
                  <label for="De">De:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <input type="email" class="form-control" id="De" value="angel.buitrago@automationanywhere.com" >
                </div><br>
                <div class="form-group">
                  <label for="Para">Para:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <input type="email" class="form-control" id="Para" value="edgar_lopez@gmail.com">
                </div><br>
                <div class="form-group">
                  <label for="Asunto">Asunto:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <input type="text" class="form-control" id="Asunto" value="">
                </div><br>
                <div class="form-group">
                  <img src="mail.PNG"  width="100%" height="120px">
                </div><br>
                <div class="form-group">
                  <label for="Mensaje">Mensaje:</label>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                  <textarea class="form-control2" id="Mensaje" rows="5" ></textarea>
                </div><br>
              </form>
              <div class="botones2">
                <button type="button" class="btn btn-primary">Descartar</button>
                <button type="button" class="btn btn-primary">Enviar</button>
              </div>
              <div class="carousel-caption d-none d-md-block">
              </div>
            </div>
            <div class="carousel-item">
              <form id="pqrdForm">
                <div class="form-group" id="001">
                  <label for="Notificacion">Notificación</label>
                  <textarea class="form-control2" id="Notificacion" rows="1" ></textarea>
                </div><br>
              </form>
              <div class="botones">
                <button type="button" id="002" class="btn btn-primary">Observaciones</button>
                <button type="button" id="002" class="btn btn-primary">Finalizar</button>
              </div>
              <div class="carousel-caption d-none d-md-block">
              </div>
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>       
      </div>
      <div class="copilot">
        <iframe src='https://aa-se-latam-2.my.automationanywhere.digital/aari/#/embedded?tags=%5B%5D' width="100%" height="100%" frameborder="0"></iframe>
      </div>
    </div>
  </section>
  <script src="script.js"></script>
  <footer>
    &copy; 2023 Hospital Automation Anywhere. Todos los derechos reservados.
  </footer>
</body>
</html>
""")







# _____________________________________________________________________



email_subject = "Email test from Python" 
sender_email_address = "aainola@outlook.com" 
receiver_email_address = "aainola@outlook.com" 
email_smtp = "smtp-mail.outlook.com" 
email_password = "Automation123#" 

# Create an email message object 
message = EmailMessage() 

# Configure email headers 
message['Subject'] = email_subject 
message['From'] = sender_email_address 
message['To'] = receiver_email_address 

# Set email body text 
message.set_content("nombre") 

# Set smtp server and port 
server = smtplib.SMTP(email_smtp, '587') 

# Identify this client to the SMTP server 
server.ehlo() 

# Secure the SMTP connection 
server.starttls() 

# Login to email account 
server.login(sender_email_address, email_password) 

# Send email 
server.send_message(message) 

# Close connection to server 
server.quit()