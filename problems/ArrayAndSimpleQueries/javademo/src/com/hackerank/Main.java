package com.hackerank;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {
    public static class Pair<T> {
        private T first;
        private T second;

        public Pair(T first, T second) {
            this.first = first;
            this.second = second;
        }

        public T getFirst() {
            return first;
        }

        public void setFirst(T first) {
            this.first = first;
        }

        public T getSecond() {
            return second;
        }

        public void setSecond(T second) {
            this.second = second;
        }
    }

    public static class Node {
        private Integer key;
        private Integer value;
        private Integer priority;
        private Node left;
        private Node right;
        private Integer size;

        public Node(Integer key, Integer value, Integer priority, Node left, Node right, Integer size) {
            this.key = key;
            this.value = value;
            this.priority = priority;
            this.left = left;
            this.right = right;
            this.size = size;
        }

        public Integer getKey() {
            return key;
        }

        public void setKey(Integer key) {
            this.key = key;
        }

        public Integer getValue() {
            return value;
        }

        public void setValue(Integer value) {
            this.value = value;
        }

        public Integer getPriority() {
            return priority;
        }

        public void setPriority(Integer priority) {
            this.priority = priority;
        }

        public Node getLeft() {
            return left;
        }

        public void setLeft(Node left) {
            this.left = left;
        }

        public Node getRight() {
            return right;
        }

        public void setRight(Node right) {
            this.right = right;
        }

        public Integer getSize() {
            return size;
        }

        public void setSize(Integer size) {
            this.size = size;
        }
    }

    public static class TreapTree {

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
            Pair<TreapTree> p2 = p1.getSecond().split(j - i);
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

    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader("D:\\projects\\sideprojects\\problem-solving\\problems\\ArrayAndSimpleQueries\\python\\input16.txt"));
        List<String> lines = reader.lines().collect(Collectors.toList());

        String[] s = lines.get(0).split(" ");
        int N = Integer.parseInt(s[0]);
        int M = Integer.parseInt(s[1]);

        TreapTree tree = new TreapTree();
        tree.fromArray(Stream.of(lines.get(1).split(" ")).map(Integer::parseInt).collect(Collectors.toList()));

        lines.stream().skip(2).map(queryStr -> queryStr.split(" ")).map(params -> Stream.of(params).map(Integer::parseInt).toArray(Integer[]::new))
                .forEach(params -> {
                    if (params[0] == 1) {
                        tree.moveToFront(params[1] - 1, params[2] - 1);
                    } else {
                        tree.moveToBack(params[1] - 1, params[2] - 1);
                    }
                });

        Integer[] result = tree.toArray();
        Integer k = result[0] - result[result.length - 1];
        k = k < 0 ? -k : k;

        System.out.println(k);

        System.out.println(Stream.of(result).map(Object::toString).collect(Collectors.joining(" ")));

        reader.close();
    }
}