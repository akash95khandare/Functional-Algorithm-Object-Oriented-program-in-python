package com.bridgelab.functional;

public class StringReplace {
	
	String str= "Hello <<UserName>>, How are you?";
	
	public String getReplaceStr(String s) {
		try {
			return str.replace("<<UserName>>", s);
		} catch(Exception e) {
			e.printStackTrace();
		}
		return "String not change...";
	}
}
