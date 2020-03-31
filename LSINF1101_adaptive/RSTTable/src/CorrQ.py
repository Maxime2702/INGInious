#!/usr/bin/python3
# -*- coding: utf-8 -*-


def table(filename_in,filename_out,width):
	file_in = open ( filename_in, "r" )
	file_out = open ( filename_out, "w")
	file_out.write ( "+-" + "-" * width + "-+\n" )
	for line in file_in:
		file_out.write ( "| {1:<{0}} |\n".format ( width, line[:width].rstrip ()) )
	file_out.write ( "+-" + "-" * width + "-+" )
	file_in.close ()
	file_out.close ()
