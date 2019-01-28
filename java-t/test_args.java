import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

import com.sun.corba.se.impl.ior.ByteBuffer;
import com.sun.net.ssl.HttpsURLConnection;

import sun.java2d.pipe.BufferedBufImgOps;

public class test_args {
    public static void main(String[] args) throws IOException{
        Word word = new Word();
        if (args.length < 1){
            System.out.print("Enter the word to translate to russian: ");
            Scanner input = new Scanner(System.in);
            String newWord = input.nextLine();
            word.setWord(newWord);
            word.engToRus();
            transtate(word);
        } else {
            if (args.length == 1){
                word.setWord(args[0]);
                word.engToRus();
                transtate(word);
            }
            else{
                switch (args[0]){
                // language pull might be updated by another "case" and adding another method to of the Word class
                //TODO: scallable choose of the language
                    case "ru":
                        word.setWord(args[1]);
                        word.engToRus();
                        transtate(word);
                        break;
                    case "en":
                        word.setWord(args[1]);
                        word.rusToEng();
                        transtate(word);
                        break;
                    default:
                        System.out.println("use a language abbreviation (\"en\" or \"ru\") as a 1st argument \nto translate a 2nd argument word");
                        break;
                }
            }
        }
    }

    public static void transtate(Word word){
        HttpURLConnection connection = null; 
        try{
            String targetURL = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=" + APIKey.KEY;
            URL url = new URL(targetURL);

            connection =(HttpURLConnection) url.openConnection();

            connection.setRequestMethod("POST");
            connection.setDoOutput(true);

            //sending request
            DataOutputStream dataOutputStream = new DataOutputStream(connection.getOutputStream());
            dataOutputStream.writeBytes("text=" + URLEncoder.encode(word.word, "UTF-8") + "&lang=" + word.language);

            //listening for the response
            InputStream response = connection.getInputStream();
            String json = new Scanner(response).nextLine();

            // result in response represents as a list
            int start = json.indexOf("[");
            int finish = json.indexOf("]");
            String translated;

            //TODO: automatic OS check
            //This realisation is for the Windows OS
            translated = new String(json.substring(start+2, finish-1).getBytes("windows-1251"), Charset.forName("UTF-8"));

            //This realistaion is for the UNIX systems
            //translated = new String(json.substring(start+2, finish-1), Charset.forName("UTF-8"));

            System.out.println(translated);

        } catch(Exception e){
            e.printStackTrace();

        } finally {
            if (connection != null){
                connection.disconnect();
            }
            System.out.println("\n0");

        }
    }
}

