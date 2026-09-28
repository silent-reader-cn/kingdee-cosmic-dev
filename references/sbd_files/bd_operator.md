# 供应链业务员-bd_operator

## 供应链业务员-主表 t_bd_operatorgroupentry

- **表名称：** 供应链业务员-主表
- **表名：** t_bd_operatorgroupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 业务组内码 | int8 | 64 |  | √ | 0 | 业务组内码 |
| 2 | fdeptid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | foperatorid | 人员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fopergrptype | 业务组类型 | varchar | 5 |  | √ | ' ' | 业务组类型,枚举: CGZ :采购组 KCZ :库管组 XSZ :销售组 JHZ :计划组 ZJZ :质检组 |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fopergrpnumber | 业务组编码 | varchar | 80 |  | √ | ' ' | 业务组编码 |
| 7 | foperatorname | 业务员名称 | varchar | 255 |  |  | ' ' | 业务员名称 |
| 8 | finvalid | 失效 | bpchar | 1 |  | √ | '0' | 失效 |
| 9 | fposition | fposition | varchar | 255 |  | √ | ' ' |  |
| 10 | foperatornumber | 业务员编码 | varchar | 80 |  | √ | ' ' | 业务员编码 |
| 11 | fopergrpname | 业务组名称 | varchar | 50 |  | √ | ' ' | 业务组名称 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fisdefault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_operatorgroupentry_pkey |  | fentryid |
| 2 | idx_bd_operatorgroupentry_fid |  | fid |

---

## 供应链业务员-多语言表 t_bd_operatorgroupentry_l

- **表名称：** 供应链业务员-多语言表
- **表名：** t_bd_operatorgroupentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | foperatorname | 业务员名称 | varchar | 255 |  |  | ' ' | 业务员名称 |
| 2 | fposition | fposition | varchar | 255 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fopergrpname | 业务组名称 | varchar | 50 |  | √ | ' ' | 业务组名称 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_operatorgroupentry_l |  | fentryid,flocaleid |
| 2 | t_bd_operatorgroupentry_l_pkey |  | fpkid |
