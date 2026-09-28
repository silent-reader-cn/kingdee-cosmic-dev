# 收款判重设置-cas_recwarnset

## 收款判重设置-主表 t_cas_recwarnset

- **表名称：** 收款判重设置-主表
- **表名：** t_cas_recwarnset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 0 :禁用 1 :启用 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpayer | 付款人相同 | bpchar | 1 |  | √ | '0' | 付款人相同 |
| 6 | fpaynum | 付款账号相同 | bpchar | 1 |  | √ | '0' | 付款账号相同 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | ftype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: rec :收款单 |
| 10 | frecamount | 收款金额相同 | bpchar | 1 |  | √ | '0' | 收款金额相同 |
| 11 | fbizdate | 业务日期相同 | bpchar | 1 |  | √ | '0' | 业务日期相同 |
| 12 | fday | 校验周期（天） | int8 | 64 |  | √ | 0 | 校验周期（天） |
| 13 | fbillno | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 14 | frecnum | 收款账号相同 | bpchar | 1 |  | √ | '0' | 收款账号相同 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_recwarnset_pkey |  | fid |
| 2 | index_recwarnset_fbillno |  | fbillno |

---

## 单据体-子表 t_cas_recwarnentry

- **表名称：** 单据体-子表
- **表名：** t_cas_recwarnentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 组织编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_recwarnset_orgid |  | forgid |
| 2 | t_cas_recwarnentry_pkey |  | fentryid |
