# 表单关联规则-mpm_formlinkrule

## 单据体-子表 t_mpm_formlinkrule_entry

- **表名称：** 单据体-子表
- **表名：** t_mpm_formlinkrule_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fimportbill | 引入单据 | varchar | 50 |  |  | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fremark | 备注信息 | varchar | 500 |  |  | ' ' | 备注信息 |
| 4 | fimportfieldname | 引入字段名称 | varchar | 100 |  |  | ' ' | 引入字段名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fauthority | 鉴权 | varchar | 20 |  |  | ' ' | 鉴权 |
| 7 | flinkfieldname | 关联字段名称 | varchar | 100 |  |  | ' ' | 关联字段名称 |
| 8 | fsourceform | 源单 | bpchar | 1 |  | √ | '0' | 源单 |
| 9 | fischoose | 源单是否选中 | bpchar | 1 |  | √ | '0' | 源单是否选中 |
| 10 | flevel | 层级 | int4 | 32 |  | √ | 0 | 层级 |
| 11 | flinkfield | 关联字段标识 | varchar | 50 |  |  | ' ' | 关联字段标识 |
| 12 | fimportfield | 引入字段标识 | varchar | 50 |  |  | ' ' | 引入字段标识 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fchildnum | 子类数量 | int4 | 32 |  | √ | 0 | 子类数量 |
| 15 | flinkbill | 关联单据 | varchar | 50 |  |  | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_formlinkrule_fid |  | fid |
| 2 | pk_t_mpm_formlinkrule_entry |  | fentryid |

---

## 表单关联规则-主表 t_mpm_formlinkrule

- **表名称：** 表单关联规则-主表
- **表名：** t_mpm_formlinkrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :启用 1 :未启用 2 :禁用 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | frulename | 规则名称 | varchar | 80 |  | √ | ' ' | 规则名称 |
| 8 | fbillno | 规则编码 | varchar | 80 |  | √ | ' ' | 规则编码 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fruledesc | 规则描述 | varchar | 2000 |  |  | ' ' | 规则描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_formlinkrule_billno |  | fbillno |
| 2 | pk_t_mpm_formlinkrule |  | fid |
