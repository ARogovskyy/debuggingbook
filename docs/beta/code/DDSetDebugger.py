#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This material is part of "The Debugging Book".
# Web site: https://www.debuggingbook.org/html/DDSetDebugger.html
# Last change: 2021-01-31 20:51:33+01:00
#
#
# Copyright (c) 2021 CISPA Helmholtz Center for Information Security
# Copyright (c) 2018-2020 Saarland University, authors, and contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


# # Generalizing Failure Circumstances

if __name__ == "__main__":
    print('# Generalizing Failure Circumstances')




if __name__ == "__main__":
    from bookutils import YouTubeVideo
    # YouTubeVideo("w4u5gCgPlmg")


if __name__ == "__main__":
    # We use the same fixed seed as the notebook to ensure consistency
    import random
    random.seed(2001)


if __package__ is None or __package__ == "":
    import DeltaDebugger
else:
    from . import DeltaDebugger


# ## Synopsis

if __name__ == "__main__":
    print('\n## Synopsis')




# ## A Failing Program

if __name__ == "__main__":
    print('\n## A Failing Program')




def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c

    # postcondition
    assert '<' not in out and '>' not in out

    return out

if __name__ == "__main__":
    remove_html_markup("Be <em>quiet</em>, he said")


BAD_INPUT = '<foo>"bar</foo>'

if __package__ is None or __package__ == "":
    from ExpectError import ExpectError
else:
    from .ExpectError import ExpectError


if __name__ == "__main__":
    with ExpectError(AssertionError):
        remove_html_markup(BAD_INPUT)


if __package__ is None or __package__ == "":
    from bookutils import quiz
else:
    from .bookutils import quiz


if __name__ == "__main__":
    quiz("If `s = '<foo>\"bar</foo>'` (i.e., `BAD_INPUT`), "
         "what is the value of `out` such that the assertion fails?",
        [
            '`bar`',
            '`bar</foo>`',
            '`"bar</foo>`',
            '`<foo>"bar</foo>`',
        ], '9999999 // 4999999')


# ## Grammars

if __name__ == "__main__":
    print('\n## Grammars')




import fuzzingbook

