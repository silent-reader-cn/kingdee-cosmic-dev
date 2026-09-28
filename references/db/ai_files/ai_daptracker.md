# DAP关系-ai_daptracker

## 单据体-子表 t_ai_daptrackerentry

- **表名称：** 单据体-子表
- **表名：** t_ai_daptrackerentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvoucherentryid | 凭证分录ID | int8 | 64 |  | √ | 0 | 凭证分录ID |
| 3 | fbillentryid | 单据分录ID | int8 | 64 |  | √ | 0 | 单据分录ID |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_daptrackerentry_pkey |  | fentryid |
| 2 | idx_ai_daptrackerentry |  | fid,fbillentryid |

---

## DAP关系-主表 t_ai_daptracker

- **表名称：** DAP关系-主表
- **表名：** t_ai_daptracker

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freoper | 关联操作 | varchar | 30 |  | √ | ' ' | 关联操作,枚举: |
| 3 | fvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 4 | fbooktypeid | 账簿类型 | int8 | 64 |  | √ | 0 | [账簿类型 bd_accountbookstype](../fibd_files/bd_accountbookstype.md) |
| 5 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fvchtemplateid | 凭证模板ID | int8 | 64 |  | √ | 0 | 凭证模板ID |
| 7 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 8 | foper | 操作编码 | varchar | 50 |  | √ | ' ' | 操作编码 |
| 9 | forgid | 核算主体 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fsourcebillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 11 | fcustomkey | 自定义标识 | varchar | 200 |  | √ | ' ' | 自定义标识 |
| 12 | fbilltype | 单据类型 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_daptracker_srcbillid |  | fsourcebillid |
| 2 | idx_ai_daptracker_billtype |  | fbilltype |
| 3 | t_ai_daptracker_pkey |  | fid |
| 4 | idx_ai_daptracker_orgperid |  | forgid,fperiodid |
| 5 | idx_ai_daptracker_vchid |  | fvoucherid |
