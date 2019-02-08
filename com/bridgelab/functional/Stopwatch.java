package com.bridgelab.functional;


public class Stopwatch {
	
	Long start,stop;
	public void start() {
		start = System.currentTimeMillis();
	}
	
	public Long elapseTime() {
		stop = System.currentTimeMillis();
		return ((stop-start)/1000);
	}
}
