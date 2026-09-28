# 云之家沟通-wf_yzjchat

## 云之家沟通-主表 t_wf_yzjchat

- **表名称：** 云之家沟通-主表
- **表名：** t_wf_yzjchat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 组Id | varchar | 80 |  | √ | ' ' | 组Id |
| 3 | fcurrenteropenid | 发起人openId | varchar | 80 |  | √ | ' ' | 发起人openId |
| 4 | fopenids | 人员OpenIds | varchar | 2000 |  | √ | ' ' | 人员OpenIds |
| 5 | frecord | 聊天记录 | varchar | 80 |  | √ | ' ' | 聊天记录 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fscene | 场景 | varchar | 80 |  | √ | ' ' | 场景 |
| 8 | fbillid | 单据Id | varchar | 36 |  | √ | ' ' | 单据Id |
| 9 | fidentitykey | 唯一标识 | varchar | 2000 |  | √ | ' ' | 唯一标识 |
| 10 | ffeaturecode | 特征码 | varchar | 80 |  | √ | ' ' | 特征码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_yzjchat_pkey |  | fid |
| 2 | idx_wf_yzjchat_group |  | fgroupid |
