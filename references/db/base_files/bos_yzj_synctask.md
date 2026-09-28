# 协同云同步任务-bos_yzj_synctask

## 协同云同步任务-多语言表 t_yzj_synctask_l

- **表名称：** 协同云同步任务-多语言表
- **表名：** t_yzj_synctask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_yzj_synctask_l_pkey |  | fpkid |
| 2 | idx_t_yzj_synctask_l_fid |  | fid,flocaleid |

---

## 协同云同步任务-主表 t_yzj_synctask

- **表名称：** 协同云同步任务-主表
- **表名：** t_yzj_synctask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 5 | fnormalcount | 一般 | int8 | 64 |  | √ | 0 | 一般 |
| 6 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :同步正常 1 :报告正常 2 :过时 3 :异常 |
| 7 | fexceptioncount | 异常 | int8 | 64 |  | √ | 0 | 异常 |
| 8 | fislatest | 是否最新 | bpchar | 1 |  | √ | ' ' | 是否最新 |
| 9 | fenable | fenable | bpchar | 1 |  | √ | ' ' |  |
| 10 | funsynccount | 未同步 | int8 | 64 |  | √ | 0 | 未同步 |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 13 | ftotal | 差异总数 | int8 | 64 |  | √ | 0 | 差异总数 |
| 14 | fsynccount | 已同步 | int8 | 64 |  | √ | 0 | 已同步 |
| 15 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_yzj_synctask_number |  | fnumber |
| 2 | t_yzj_synctask_pkey |  | fid |
