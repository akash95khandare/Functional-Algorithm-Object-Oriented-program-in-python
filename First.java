import java.io.BufferedReader;
import java.io.InputStreamReader;

class First
{
	public static String str= "Hello <<UserName>> How are you?";
	StringBuffer modifiedStr= new StringBuffer(str);
	public void replaceName(){
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Enter Name :");
		try{
		System.out.println(str.replace("<<UserName>>",br.readLine()));
		} catch(Exception e){
			e.printStackTrace();
		}
	}

	public void display(){
		System.out.println("String is : "+modifiedStr);
	}

	public static void main(String args[]){
		First f=new First();
		f.replaceName();
		f.display();
	}
}