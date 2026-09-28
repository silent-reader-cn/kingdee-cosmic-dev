# s-HR集成映射关系-xkcts_shr_orgmapping

## s-HR集成映射关系-主表 t_xkbas_shr_org

- **表名称：** s-HR集成映射关系-主表
- **表名：** t_xkbas_shr_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 60 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 8 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkbas_shr_org_fcreatetim |  | fcreatetime |
| 2 | pk_t_xkbas_shr_org |  | fid |

---

## 映射关系-子表 t_xkbas_shr_org_entry

- **表名称：** 映射关系-子表
- **表名：** t_xkbas_shr_org_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadminorgid | 行政组织（部门）编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 1 | 分录行号 |
| 4 | fpaymentorgid | 对应应付组织（收付职能）编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsettlementorgid | 对应费用承担组织（结算职能）编码 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbas_shr_org_entry |  | fentryid |
| 2 | idx_t_xkbas_shr_org_entry_fid |  | fid |
