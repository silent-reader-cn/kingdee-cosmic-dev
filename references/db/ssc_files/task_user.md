# 共享用户-task_user

## 共享用户-主表 t_tk_usergroupentry

- **表名称：** 共享用户-主表
- **表名：** t_tk_usergroupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaskallnum_e | 处理任务总数上限 | int8 | 64 |  | √ | 10000 | 处理任务总数上限 |
| 3 | fgroupid | 用户组id | int8 | 64 |  | √ | 0 | 用户组id |
| 4 | fcurtasknum_e | 处理中任务数上限 | int8 | 64 |  | √ | 10000 | 处理中任务数上限 |
| 5 | fdptname | fdptname | int8 | 64 |  | √ | 0 |  |
| 6 | fusestatus | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态 |
| 7 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 8 | fuserid | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fteamleader | 组长 | bpchar | 1 |  | √ | '0' | 组长 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fability | 能力值 | numeric | 19 | 10 | √ | 1.0000000000 | 能力值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_usergroup_e_fgrpid |  | fgroupid |
| 2 | t_tk_usergroupentry_pkey |  | fentryid |
| 3 | index_usergroupentry |  | fuserid |
| 4 | idx_ssc_usergroup_e_fid |  | fid |
