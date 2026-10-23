class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        st, a, p = [], [0]*n, 0
        for i in logs:
            fi, e, t = i.split(":")
            fi, t = int(fi), int(t)
            if e=="start":
                if st: a[st[-1]]+=t-p
                st.append(fi)
                p=t
            else:
                a[st.pop()]+=t-p+1
                p=t+1
        return a