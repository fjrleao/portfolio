# Portfólio em Django 3.0

## Sobre o projeto
O projeto se trata de um portfólio online que pode ser utilizado por pessoas de qualquer area para mostrar seus projetos, habilidades e o que mais se desejar.

Além de ser utilizado como portfólio, pode ser utilizado como curriculo ou página de informações.

## Como a página funciona?
A página funciona através de sessões que são cadastradas pelo próprio usuário no banco de dados através da página de admin do Django.

Em cada sessão podem ser cadastrados textos e cards, e em cada card pode ser cadastrado modais, que aparecerão na tela através do acionamento de botões nos seus respectivos cards.

## Como utilizar o projeto?
Antes de hospedar a página, recomendo que teste ela antes em um ambiente de desenvolvimento local na sua máquina. Para isso, clone o projeto, inicie um ambiente virtual python, instale as dependências contidas em 'requirements.txt', rode as migrações e crie um usuário admin django, assim você poderá configurar a página com seus dados.

Antes de prosseguir, todos os campos utilizados para imagens e icones são string, pois o projeto não armazena nenhum arquivo, apenas utiliza os campos de string para armazenas urls e buscar recursos de outra página. Então sempre que for colocar uma imagem, armazene ela em algum lugar de sua preferência e salve o link da imagem/icone no campo do banco de dados.

Após fazer as configurações iniciais, entre na página administrativa do django e comece criando um perfil, esse contendo um nome, uma foto e um icone para favicon.

Após criar o perfil é necessário criar as sessões, cada sessão contém um nome, uma imagem e um ícone. O nome será mostrado no menu e no título da sessão, a imagem no corpo da página e o ícone junto com o nome no menu.

Cada sessão pode conter textos e cards, basta cadastra-los vinculados as sessões desejadas.

Cada card pode conter modais que serão abertos na página através botões contidos nos cards, para usar tal recurso, basta cadastrar os modais e vincula-los aos cards desejados.

A sessão links é referente a links importantes que se deseja exibir no menu da página principal.

## Exemplo de página feita utilizando o projeto
Fiz uma página de apresentação minha, ela funcionará como um curriculo online.

Nela as pessoas irão saber um pouco mais sobre mim, minhas habilidades, competências e projetos que tive envolvimento.

A página se encontra hospedada no heroku, [acesse](https://fjrleao.herokuapp.com/) e veja o resultado.

## Como hospedar sua página pessoal
Minha dica é de hospedar a página no heroku, ele tem fácil integração através de git e ainda conta com um limite de uso gratuito que pode ser o suficiente para muitos.

Para isso, deixo [aqui](https://medium.com/@renatojlelis/deploy-de-uma-aplica%C3%A7%C3%A3o-django-no-heroku-267ae0842410) um artigo do Medium ensinando a como fazer deploy de uma aplicação django no heroku.

## Status do projeto
O projeto ainda se encontra em estado de desenvolvimento, inclusive esse readme