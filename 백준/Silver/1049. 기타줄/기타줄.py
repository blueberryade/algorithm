import sys
input = sys.stdin.readline
n,m = map(int,input().split())

package = []
single = []
for _ in range(m):
    a,b = map(int,input().split())
    package.append(a)
    single.append(b)

result = 0
package = min(package)
single = min(single)

if package > single*6:
    result+= n*single
else:
    result+=(n//6) * package
    if n%6 * single > package:
        result+=package
    else:
        result+=n%6*single

print(result)
