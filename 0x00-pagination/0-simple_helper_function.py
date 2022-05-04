#!/usr/bin/env python3
""" A helper function for getting page number and size"""

def index_range(page, page_size):
	"""A function that takes in a page 
	 -page no
	 -page size
	 returns a tuple.
	"""
	if page and page_size:
		st_index = (page - 1) * page_size
		end = st_index + page_size
	tup = (st_index, end)
	return tup
