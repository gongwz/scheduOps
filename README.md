# scheduOps 异步

<a name="ScheduOps"></a>
### ScheduOps

<br />![](https://cdn.nlark.com/yuque/0/2020/svg/486920/1594719475561-3f40081b-f28d-4050-906f-ba9fd51f76ad.svg#align=left&display=inline&height=20&margin=%5Bobject%20Object%5D&originHeight=20&originWidth=98&size=0&status=done&style=none&width=98)[![](https://cdn.nlark.com/yuque/0/2020/svg/486920/1594719475362-38e63632-dc26-416f-9ee5-dc3b4553fe68.svg#align=left&display=inline&height=20&margin=%5Bobject%20Object%5D&originHeight=20&originWidth=98&size=0&status=done&style=none&width=98)]()![](https://cdn.nlark.com/yuque/0/2020/svg/486920/1594719475494-85eb2ec4-9312-4297-9136-3de634bbce2a.svg#align=left&display=inline&height=20&margin=%5Bobject%20Object%5D&originHeight=20&originWidth=76&size=0&status=done&style=none&width=76)[![](https://cdn.nlark.com/yuque/0/2020/svg/486920/1594719475472-dab71e89-05ca-4e52-837e-a4df50301cec.svg#align=left&display=inline&height=20&margin=%5Bobject%20Object%5D&originHeight=20&originWidth=90&size=0&status=done&style=none&width=90)]()[![](https://cdn.nlark.com/yuque/0/2020/svg/486920/1594719476110-afa843a9-1077-49d1-a358-44eb8ff470fe.svg#align=left&display=inline&height=20&margin=%5Bobject%20Object%5D&originHeight=20&originWidth=84&size=0&status=done&style=none&width=84)]()<br />

<a name="ae406301"></a>
#### 集中化任务调度

- 异步任务调度
- 计划任务统一管理 Crontab
- Job 执行状态监控



<a name="838f2d93"></a>
### ScheduOps 能做什么？

<br />以下案例是 scheduOps 在发布系统（Pilot）中的使用场景，封装了 SaltStack Api、AnsibleApi、JenkinsApi、JiraApi等，使用一套平台操作各类自动化流程，进行集中管理。<br />
<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/486920/1594719674366-7e1ae835-b85c-44f0-964e-9ddb2071a594.png#align=left&display=inline&height=300&margin=%5Bobject%20Object%5D&name=image.png&originHeight=600&originWidth=1526&size=448460&status=done&style=none&width=763)<br />
<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/486920/1594719713896-cc8860c4-ccff-4cd3-87d3-8c5e2777f8b3.png#align=left&display=inline&height=387&margin=%5Bobject%20Object%5D&name=image.png&originHeight=774&originWidth=1523&size=289695&status=done&style=none&width=761.5)<br />
<br />![image.png](https://cdn.nlark.com/yuque/0/2020/png/486920/1594719740616-2ac6789e-28ec-4940-ba95-71ad02623a9f.png#align=left&display=inline&height=407&margin=%5Bobject%20Object%5D&name=image.png&originHeight=813&originWidth=1524&size=399986&status=done&style=none&width=762)<br />

<a name="5a991227"></a>
### 如何使用？


```python
git clone https://github.com/gongwz/scheduOps.git
pip3 install -r requirements.txt
```

<br />使用本项目之前请先阅读本人另外两个项目：<br />
<br />[https://github.com/gongwz/formcurd.git](https://github.com/gongwz/formcurd.git)<br />[https://github.com/gongwz/pilot.git](https://github.com/gongwz/pilot.git)<br />

> Author: 卫振 （weizhen）  -- 首次尝试微博图床 ^_-

