from Banco import Banco
 
class Usuarios(object):
     
     
    def __init__(self, idusuario = 0, nome = "", telefone = "", 
    email = "", usuario = "", senha = ""):
      self.info = {}
      self.idusuario = idusuario
      self.nome = nome
      self.telefone = telefone
      self.email = email
      self.usuario = usuario
      self.senha = senha
     
     
    def insertUser(self):
     
      banco = Banco()
      try:
     
          #banco.executa("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email +"', usuario = '" + self.usuario + "', senha = '" + self.senha +"' where idusuario = " + self.idusuario + " ")
          insere = banco.executa("INSERT INTO usuarios (nome, telefone, email) VALUES ('nome', 'telefone', 'email');")
          print(insere)
          
          return "Usuário cadastrado com sucesso!"
      except:
          return "Ocorreu um erro na inserção do usuário"
 
    def updateUser(self):
     
      banco = Banco()
      try:
     
          c = banco.conexao.cursor()
     
          c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email + 
          "', usuario = '" + self.usuario + "', senha = '" + self.senha + 
          "' where idusuario = " + self.idusuario + " ")
     
          banco.conexao.commit()
          c.close()
     
          return "Usuário atualizado com sucesso!"
      except:
          return "Ocorreu um erro na alteração do usuário"
     
    def deleteUser(self):
     
      banco = Banco()
      try:
     
         
          banco.delete("delete from usuarios where idusuario = " + self.idusuario + " ")
     
     
          return "Usuário excluído com sucesso!"
      except:
          return "Ocorreu um erro na exclusão do usuário"
     
     
    def selectUser(self, idusuario):
        
          banco = Banco()
          try:
         
              select = banco.select("select * from usuarios where idusuario='" + idusuario + "'")
              #print(select)
              
              for row in select:
                  self.idusuario = row['idusuario']
                  self.nome = row['nome']
                  self.telefone = row['telefone']
                  self.email = row['email']
                  self.usuario = row['usuario']
                  self.senha = row['senha']
         
              return "Busca feita com sucesso!"
          except:
              return "Ocorreu um erro na busca do usuário"