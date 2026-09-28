# 术语修改日志-cts_termwordlog

## 术语修改日志-主表 t_cts_termwordlog

- **表名称：** 术语修改日志-主表
- **表名：** t_cts_termwordlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 5 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdestterm | 新值 | varchar | 1024 |  | √ | ' ' | 新值 |
| 8 | fstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | ftype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 3 :替换 4 :恢复 |
| 11 | fwordid | 术语 | int8 | 64 |  | √ | 0 | 术语替换 cts_termword |
| 12 | ftermwordcomp | 词条 | varchar | 1024 |  | √ | ' ' | 词条 |
| 13 | fenable | 启用 | bpchar | 1 |  | √ | '1' | 启用,枚举: |
| 14 | fsrcterm | 新值 | varchar | 1024 |  | √ | ' ' | 新值 |
| 15 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cts_termwordlog_pkey |  | fid |
| 2 | idx_cts_termwordlog_fwordid |  | fwordid |

---

## 术语修改日志-多语言表 t_cts_termwordlog_l

- **表名称：** 术语修改日志-多语言表
- **表名：** t_cts_termwordlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 1024 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cts_termwordlog_l_fid |  | fid,flocaleid |
| 2 | t_cts_termwordlog_l_pkey |  | fpkid |
