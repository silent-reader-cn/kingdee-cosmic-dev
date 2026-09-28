# 无代码历史参与人-wf_nocode_hiparticipant

## 无代码历史参与人-主表 t_wf_nocode_hiparticipant

- **表名称：** 无代码历史参与人-主表
- **表名：** t_wf_nocode_hiparticipant

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusernameformatter | 被设置的用户名称 | varchar | 500 |  | √ | ' ' | 被设置的用户名称 |
| 3 | fsubscribesign | 是否订阅会审 | bpchar | 1 |  | √ | '1' | 是否订阅会审 |
| 4 | fcurrentsubject | 当前任务主题 | varchar | 1000 |  | √ | ' ' | 当前任务主题 |
| 5 | ftrustnameformat | 受托人名称格式化 | varchar | 500 |  | √ | ' ' | 受托人名称格式化 |
| 6 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 7 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 8 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 9 | ftransferopinion | 转交意见 | varchar | 2000 |  | √ | ' ' | 转交意见 |
| 10 | ftrustname | 受托人名称 | varchar | 255 |  | √ | ' ' | 受托人名称 |
| 11 | fparenttaskid | 父任务Id | int8 | 64 |  | √ | 0 | 父任务Id |
| 12 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 13 | fownerid | 所有者id | int8 | 64 |  | √ | 0 | 所有者id |
| 14 | fusername | 用户名称 | varchar | 255 |  | √ | ' ' | 用户名称 |
| 15 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fduration | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 17 | fisdisplay | 是否显示 | bpchar | 1 |  | √ | '1' | 是否显示 |
| 18 | ftype | 参与人类型 | varchar | 30 |  | √ | ' ' | 参与人类型 |
| 19 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 20 | freadtime | 开封时间 | timestamp | 0 |  |  | null | 开封时间 |
| 21 | fdelegateid | 委托设置Id | int8 | 64 |  | √ | 0 | 委托设置Id |
| 22 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 23 | fcompositetaskid | 聚合任务 | int8 | 64 |  | √ | 0 | 聚合任务 |
| 24 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_nocode_hiparticipant |  | fid |
| 2 | idx_wf_nc_hipartcpant_type |  | ftype |
| 3 | idx_wf_nc_hipartcpant_credate |  | fcreatedate |
| 4 | idx_wf_nc_hipartcpant_task |  | ftaskid |
| 5 | idx_wf_nc_hipartcpant_comptask |  | fcompositetaskid |
| 6 | idx_wf_nc_hipartcpant_ownerid |  | fownerid,ftype,fendtime,fdelegateid |
| 7 | idx_wf_nc_hipartcpant_ptasksub |  | fparenttaskid,fsubscribesign |
| 8 | idx_wf_nc_hipartcpant_user |  | fuserid |
| 9 | idx_wf_nc_hipartcpant_procinst |  | fprocinstid |

---

## 无代码历史参与人-多语言表 t_wf_nocode_hiparticipant_l

- **表名称：** 无代码历史参与人-多语言表
- **表名：** t_wf_nocode_hiparticipant_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fusernameformatter | 被设置的用户名称 | varchar | 500 |  | √ | ' ' | 被设置的用户名称 |
| 3 | fusername | 用户名称 | varchar | 255 |  | √ | ' ' | 用户名称 |
| 4 | fcurrentsubject | 当前任务主题 | varchar | 1000 |  | √ | ' ' | 当前任务主题 |
| 5 | ftrustnameformat | 受托人名称格式化 | varchar | 500 |  | √ | ' ' | 受托人名称格式化 |
| 6 | ftransferopinion | 转交意见 | varchar | 2000 |  | √ | ' ' | 转交意见 |
| 7 | ftrustname | 受托人名称 | varchar | 255 |  | √ | ' ' | 受托人名称 |
| 8 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 9 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_nocode_hiparticipant_l |  | fid,flocaleid |
| 2 | pk_wf_nocode_hiparticipant_l |  | fpkid |
