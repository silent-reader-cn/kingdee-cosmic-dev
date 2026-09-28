# 流程耗时明细-wf_durationdetail

## 流程耗时明细-多语言表 t_wf_durationdetail_l

- **表名称：** 流程耗时明细-多语言表
- **表名：** t_wf_durationdetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuspendreason | 挂起原因 | text | 0 |  |  | null | 挂起原因 |
| 3 | factivityname | 当前活动节点名称 | varchar | 500 |  | √ | ' ' | 当前活动节点名称 |
| 4 | fprocname | 流程名称 | varchar | 115 |  | √ | ' ' | 流程名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_durationdetail_l |  | fid,flocaleid |
| 2 | t_wf_durationdetail_l_pkey |  | fpkid |

---

## 流程耗时明细-主表 t_wf_durationdetail

- **表名称：** 流程耗时明细-主表
- **表名：** t_wf_durationdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsuspduration | 挂起时长 | int8 | 64 |  | √ | 0 | 挂起时长 |
| 4 | factinstid | 当前节点实例ID | int8 | 64 |  | √ | 0 | 当前节点实例ID |
| 5 | fsuspendreason | 挂起原因 | text | 0 |  |  | null | 挂起原因 |
| 6 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 7 | ferrortype | 异常类型 | varchar | 30 |  | √ | ' ' | 异常类型,枚举: engine :引擎异常 nullParticipant :参与人为空异常 business :业务调用异常 conditionParse :条件解析异常 messageService :消息异常 configuration :配置异常 outSet :出口线异常 |
| 8 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 9 | fcalduration | 工作日历时长 | int8 | 64 |  | √ | 0 | 工作日历时长 |
| 10 | fsuspenderid | 挂起人 | int8 | 64 |  | √ | 0 | 挂起人 |
| 11 | fundosusptime | 撤销挂起时间 | timestamp | 0 |  |  | null | 撤销挂起时间 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: 1 :异常挂起 2 :手动挂起 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | factid | 当前活动节点ID | varchar | 255 |  | √ | ' ' | 当前活动节点ID |
| 16 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | factivityname | 当前活动节点名称 | varchar | 500 |  | √ | ' ' | 当前活动节点名称 |
| 18 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 19 | frealduration | 有效时长 | int8 | 64 |  | √ | 0 | 有效时长 |
| 20 | fprocname | 流程名称 | varchar | 115 |  | √ | ' ' | 流程名称 |
| 21 | fprocnumber | 流程编码 | varchar | 50 |  | √ | ' ' | 流程编码 |
| 22 | fsuspendtime | 开始挂起时间 | timestamp | 0 |  |  | null | 开始挂起时间 |
| 23 | ftaskid | 任务Id | int8 | 64 |  | √ | 0 | 任务Id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_durationdetail |  | fprocinstid,factid |
| 2 | idx_wf_durationdetail_ttu |  | ftaskid,ftype,fundosusptime |
| 3 | t_wf_durationdetail_pkey |  | fid |
| 4 | idx_wf_durationdetail_actinst |  | factinstid |
