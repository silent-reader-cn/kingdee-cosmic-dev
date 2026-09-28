# 用户隐私操作日志-recru_privacyoplog

## 用户隐私操作日志-多语言表 t_recru_privacyoplog_l

- **表名称：** 用户隐私操作日志-多语言表
- **表名：** t_recru_privacyoplog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_privacyoplog_l |  | fpkid |
| 2 | idx_recru_privacyoplog_l_fid |  | fid,flocaleid |

---

## 用户隐私操作日志-主表 t_recru_privacyoplog

- **表名称：** 用户隐私操作日志-主表
- **表名：** t_recru_privacyoplog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | foperatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | fipaddress | 操作ip地址 | varchar | 100 |  | √ | ' ' | 操作ip地址 |
| 8 | fsubjecttypeid | 操作对象类型 | int8 | 64 |  | √ | 0 | [隐私操作对象类型 recru_subjecttype](../recru_files/recru_subjecttype.md) |
| 9 | fsubjectid | 操作对象单据id | int8 | 64 |  | √ | 0 | 操作对象单据id |
| 10 | fprivacyopid | 操作 | int8 | 64 |  | √ | 0 | [隐私操作 recru_privacyop](../recru_files/recru_privacyop.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 2 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsessionid | 会话id | varchar | 100 |  | √ | ' ' | 会话id |
| 16 | fenable | 使用状态 | varchar | 2 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fterminal | 操作终端 | varchar | 2 |  | √ | ' ' | 操作终端,枚举: 1 :客户端 2 :PC端 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_recru_privacyoplog |  | fid |
| 2 | idx_recru_privacyoplog_number |  | fnumber |
