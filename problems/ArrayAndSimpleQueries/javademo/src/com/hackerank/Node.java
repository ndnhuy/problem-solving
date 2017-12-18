package com.hackerank;

public class Node {
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
