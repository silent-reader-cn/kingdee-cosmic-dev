# 更新记录明细-bd_admin_predata_log

## 更新记录明细-多语言表 t_bd_admindivisionlog_l

- **表名称：** 更新记录明细-多语言表
- **表名：** t_bd_admindivisionlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | foriginname | 原名称 | varchar | 255 |  | √ | ' ' | 原名称 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | foriginfullname | 原长名称 | varchar | 1024 |  | √ | ' ' | 原长名称 |
| 6 | forigindescription | 原描述 | varchar | 255 |  | √ | ' ' | 原描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_admindivisionlog_l |  | fpkid |
| 2 | idx_bd_adminlog_l |  | fid |

---

## 更新记录明细-主表 t_bd_admindivisionlog

- **表名称：** 更新记录明细-主表
- **表名：** t_bd_admindivisionlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foriginlongnumber | 原长编码 | varchar | 255 |  | √ | ' ' | 原长编码 |
| 3 | foriginareacode | 原参考码 | varchar | 10 |  | √ | ' ' | 原参考码 |
| 4 | foriginname | 原名称 | varchar | 255 |  | √ | ' ' | 原名称 |
| 5 | fparentname | 上级行政区划 | varchar | 512 |  | √ | ' ' | 上级行政区划 |
| 6 | forigindescription | 原描述 | varchar | 255 |  | √ | ' ' | 原描述 |
| 7 | fcitynumber | 电话区号 | varchar | 255 |  | √ | ' ' | 电话区号 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fupdatemode | 更新方式 | varchar | 10 |  | √ | ' ' | 更新方式,枚举: insert :新增 update :更新 disable :禁用 |
| 10 | foriginfullspell | 原全拼 | varchar | 255 |  | √ | ' ' | 原全拼 |
| 11 | fareacode | 参考码 | varchar | 36 |  | √ | ' ' | 参考码 |
| 12 | fsimplespell | 英文简称 | varchar | 512 |  | √ | ' ' | 英文简称 |
| 13 | foriginfullname | 原长名称 | varchar | 1024 |  | √ | ' ' | 原长名称 |
| 14 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 15 | fpresetlogid | 版本更新记录id | int8 | 64 |  | √ | 0 | 版本更新记录id |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | foriginsimplespell | 原简拼 | varchar | 255 |  | √ | ' ' | 原简拼 |
| 18 | fischildren | 子节点 | bpchar | 1 |  | √ | '0' | 子节点 |
| 19 | foriginadmindivisionlvid | 原行政级次ID | int8 | 64 |  | √ | 0 | 原行政级次ID |
| 20 | fdescription | 描述 | varchar | 512 |  | √ | ' ' | 描述 |
| 21 | foriginlevel | 原行政级次 | int8 | 64 |  | √ | 0 | 原行政级次 |
| 22 | fadmindivisionid | 行政区划 | int8 | 64 |  | √ | 0 | 行政区划 |
| 23 | foriginparentid | 原父级ID | int8 | 64 |  | √ | 0 | 原父级ID |
| 24 | ffullspell | 英文全称 | varchar | 512 |  | √ | ' ' | 英文全称 |
| 25 | fadminlvname | 行政级次 | varchar | 128 |  | √ | ' ' | 行政级次 |
| 26 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_adminlog_preset |  | fpresetlogid |
| 2 | pk_bd_admindivisionlog |  | fid |
