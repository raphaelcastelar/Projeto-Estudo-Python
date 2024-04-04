package DAO;

import java.sql.PreparedStatement;
import java.sql.SQLException;

import conexao.conexao;
import entity.Usuario;

/**
 * usuarioDAO
 */
public class usuarioDAO {
    public void cadastrarUsuario(Usuario Usuario){
        String sql = "INSERT INTO USUARIO (NOME, LOGIN, SENHA, EMAIL) VALUES (?, ?, ?, ?)";
        PreparedStatement ps = null;

        try {
            ps = conexao.getConexao().prepareStatement(sql);
            ps.setString(1, Usuario.getNome());
            ps.setString(2, Usuario.getLogin());
            ps.setString(3, Usuario.getSenha());
            ps.setString(4, Usuario.getEmail());
            ps.execute();
            ps.close();
          
        
        
        } catch (SQLException e) {
            
            e.printStackTrace();
        }

    }
    
}