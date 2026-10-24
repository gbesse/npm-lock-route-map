import re
from .common import identifier

def package_name(x):
 if not isinstance(x,str)or not re.fullmatch(r'(?:@[A-Za-z0-9_.-]+/)?[A-Za-z0-9_.-]+',x)or any(v in ('.','..')for v in x.split('/')):raise ValueError('package_name')
 return x
def run(data):
 lock=data['lock'];include=data.get('include_development',False)
 if lock.get('lockfileVersion')!=3 or not isinstance(lock.get('packages'),dict)or len(lock['packages'])>5000 or not isinstance(include,bool):raise ValueError('lock_v3')
 packages=lock['packages']
 if''not in packages:raise ValueError('root')
 for path,p in packages.items():
  if not isinstance(path,str)or path.startswith(('/','\\'))or'\\'in path or any(v in ('.','..')for v in path.split('/'))or not isinstance(p,dict):raise ValueError('package_path')
 def resolve(path,name):
  parts=path.split('/')if path else[]
  for n in range(len(parts),-1,-1):
   if n and parts[n-1]=='node_modules':continue
   candidate='/'.join(parts[:n]+['node_modules',name])
   if candidate in packages:return candidate
  return None
 visited=set();todo=[''];edges=[]
 while todo:
  path=todo.pop(0)
  if path in visited:continue
  visited.add(path);node=packages[path]
  if node.get('link'):continue
  deps={k:('required',v)for k,v in node.get('dependencies',{}).items()}
  if path==''and include:deps.update({k:('development',v)for k,v in node.get('devDependencies',{}).items()if k not in deps})
  deps.update({k:('optional',v)for k,v in node.get('optionalDependencies',{}).items()})
  for name,(kind,requested)in sorted(deps.items()):
   package_name(name);target=resolve(path,name);linked=target is not None and bool(packages[target].get('link'));status='workspace_link_not_followed'if linked else'resolved_locked_path'if target is not None else'missing_optional'if kind=='optional'else'unresolved'
   edges.append({'from':path,'dependency':name,'kind':kind,'requested':requested,'to':target,'locked_version':packages[target].get('version')if target is not None else None,'status':status})
   if target is not None and not linked:todo.append(target)
 return {'edges':edges,'reachable_package_paths':sorted(visited),'unreachable_package_paths':sorted(set(packages)-visited),'model':'package_lock_v3_physical_node_modules_route_resolution_no_semver_registry_or_peer_solver'}
