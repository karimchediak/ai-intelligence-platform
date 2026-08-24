def confidence(result):
 n=len(result.get('plan',[])); return round(min(.99,.55+n*.08),2)
