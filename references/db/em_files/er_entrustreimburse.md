# 委托报销-er_entrustreimburse

## 委托报销-多语言表 t_er_entrustreimburse_l

- **表名称：** 委托报销-多语言表
- **表名：** t_er_entrustreimburse_l

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
| 1 | idx_t_er_etreim_l_lid |  | fid,flocaleid |
| 2 | t_er_entrustreimburse_l_pkey |  | fpkid |

---

## 委托范围-多选基础资料表 t_er_entrustreimbursescop

- **表名称：** 委托范围-多选基础资料表
- **表名：** t_er_entrustreimbursescop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [费用单据类型 er_billtype](../basedata_files/er_billtype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_entrustreimbursescop |  | fpkid |
| 2 | idx_er_entrustreimbursescop_id |  | fid |

---

## 委托报销-主表 t_er_entrustreimburse

- **表名称：** 委托报销-主表
- **表名：** t_er_entrustreimburse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcuruser | 当前用户为受托（移动端用） | bpchar | 1 |  | √ | '0' | 当前用户为受托（移动端用） |
| 3 | fconsignorid | 委托人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | ftrusteeorgid | 受托人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fenddate | 委托日期.结束 | timestamp | 0 |  |  | null | 委托日期.结束 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | frentrustdate | 委托时间（废弃） | varchar | 100 |  | √ | ' ' | 委托时间（废弃） |
| 13 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fentrustedscope | fentrustedscope | varchar | 255 |  | √ | ' ' |  |
| 18 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fconsignororgid | 委托人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fctrlstrategy | fctrlstrategy | varchar | 10 |  | √ | ' ' |  |
| 21 | fstartdate | 委托日期.开始 | timestamp | 0 |  |  | null | 委托日期.开始 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | frentrustedscope | 委托范围 | varchar | 1000 |  | √ | ' ' | 委托范围 |
| 24 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 25 | ftrusteeid | 受托人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_entrb_fconsignorid |  | fconsignorid |
| 2 | t_er_entrustreimburse_pkey |  | fid |
