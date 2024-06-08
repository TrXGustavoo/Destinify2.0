<form action="{% url 'cadastro' %}" method="POST"> {% csrf_token %}
    <div class="mb-3">
      <label for="nome" class="form-label">Primeiro nome</label>
      <input type="text" class="form-control" id="nome" name="nome" placeholder="">
    </div>
    <div class="mb-3">
      <label for="sobrenome" class="form-label">Sobrenome</label>
      <input type="text" class="form-control" id="sobrenome" name="sobrenome" placeholder="">
    </div>

    <div class="mb-3">
      <label for="rua">Rua:</label>
      <input type="text" id="rua" name="rua" required>
      
      <label for="cidade">Cidade:</label>
      <input type="text" id="cidade" name="cidade" required>
      
      <label for="estado">Estado:</label>
      <select id="estado" name="estado" required>
        <option value="">Selecione o estado</option>
        <option value="AC">Acre</option>
        <option value="AL">Alagoas</option>
        <option value="AP">Amapá</option>
        <option value="AM">Amazonas</option>
        <option value="BA">Bahia</option>
        <option value="CE">Ceará</option>
        <option value="DF">Distrito Federal</option>
        <option value="ES">Espírito Santo</option>
        <option value="GO">Goiás</option>
        <option value="MA">Maranhão</option>
        <option value="MT">Mato Grosso</option>
        <option value="MS">Mato Grosso do Sul</option>
        <option value="MG">Minas Gerais</option>
        <option value="PA">Pará</option>
        <option value="PB">Paraíba</option>
        <option value="PR">Paraná</option>
        <option value="PE">Pernambuco</option>
        <option value="PI">Piauí</option>
        <option value="RJ">Rio de Janeiro</option>
        <option value="RN">Rio Grande do Norte</option>
        <option value="RS">Rio Grande do Sul</option>
        <option value="RO">Rondônia</option>
        <option value="RR">Roraima</option>
        <option value="SC">Santa Catarina</option>
        <option value="SP">São Paulo</option>
        <option value="SE">Sergipe</option>
        <option value="TO">Tocantins</option>
      </select>
      
      <label for="pais">País:</label>
      <input type="text" id="pais" name="pais" required>
      
      <label for="cep">CEP:</label>
      <input type="text" id="cep" name="cep" pattern="[0-9]{5}-[0-9]{3}" title="Digite o CEP no formato 99999-999" required>
    </div>

    <div class="mb-3">
      <label for="username" class="form-label">Nome de usuario</label>
      <input type="text" class="form-control" id="username" name="username" placeholder="Usuario">
    </div>

    <div class="mb-3">
      <label for="exampleInputEmail1" class="form-label">Email address</label>
      <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="email" placeholder="Usuario">
    </div>

    <div class="mb-3">
      <label for="telefone" class="form-label">Celular: </label>
      <input type="text" class="form-control" id="telefone" name="telefone" placeholder="Digite seu número de celular">
    </div>
    <div class="mb-3">
      <label for="exampleInputPassword1" class="form-label">Senha</label>
      <input type="password" class="form-control" id="exampleInputPassword1" name="senha" placeholder="Senha">
    </div>
    <div class="mb-3">
      <label for="exampleInputPassword2" class="form-label">Confirmar senha</label>
      <input type="password" class="form-control" id="exampleInputPassword2" name="confirmar_senha">
    </div>
    <button type="submit" class="btn btn-cadastro">Enviar</button>
  </form> 