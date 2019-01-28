public class Word{
    public String word;
    public String language;

    public Word(){
        word = "";
        language = "";
    }

    public void setWord(String newWord){
        word = newWord;
    }

    public void rusToEng(){
        language = "ru-en";
    }

    public void engToRus(){
        language = "en-ru";
    }
}