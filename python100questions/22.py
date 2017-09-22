for a in ['x','y','z']:
	for b in ['x','y','z']:
		for c in ['x','y','z']:
			if (a!=b)and(a!=c)and(b!=c) and a!='x' and c!='x' and c!='z':
				print("a和{}比，b和{}比，c和{}比".format(a,b,c))
