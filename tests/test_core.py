import unittest
from npm_lock_route_map import run
class Tests(unittest.TestCase):
 def test_nested_shadow_and_root_hoist(self):
  lock={'lockfileVersion':3,'packages':{'':{'dependencies':{'a':'1','b':'1'}},'node_modules/a':{'version':'1','dependencies':{'b':'2','c':'1'}},'node_modules/b':{'version':'1'},'node_modules/a/node_modules/b':{'version':'2'},'node_modules/c':{'version':'1'}}};edges=run({'lock':lock})['edges'];routes={(e['from'],e['dependency']):e['to']for e in edges};self.assertEqual(routes['node_modules/a','b'],'node_modules/a/node_modules/b');self.assertEqual(routes['node_modules/a','c'],'node_modules/c')
 def test_scoped_package_and_workspace_link_are_explicit(self):
  lock={'lockfileVersion':3,'packages':{'':{'dependencies':{'@scope/a':'1','workspace':'file:x'}},'node_modules/@scope/a':{'version':'1'},'node_modules/workspace':{'link':True,'resolved':'packages/workspace'}}};r=run({'lock':lock});self.assertEqual(r['edges'][0]['to'],'node_modules/@scope/a');self.assertEqual(r['edges'][1]['status'],'workspace_link_not_followed')
 def test_optional_missing_and_dev_flag(self):
  lock={'lockfileVersion':3,'packages':{'':{'optionalDependencies':{'os-only':'1'},'devDependencies':{'dev':'1'}},'node_modules/dev':{'version':'1'}}};self.assertEqual(len(run({'lock':lock})['edges']),1);self.assertEqual(len(run({'lock':lock,'include_development':True})['edges']),2)
 def test_no_semver_claim_for_existing_locked_path(self):
  lock={'lockfileVersion':3,'packages':{'':{'dependencies':{'x':'999'}},'node_modules/x':{'version':'1'}}};self.assertEqual(run({'lock':lock})['edges'][0]['status'],'resolved_locked_path')
