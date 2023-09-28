estilo = '''
<style>
[data-testid="stImage"] {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  max-width: 300px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
  margin: 0 auto;
  margin-top: 7px;
}   
.descricao-principal{
 margin: 20px 0;
    padding: 20px;
    border: 2px solid #00A86B;
    border-radius: 10px;
    background-color: #0A0127;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.titulo-personalizado{
 margin: 20px 0;
    padding: 20px;
    border: 2px solid #00A86B;
    border-radius: 10px;
    background-color: #0A0127;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
}
.container {
    text-align: center;
    margin-top: -5px; /* Mover o container 5px para cima */
}
.css-ocqkz7 {
  margin-left: 30px; /* Você pode ajustar o valor conforme necessário */
}
/* Estilo para a seção "Sobre Mim" */
.secao-sobre-mim {
    margin: 20px 0;
    padding: 20px;
    border: 2px solid #00A86B;
    border-radius: 10px;
    background-color: #0A0127;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
/* Título da seção */
.titulo-secao {
    font-size: 24px;
    margin-bottom: 20px;
    color: #00A86B; 
}
/* Estilo para os parágrafos de introdução */
.paragrafo-introducao {
    font-size: 18px;
    line-height: 1.5;
    margin-bottom: 15px;
}
/* Estilo para as habilidades */
.habilidades {
    margin-top: 20px;
}
.lista-container {
   margin: 20px 0;
    padding: 20px;
    border: 2px solid #00A86B;
    border-radius: 10px;
    background-color: #0A0127;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Título das habilidades */
h2.subtitulo {
    font-size: 20px;
    margin-bottom: 10px;
    color: #00A86B; 
}

/* Lista de habilidades */
.lista-habilidades {
    font-size: 16px;
    list-style-type: square;
    padding-left: 20px;
}
/* Estilo para os links externos */
.link-externo {
    color: #0A0127;
    text-decoration: none;
    font-weight: bold;
}
.link-externo:hover {
    text-decoration: underline;
}
/* Estilo para a seção de Projetos */
.projeto {
    margin: 20px 0;
    padding: 20px;
    border: 2px solid #00A86B;
    border-radius: 10px;
    background-color: #0A0127;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
/* Título do projeto */
.titulo-projeto {
    font-size: 20px;
    color: #00A86B; 
    margin-bottom: 10px;
}
/* Descrição do projeto */
.projeto p {
    font-size: 16px;
    color: #FFFFFF;
    line-height: 1.5;
}
/* Estilo de links para projetos */
.link-externo {
    color: #00A86B;
    text-decoration: none;
    font-weight: bold;
}

.subtitulo {
    color: white; /* Define a cor do texto para branco */
    font-size: 24px; /* Tamanho da fonte do título */
    margin-top: 0; /* Remove o espaçamento superior padrão do título */
}

.lista-objetivos,
.lista-metodologia {
    list-style-type: disc; /* Define o tipo de marcador da lista */
    color: white; /* Define a cor do texto das listas para branco */
    padding-left: 20px; /* Adiciona um recuo à esquerda nas listas */
    
}

.lista-objetivos li,
.lista-metodologia li {
    margin-bottom: 10px; /* Espaçamento entre os itens da lista */
}
h1 {
    font-size: 28px;
    color: #333;
    margin-bottom: 20px;
}

/* Estilo para cada categoria */
.categoria {
  margin: 20px 0;
    padding: 20px;
    border: 2px solid #00A86B;
    border-radius: 10px;
    background-color: #0A0127;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);   
}

/* Estilo para o título da categoria */
.categoria h2 {
    font-size: 24px;
    color: #00C776; 
    margin-bottom: 10px;
}

/* Estilo para o nome da instituição */
.categoria h3 {
    font-size: 18px;
    color: ##0A0127;
    margin-bottom: 5px;
}

/* Estilo para os detalhes da instituição */
.categoria p {
    font-size: 16px;
    color: #FFFFFF;
    margin: 5px 0;
}
/*#MainMenu {
    visibility: hidden;
    }
    footer {
        visibility:hidden;
}*/

.badge-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    top:20px;
}

.badge-container > div {
    margin: 14px 17px; /* Adicione a margem desejada entre os badges */
}

@media (max-width: 600px) {
    .badge-container {
    display: flex;
    justify-content: center;
    }
    .badge-container > div {
        margin: 0 10px; 
    }
}
#MainMenu {
    visibility: hidden;
    }
    footer {
        visibility:hidden;
}
.css-1d9fzic p {
        font-size:24px;
        color: #00A86B;
        font-weight: bold;
}
.css-1qg05tj {
    margin: 20px 0;
    padding: 20px;
    border: 2px solid #00A86B;
    border-radius: 10px;
    background-color: #190431;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  
     text-align: center; /* Centraliza horizontalmente */
        display: flex; /* Centraliza verticalmente */
        align-items: center; /* Centraliza verticalmente */
        justify-content: center; /* Centraliza verticalmente *
}
 .streamlit-expander {
            background-color: #0A0127;
            border: 2px solid #00A86B;
            border-radius: 10px; 
        }
        .streamlit-expanderHeader {
            color: #00A86B;
            font-size: 25px; /* Aumenta o tamanho da fonte do cabeçalho */
        

}
.css-1d9fzic p{
    font-size:25px;
}
</style>
'''