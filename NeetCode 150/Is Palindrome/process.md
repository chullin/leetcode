## Is Palindrome
Given a string `s`, return `true` if it is a palindrome, otherwise return `false`.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

```python
Input: s = "Was it a car or a cat I saw?"

Output: True
```
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
```python
Input: s = "tab a cat"

Output: False
```
Explanation: "tabacat" is not a palindrome.

Constraints:

* `1 <= s.length <= 1000`
* `s` is made up of only printable ASCII characters.


# 結果
### Wrong Answer

Passed test cases: 22 / 31
Last executed test case

```python
Input:
s="0P"

Your Output:
True

Expected output:
False
```