DIGIT_GRAMMAR = {
    "<start>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

EXPR_GRAMMAR = {
    "<start>":
        ["<expr>"],

    "<expr>":
        ["<term> + <expr>", "<term> - <expr>", "<term>"],

    "<term>":
        ["<factor> * <term>", "<factor> / <term>", "<factor>"],

    "<factor>":
        ["+<factor>",
         "-<factor>",
         "(<expr>)",
         "<integer>.<integer>",
         "<integer>"],

    "<integer>":
        ["<digit><integer>", "<digit>"],

    "<digit>":
        ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

from fuzzingbook.GrammarFuzzer import GrammarFuzzer

if __name__ == "__main__":
    simple_expr_fuzzer = GrammarFuzzer(EXPR_GRAMMAR)


if __name__ == "__main__":
    for i in range(10):
        fuzz_expr = simple_expr_fuzzer.fuzz()
        print(fuzz_expr)


SIMPLE_HTML_GRAMMAR = {
    "<start>":
        ["<html>"],

    "<html>":
        ["<plain-text>", "<tagged-text>"],
}

import string

SIMPLE_HTML_GRAMMAR.update({
    "<plain-text>":
        ["", "<plain-char><plain-text>"],

    "<plain-char>":
        ["<letter>", "<digit>", "<other>", "<whitespace>"],

    "<letter>": list(string.ascii_letters),
    "<digit>": list(string.digits),
    "<other>": list(string.punctuation.replace('<', '').replace('>', '')),
    "<whitespace>": list(string.whitespace)
})

SIMPLE_HTML_GRAMMAR.update({
    "<tagged-text>":
        ["<opening-tag><html><closing-tag>",
         "<self-closing-tag>",
         "<opening-tag>"],
})

SIMPLE_HTML_GRAMMAR.update({
    "<opening-tag>":
        ["<lt><id><gt>",
         "<lt><id><attrs><gt>"],

    "<lt>": [ "<" ],
    "<gt>": [ ">" ],

    "<id>":
        ["<letter>", "<id><letter>", "<id><digit>"],

    "<closing-tag>":
        ["<lt>/<id><gt>"],

    "<self-closing-tag>":
        ["<lt><id><attrs>/<gt>"],
})

SIMPLE_HTML_GRAMMAR.update({
    "<attrs>":
        ["<attr>", "<attr><attrs>" ],

    "<attr>":
        [" <id>='<plain-text>'",
         ' <id>="<plain-text>"'],
})

if __name__ == "__main__":
    simple_html_fuzzer = GrammarFuzzer(SIMPLE_HTML_GRAMMAR)


if __name__ == "__main__":
    for i in range(10):
        fuzz_html = simple_html_fuzzer.fuzz()
        print(repr(fuzz_html))


# ## Derivation Trees

if __name__ == "__main__":
    print('\n## Derivation Trees')




if __name__ == "__main__":
    fuzz_html


from fuzzingbook.GrammarFuzzer import display_tree

def display_tree(tree):
    def graph_attr(dot):
        dot.attr('node', shape='plain')
        dot.attr('node', fontname="'Fira Mono', 'Source Code Pro', 'Courier', monospace")
        
    def node_attr(dot, nid, symbol, ann):
        fuzzingbook.GrammarFuzzer.default_node_attr(dot, nid, symbol, ann)
        if symbol.startswith('<'):
            dot.node(repr(nid), fontcolor='#0060a0')
        else:
            dot.node(repr(nid), fontcolor='#00a060')
        dot.node(repr(nid), scale='2')
    
    return fuzzingbook.GrammarFuzzer.display_tree(tree,
        node_attr=node_attr,
        graph_attr=graph_attr)

if __name__ == "__main__":
    display_tree(simple_html_fuzzer.derivation_tree)


import pprint

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(depth=7)
    pp.pprint(simple_html_fuzzer.derivation_tree)


# ## Parsing

if __name__ == "__main__":
    print('\n## Parsing')




from fuzzingbook.Parser import EarleyParser  # minor dependency

if __name__ == "__main__":
    simple_html_parser = EarleyParser(SIMPLE_HTML_GRAMMAR)


if __name__ == "__main__":
    bad_input_tree = list(simple_html_parser.parse(BAD_INPUT))[0]


if __name__ == "__main__":
    display_tree(bad_input_tree)


from fuzzingbook.GrammarFuzzer import tree_to_string, all_terminals

if __name__ == "__main__":
    tree_to_string(bad_input_tree)


if __name__ == "__main__":
    assert tree_to_string(bad_input_tree) == BAD_INPUT


# ## Mutating the Tree

if __name__ == "__main__":
    print('\n## Mutating the Tree')




from fuzzingbook.Grammars import is_valid_grammar

class TreeMutator:
    """Grammar-based mutations of derivation trees."""
    
    def __init__(self, grammar, tree, fuzzer=None, log=False):
        """Constructor. 
        `grammar` is the underlying grammar; 
        `tree` is the tree to work on.
        `fuzzer` is the grammar fuzzer to use (default: `GrammarFuzzer`)
        """

        assert is_valid_grammar(grammar)
        self.grammar = grammar
        self.tree = tree
        self.log = log
        
        if fuzzer is None:
            fuzzer = GrammarFuzzer(grammar)
        self.fuzzer = fuzzer

# ### Referencing Subtrees

if __name__ == "__main__":
    print('\n### Referencing Subtrees')




class TreeMutator(TreeMutator):
    def get_subtree(self, path, tree=None):
        """Access a subtree based on `path` (a list of children numbers)"""
        if tree is None:
            tree = self.tree

        node, children = tree  # FIXME: should be symbol

        if not path:
            return tree

        return self.get_subtree(path[1:], children[path[0]])

def bad_input_tree_mutator():
    return TreeMutator(SIMPLE_HTML_GRAMMAR, bad_input_tree, log=2)    

if __name__ == "__main__":
    plain_text_subtree = bad_input_tree_mutator().get_subtree([0, 0, 1, 0])
    pp.pprint(plain_text_subtree)


if __name__ == "__main__":
    tree_to_string(plain_text_subtree)


def primes_generator():
    # Adapted from https://www.python.org/ftp/python/doc/nluug-paper.ps
    primes = [2]
    yield 2
    i = 3
    while True:
        for p in primes:
            if i % p == 0 or p * p > i:
                break

        if i % p != 0:
            primes.append(i)
            yield i

        i += 2

if __name__ == "__main__":
    prime_numbers = primes_generator()


if __name__ == "__main__":
    quiz("In `bad_input_tree`, what is "
         " the subtree at the path `[0, 0, 2, 1]` as string?", 
        [
            f"`{tree_to_string(bad_input_tree_mutator().get_subtree([0, 0, 2, 0]))}`",
            f"`{tree_to_string(bad_input_tree_mutator().get_subtree([0, 0, 2, 1]))}`",
            f"`{tree_to_string(bad_input_tree_mutator().get_subtree([0, 0, 2]))}`",
            f"`{tree_to_string(bad_input_tree_mutator().get_subtree([0, 0, 0]))}`",
        ], 'next(prime_numbers)', globals()
        )


# ### Creating new Subtrees

if __name__ == "__main__":
    print('\n### Creating new Subtrees')




class TreeMutator(TreeMutator):
    def new_tree(self, start_symbol):
        """Create a new subtree for <start_symbol>."""

        if self.log >= 2:
            print(f"Creating new tree for {start_symbol}")
            
        tree = (start_symbol, None)
        return self.fuzzer.expand_tree(tree)

if __name__ == "__main__":
    plain_text_tree = bad_input_tree_mutator().new_tree('<plain-text>')
    display_tree(plain_text_tree)


if __name__ == "__main__":
    tree_to_string(plain_text_tree)


# ### Mutating the Tree

if __name__ == "__main__":
    print('\n### Mutating the Tree')




class TreeMutator(TreeMutator):
    def mutate(self, path, tree=None):
        """Return a new tree mutated at `path`"""
        if tree is None:
            tree = self.tree

        node, children = tree

        if not path:
            return self.new_tree(node)

        head = path[0]
        new_children = (children[:head] +
                        [self.mutate(path[1:], children[head])] +
                        children[head + 1:])
        return node, new_children

if __name__ == "__main__":
    mutated_tree = bad_input_tree_mutator().mutate([0, 0, 1, 0])
    display_tree(mutated_tree)


if __name__ == "__main__":
    tree_to_string(mutated_tree)


# ## Generalizing Trees

if __name__ == "__main__":
    print('\n## Generalizing Trees')




class TreeGeneralizer(TreeMutator):
    """Determine which parts of a derivation tree can be generalized."""
    
    def __init__(self, grammar, tree, test,
                 max_tries_for_generalization=10,
                 **kwargs):
        """Constructor. `grammar` and `tree` are as in `TreeMutator`.
        `test` is a function taking a string that either
          * raises an exception, indicating test failure;
          * or not, indicating test success.
        `max_tries_for_generalization` is the number of times
          an instantiation has to fail before it is generalized."""
        
        super().__init__(grammar, tree, **kwargs)
        self.test = test
        self.max_tries_for_generalization = max_tries_for_generalization

class TreeGeneralizer(TreeGeneralizer):
    def test_tree(self, tree):
        """Return True if testing `tree` passes, else False"""
        s = tree_to_string(tree)
        if self.log:
            print(f"Testing {repr(s)}...", end="")
        try:
            self.test(s)
        except Exception as exc:
            if self.log:
                print(f"FAIL ({type(exc).__name__})")
            ret = False
        else:
            if self.log:
                print(f"PASS")
            ret = True

        return ret

# ### Testing for Generalization

if __name__ == "__main__":
    print('\n### Testing for Generalization')




class TreeGeneralizer(TreeGeneralizer):
    def can_generalize(self, path, tree=None):
        """Return True if the subtree at `path` can be generalized."""
        for i in range(self.max_tries_for_generalization):
            mutated_tree = self.mutate(path, tree)
            if self.test_tree(mutated_tree):
                # Failure no longer occurs; cannot abstract
                return False
            
        return True

def bad_input_tree_generalizer(**kwargs):
    return TreeGeneralizer(SIMPLE_HTML_GRAMMAR, bad_input_tree,
        remove_html_markup, **kwargs)    

if __name__ == "__main__":
    bad_input_tree_generalizer(log=True).can_generalize([0])


if __name__ == "__main__":
    bad_input_tree_generalizer(log=True).can_generalize([0, 0, 1, 0])


if __name__ == "__main__":
    bad_input_tree_generalizer(log=True).can_generalize([0, 0, 2])


if __name__ == "__main__":
    quiz("Is this also true for `<opening-tag>`?",
         [
             "Yes",
             "No"
         ], '("No" == "No") + ("No" is "No")')


if __name__ == "__main__":
    bad_input_tree_generalizer().can_generalize([0, 0, 0])


if __name__ == "__main__":
    bad_input_tree_generalizer(max_tries_for_generalization=100).can_generalize([0, 0, 0])


# ### Generalizable Paths

if __name__ == "__main__":
    print('\n### Generalizable Paths')




class TreeGeneralizer(TreeGeneralizer):
    def find_paths(self, predicate, path=None, tree=None):
        """Return a list of all paths for which `predicate` holds.
        `predicate` is a function `predicate`(`path`, `tree`), where
         `path` denotes a subtree in `tree`. If `predicate()` returns
         True, `path` is included in the returned list."""

        if path is None:
            path = []
        if tree is None:
            tree = self.tree
            
        node, children = self.get_subtree(path)

        if predicate(path, tree):
            if self.log:
                node, children = self.get_subtree(path)
            return [path]

        paths = []
        for i, child in enumerate(children):
            child_node, _ = child
            if child_node in self.grammar:
                paths += self.find_paths(predicate, path + [i])

        return paths        
    
    def generalizable_paths(self):
        """Return a list of all paths whose subtrees can be generalized."""
        return self.find_paths(self.can_generalize)

if __name__ == "__main__":
    bad_input_generalizable_paths = \
        bad_input_tree_generalizer().generalizable_paths()
    bad_input_generalizable_paths


class TreeGeneralizer(TreeGeneralizer):
    def generalize_path(self, path, tree=None):
        """Return a copy of the tree in which the subtree at `path`
        is generalized (= replaced by a nonterminal without children)"""
        if tree is None:
            tree = self.tree

        symbol, children = tree

        if not path:
            return symbol, None  # Nonterminal without children

        head = path[0]
        new_children = (children[:head] +
                        [self.generalize_path(path[1:], children[head])] +
                        children[head + 1:])
        return symbol, new_children

if __name__ == "__main__":
    all_terminals(bad_input_tree_generalizer().generalize_path([0, 0, 0]))


class TreeGeneralizer(TreeGeneralizer):
    def generalize(self):
        """Returns a copy of the tree in which all generalizable subtrees
        are generalized (= replaced by nonterminals without children)"""
        tree = self.tree
        for path in self.generalizable_paths():
            tree = self.generalize_path(path, tree)
            
        return tree

if __name__ == "__main__":
    abstract_failure_inducing_input = bad_input_tree_generalizer().generalize()


if __name__ == "__main__":
    all_terminals(abstract_failure_inducing_input)


# ## Fuzzing with Patterns

if __name__ == "__main__":
    print('\n## Fuzzing with Patterns')




import copy

class TreeGeneralizer(TreeGeneralizer):
    def fuzz_tree(self, tree):
        """Return an instantiated copy of `tree`."""
        tree = copy.deepcopy(tree)
        return self.fuzzer.expand_tree(tree)

if __name__ == "__main__":
    bitg = bad_input_tree_generalizer()
    for i in range(10):
        print(all_terminals(bitg.fuzz_tree(abstract_failure_inducing_input)))


if __name__ == "__main__":
    successes = 0
    failures = 0
    trials = 1000

    for i in range(trials):
        test_input = all_terminals(
            bitg.fuzz_tree(abstract_failure_inducing_input))
        try:
            remove_html_markup(test_input)
        except AssertionError:
            successes += 1
        else:
            failures += 1


if __name__ == "__main__":
    successes, failures


if __name__ == "__main__":
    failures / 1000


# ## Putting it all Together

if __name__ == "__main__":
    print('\n## Putting it all Together')




# ### Constructor

if __name__ == "__main__":
    print('\n### Constructor')




if __package__ is None or __package__ == "":
    from DeltaDebugger import CallCollector, is_reducible
else:
    from .DeltaDebugger import CallCollector, is_reducible


import copy

class DDSetDebugger(CallCollector):
    """Debugger implementing the DDSET algorithm
    for abstracting failure-inducing inputs"""
    
    def __init__(self, grammar, 
                 generalizer_class=TreeGeneralizer,
                 parser=None,
                 **kwargs):
        """Constructor.
        `grammar` is an input grammar in fuzzingbook format.
        `generalizer_class` is the tree generalizer class to use
          (default: TreeGeneralizer)
        `parser` is the parser to use (default: `EarleyParser(grammar)`).

        All other args are passed to the tree generalizer, notably
        `fuzzer` is the fuzzer to use (default: `GrammarFuzzer`)
        `log` enables debugging output if set to True.
        """
        super().__init__()
        self.grammar = grammar
        assert is_valid_grammar(grammar)

        self.generalizer_class = generalizer_class

        if parser is None:
            parser = EarleyParser(grammar)
        self.parser = parser
        self.kwargs = kwargs
        
        # These save state for further fuzz() calls
        self.generalized_trees = None
        self.generalized_args = None
        self.generalizers = None

# ### Generalizing Arguments

if __name__ == "__main__":
    print('\n### Generalizing Arguments')




class DDSetDebugger(DDSetDebugger):
    def generalize(self):
        """Generalize arguments seen. For each function argument,
        produce an abstract failure-inducing input that characterizes
        the set of inputs for which the function fails."""
        if self.generalized_args is not None:
            return self.generalized_args

        self.generalized_args = copy.deepcopy(self.args())
        self.generalized_trees = {}
        self.generalizers = {}

        for arg in self.args():
            def test(value):
                return self.call({arg: value})

            value = self.args()[arg]
            if isinstance(value, str):
                tree = list(self.parser.parse(value))[0]
                gen = self.generalizer_class(self.grammar, tree, test, 
                                             **self.kwargs)
                generalized_tree = gen.generalize()
                
                self.generalizers[arg] = gen
                self.generalized_trees[arg] = generalized_tree
                self.generalized_args[arg] = all_terminals(generalized_tree)

        return self.generalized_args

class DDSetDebugger(DDSetDebugger):
    def __repr__(self):
        """Return a string representation of the generalized call."""
        return self.format_call(self.generalize())

if __name__ == "__main__":
    with DDSetDebugger(SIMPLE_HTML_GRAMMAR) as dd:
        remove_html_markup(BAD_INPUT)
    dd


# ### Fuzzing

if __name__ == "__main__":
    print('\n### Fuzzing')




class DDSetDebugger(DDSetDebugger):
    def fuzz_args(self):
        """Return arguments randomly instantiated
        from the abstract failure-inducing pattern."""
        if self.generalized_trees is None:
            self.generalize()
            
        args = copy.deepcopy(self.generalized_args)
        for arg in args:
            def test(value):
                return self.call({arg: value})

            if arg not in self.generalized_trees:
                continue

            tree = self.generalized_trees[arg]
            gen = self.generalizers[arg]
            instantiated_tree = gen.fuzz_tree(tree)
            args[arg] = all_terminals(instantiated_tree)
            
        return args
    
    def fuzz(self):
        """Return a call with arguments randomly instantiated
        from the abstract failure-inducing pattern."""
        return self.format_call(self.fuzz_args())

if __name__ == "__main__":
    with DDSetDebugger(SIMPLE_HTML_GRAMMAR) as dd:
        remove_html_markup(BAD_INPUT)


if __name__ == "__main__":
    dd.fuzz()


if __name__ == "__main__":
    dd.fuzz()


if __name__ == "__main__":
    dd.fuzz()


if __name__ == "__main__":
    with ExpectError(AssertionError):
        eval(dd.fuzz())


# ## More Examples

if __name__ == "__main__":
    print('\n## More Examples')




# ### Square Root

if __name__ == "__main__":
    print('\n### Square Root')




if __package__ is None or __package__ == "":
    from Assertions import square_root  # minor dependency
else:
    from .Assertions import square_root  # minor dependency


if __name__ == "__main__":
    with ExpectError(AssertionError):
        square_root(-1)


INT_GRAMMAR = {
    "<start>":
        ["<int>"],

    "<int>":
        ["<positive-int>", "-<positive-int>"],

    "<positive-int>":
        ["<digit>", "<nonzero-digit><positive-int>"],

    "<nonzero-digit>": list("123456789"),
    
    "<digit>": list(string.digits),
}

def square_root_test(s):
    return square_root(int(s))

if __name__ == "__main__":
    with DDSetDebugger(INT_GRAMMAR, log=True) as dd_square_root:
        square_root_test("-1")


if __name__ == "__main__":
    dd_square_root


# ### Middle

if __name__ == "__main__":
    print('\n### Middle')




if __package__ is None or __package__ == "":
    from StatisticalDebugger import middle  # minor dependency
else:
    from .StatisticalDebugger import middle  # minor dependency


def middle_test(s):
    x, y, z = eval(s)
    assert middle(x, y, z) == sorted([x, y, z])[1]

XYZ_GRAMMAR = {
    "<start>":
        ["<int>, <int>, <int>"],

    "<int>":
        ["<positive-int>", "-<positive-int>"],

    "<positive-int>":
        ["<digit>", "<nonzero-digit><positive-int>"],

    "<nonzero-digit>": list("123456789"),
    
    "<digit>": list(string.digits),
}

if __name__ == "__main__":
    with ExpectError(AssertionError):
        middle_test("2, 1, 3")


if __name__ == "__main__":
    with DDSetDebugger(XYZ_GRAMMAR, log=True) as dd_middle:
        middle_test("2, 1, 3")


if __name__ == "__main__":
    dd_middle


# ## Synopsis

if __name__ == "__main__":
    print('\n## Synopsis')




if __name__ == "__main__":
    with DDSetDebugger(SIMPLE_HTML_GRAMMAR) as dd:
        remove_html_markup('<foo>"bar</foo>')
    dd


if __name__ == "__main__":
    dd.generalize()


if __name__ == "__main__":
    for i in range(10):
        print(dd.fuzz())


if __package__ is None or __package__ == "":
    from ClassDiagram import display_class_hierarchy
else:
    from .ClassDiagram import display_class_hierarchy


if __name__ == "__main__":
    display_class_hierarchy([DDSetDebugger, TreeGeneralizer],
                            public_methods=[
                                CallCollector.__init__,
                                CallCollector.__enter__,
                                CallCollector.__exit__,
                                CallCollector.function,
                                CallCollector.args,
                                CallCollector.exception,
                                CallCollector.call,
                                DDSetDebugger.__init__,
                                DDSetDebugger.__repr__,
                                DDSetDebugger.fuzz,
                                DDSetDebugger.fuzz_args,
                                DDSetDebugger.generalize,
                            ], project='debuggingbook')


# ## Lessons Learned

if __name__ == "__main__":
    print('\n## Lessons Learned')




# ## Next Steps

if __name__ == "__main__":
    print('\n## Next Steps')




# ## Background

if __name__ == "__main__":
    print('\n## Background')




# ## Exercises

if __name__ == "__main__":
    print('\n## Exercises')




# ### Exercise 1: Generalization and Specialization

if __name__ == "__main__":
    print('\n### Exercise 1: Generalization and Specialization')




if __name__ == "__main__":
    all_terminals(abstract_failure_inducing_input)


if __name__ == "__main__":
    more_precise_bitg = \
        bad_input_tree_generalizer(max_tries_for_generalization=100)

    more_precise_abstract_failure_inducing_input = \
        more_precise_bitg.generalize()


if __name__ == "__main__":
    all_terminals(more_precise_abstract_failure_inducing_input)


if __name__ == "__main__":
    successes = 0
    failures = 0
    trials = 1000

    for i in range(trials):
        test_input = all_terminals(
            more_precise_bitg.fuzz_tree(
                more_precise_abstract_failure_inducing_input))
        try:
            remove_html_markup(test_input)
        except AssertionError:
            successes += 1
        else:
            failures += 1


if __name__ == "__main__":
    successes, failures


if __name__ == "__main__":
    failures / 1000


# ### Exercise 2: Hierarchical Delta Debugging

if __name__ == "__main__":
    print('\n### Exercise 2: Hierarchical Delta Debugging')




if __package__ is None or __package__ == "":
    from DeltaDebugger import DeltaDebugger
else:
    from .DeltaDebugger import DeltaDebugger


import copy

if __name__ == "__main__":
    from IPython.display import display


class TreeHDDReducer(TreeGeneralizer):
    def _reduce(self, path, tree):
        """This is HDD"""

        node, children = self.get_subtree(path, tree)
            
        if len(path) >= 1:
            parent, parent_children = self.get_subtree(path[:-1], tree)
 
            assert parent_children[path[-1]] == (node, children)

            def test_children(children):
                parent_children[path[-1]] = (node, children)
                s = tree_to_string(tree)
                self.test(s)

            with DeltaDebugger() as dd:
                test_children(children)
            
            # display(display_tree(tree))

            children = dd.min_args()['children']
            parent_children[path[-1]] = (node, children)
        
        for i, child in enumerate(children):
            self._reduce(path + [i], tree)
            
        return tree

    def reduce(self):
        return self._reduce([], self.tree)

def bad_input_tree_hdd_reducer():
    return TreeHDDReducer(SIMPLE_HTML_GRAMMAR, copy.deepcopy(bad_input_tree),
                       remove_html_markup, log=True)    

if __name__ == "__main__":
    all_terminals(bad_input_tree_hdd_reducer().reduce())


# ## Exercise 3: Reducing Trees

if __name__ == "__main__":
    print('\n## Exercise 3: Reducing Trees')




class TreeReducer(TreeGeneralizer):
    def new_min_tree(self, start_symbol):
        if self.log >= 2:
            print(f"Creating new minimal tree for {start_symbol}")

        fuzzer = GrammarFuzzer(self.grammar, start_symbol=start_symbol,
                               min_nonterminals=0,
                               max_nonterminals=0)
        fuzzer.fuzz()
        return fuzzer.derivation_tree

def bad_input_tree_reducer():
    return TreeReducer(SIMPLE_HTML_GRAMMAR, bad_input_tree,
                       remove_html_markup, log=2)    

if __name__ == "__main__":
    tree_to_string(bad_input_tree_reducer().new_min_tree('<start>'))


class TreeReducer(TreeReducer):
    def reduce_path(self, path, tree=None):
        if tree is None:
            tree = self.tree

        node, children = tree

        if not path:
            return self.new_min_tree(node)

        head = path[0]
        new_children = (children[:head] +
                        [self.reduce_path(path[1:], children[head])] +
                        children[head + 1:])
        return node, new_children

if __name__ == "__main__":
    tree_to_string(bad_input_tree_reducer().reduce_path([0, 0, 1, 0]))


class TreeReducer(TreeReducer):
    def can_reduce(self, path, tree=None):
        reduced_tree = self.reduce_path(path, tree)
        if self.test_tree(reduced_tree):
            # Failure no longer occurs; cannot reduce
            return False

        return True

class TreeReducer(TreeReducer):
    def reducible_paths(self):
        return self.find_paths(self.can_reduce)

if __name__ == "__main__":
    bad_input_tree_reducer().reducible_paths()


class TreeReducer(TreeReducer):
    def reduce(self):
        tree = self.tree
        for path in self.reducible_paths():
            tree = self.reduce_path(path, tree)
            
        return tree

if __name__ == "__main__":
    all_terminals(bad_input_tree_reducer().reduce())
