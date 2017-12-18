package com.hackerank;

import java.util.List;
import java.util.Random;

public class TreapTree {

    private Node root = null;
    private Random random = new Random();

    public TreapTree(Node root) {
        this.root = root;
    }

    public TreapTree() {
    }

    public Pair<TreapTree> split(Integer key) {
        Pair<Node> splitResult = this.split(this.root, key, 0);
        return new Pair<>(new TreapTree(splitResult.getFirst()), new TreapTree(splitResult.getSecond()));
    }

    public TreapTree merge(TreapTree rightTree) {
        this.root = this.merge(this.root, rightTree.root);
        return this;
    }

    public TreapTree fromArray(List<Integer> keys) {
        for (int i = 0; i < keys.size(); i++) {
            this.insert(i, keys.get(i));
        }
        return this;
    }

    public TreapTree moveToFront(int i, int j) {
        Pair<TreapTree> p1 = this.split(j);
        Pair<TreapTree> p2 = p1.getFirst().split(i - 1);
        TreapTree mergedTree = p2.getSecond().merge(p2.getFirst());
        this.root = mergedTree.merge(p1.getSecond()).root;
        return this;
    }

    public TreapTree moveToBack(int i, int j) {
        Pair<TreapTree> p1 = this.split(i - 1);
        Pair<TreapTree> p2 = p1.getSecond().split(j - 1);
        TreapTree mergedTree = p2.getSecond().merge(p2.getFirst());
        this.root = p1.getFirst().merge(mergedTree).root;
        return this;
    }

    public Integer[] toArray() {
        Integer[] a = new Integer[this.size(this.root)];
        this.populateArray(this.root, a, 0);
        return a;
    }

    private void populateArray(Node node, Integer[] a, int smallerNodeCount) {
        if (node == null) {
            return;
        }

        a[this.key(node, smallerNodeCount)] = node.getValue();
        this.populateArray(node.getLeft(), a, smallerNodeCount);
        this.populateArray(node.getRight(), a, smallerNodeCount + this.size(node.getLeft()) + 1);
    }

    public void insert(Integer key, Integer value) {
        Pair<Node> splitResult = this.split(this.root, key, 0);
        Node l = this.merge(splitResult.getFirst(), new Node(key, value, random.nextInt(Integer.MAX_VALUE), null, null, 1));
        Node r = splitResult.getSecond();
        this.root = this.merge(l, r);
    }

    private Pair<Node> split(Node node, Integer key, int smallerNodeCount) {
        if (node == null) {
            return new Pair(null, null);
        }

        if (key < this.key(node, smallerNodeCount)) {
            Pair<Node> splitResult = this.split(node.getLeft(), key, smallerNodeCount);
            node.setLeft(splitResult.getSecond());
            this.updateSize(splitResult.getFirst());
            this.updateSize(node);
            return new Pair<>(splitResult.getFirst(), node);
        }

        if (key >= this.key(node, smallerNodeCount)) {
            Pair<Node> splitResult = this.split(node.getRight(), key, smallerNodeCount + this.size(node.getLeft()) + 1);
            node.setRight(splitResult.getFirst());
            this.updateSize(node);
            this.updateSize(splitResult.getSecond());
            return new Pair<>(node, splitResult.getSecond());
        }

        return null;
    }

    private Node merge(Node leftRoot, Node rightRoot) {
        if (leftRoot == null) {
            return rightRoot;
        }

        if (rightRoot == null) {
            return leftRoot;
        }

        if (leftRoot.getPriority() <= rightRoot.getPriority()) {
            rightRoot.setLeft(this.merge(leftRoot, rightRoot.getLeft()));
            this.updateSize(rightRoot);
            return rightRoot;
        } else {
            leftRoot.setRight(this.merge(leftRoot.getRight(), rightRoot));
            this.updateSize(leftRoot);
            return leftRoot;
        }
    }

    private Integer key(Node node, int smallerNodeCount) {
        return this.size(node.getLeft()) + smallerNodeCount;
    }

    private Integer size(Node node) {
        return node == null ? 0 : node.getSize();
    }

    private void updateSize(Node node) {
        if (node != null) {
            node.setSize(1 + this.size(node.getLeft()) + this.size(node.getRight()));
        }
    }
}