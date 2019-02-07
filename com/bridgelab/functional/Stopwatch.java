package com.bridgelab.functional;

import java.time.LocalTime;
import java.time.Period;

public class Stopwatch {
	
	LocalTime start,stop;
	public LocalTime start() {
		start = LocalTime.now();
		Period p = getPeriod()
	}
	
	public LocalTime stop() {
		stop = LocalTime.now();
		return (start-stop);
	}
}
