# 预算控制日志-xkbm_budgetctrllog

## 控制明细-子表 t_xkbm_ctrllogentity

- **表名称：** 控制明细-子表
- **表名：** t_xkbm_ctrllogentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flevel | 日志级别 | varchar | 50 |  | √ | ' ' | 日志级别 |
| 3 | fdescriptions | 操作内容 | varchar | 255 |  | √ | ' ' | 操作内容 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fruleid | 控制规则 | int8 | 64 |  | √ | 0 | [预算控制规则 xkbm_ctrlrule](../xkbm_files/xkbm_ctrlrule.md) |
| 6 | flogtype | 日志类型 | varchar | 50 |  | √ | ' ' | 日志类型 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | flogtime | 操作时间 | varchar | 50 |  | √ | ' ' | 操作时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_ctrllogentity |  | fentryid |
| 2 | idx_xkbm_ctrllogentity |  | flogtype,fruleid |

---

## 预算控制结果-子表 t_xkbm_ctrlressubentity

- **表名称：** 预算控制结果-子表
- **表名：** t_xkbm_ctrlressubentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbalvalue | 可用数 | numeric | 23 | 10 | √ | 0 | 可用数 |
| 2 | foverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fctrldate | 控制日期 | timestamp | 0 |  |  | null | 控制日期 |
| 5 | fbudgetvalue | 预算数 | numeric | 23 | 10 | √ | 0 | 预算数 |
| 6 | frptdimgroupkey | 编制维度组合键 | varchar | 500 |  | √ | ' ' | 编制维度组合键 |
| 7 | fctrlruleid | 控制规则 | int8 | 64 |  | √ | 0 | [预算控制规则 xkbm_ctrlrule](../xkbm_files/xkbm_ctrlrule.md) |
| 8 | forgunit | 控制组织 | int8 | 64 |  | √ | 0 | [预算组织 xkbm_budgetorgunit](../xkbm_files/xkbm_budgetorgunit.md) |
| 9 | fyear | 控制年度 | varchar | 50 |  | √ | ' ' | 控制年度 |
| 10 | fscheme | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 11 | fperiodtype | 周期类型 | bpchar | 1 |  | √ | '0' | 周期类型,枚举: 0 :年 1 :半年 2 :季 3 :月 5 :周 6 :日 |
| 12 | fperiod | 控制期间 | int4 | 32 |  | √ | 0 | 控制期间 |
| 13 | factvalue | 已发生 | numeric | 23 | 10 | √ | 0 | 已发生 |
| 14 | fcurbillvalue | 当前单据数 | numeric | 23 | 10 | √ | 0 | 当前单据数 |
| 15 | fcumperiodenddate | 期间累计截止日期 | timestamp | 0 |  |  | null | 期间累计截止日期 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbm_rptitemdatatype](../fibd_files/xkbm_rptitemdatatype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_ctrlressub_id |  | fentryid |
| 2 | pk_xkbm_ctrlressubentity |  | fdetailid |

---

## 预算控制日志-主表 t_xkbm_budgetctrllog

- **表名称：** 预算控制日志-主表
- **表名：** t_xkbm_budgetctrllog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 预算业务服务 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fbillformid | 控制单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 6 | falldetailed | 所有信息 | text | 0 |  |  | null | 所有信息 |
| 7 | fcreatetime | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 8 | foperatetime | 操作日期 | timestamp | 0 |  |  | null | 操作日期 |
| 9 | fmodifier | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | foperationnumber | 操作名称 | varchar | 50 |  | √ | ' ' | 操作名称 |
| 11 | fdescription | 操作说明 | varchar | 2000 |  | √ | ' ' | 操作说明 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 19 | foperationid | 操作ID | varchar | 50 |  | √ | ' ' | 操作ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_budgetctrllog |  | fid |
| 2 | idx_xkbm_budgetctrllog |  | fbillformid,fbillno |

---

## 预算控制日志-多语言表 t_xkbm_budgetctrllog_l

- **表名称：** 预算控制日志-多语言表
- **表名：** t_xkbm_budgetctrllog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_budgetctrllog_l |  | fpkid |
| 2 | idx_xkbm_ctrllog_l_fname |  | fname |
| 3 | idx_xkbm_ctrllog_l_fid |  | fid |

---

## 单据发生信息-子表 t_xkbm_ctrllogsubentity

- **表名称：** 单据发生信息-子表
- **表名：** t_xkbm_ctrllogsubentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdrptdimgroupkey | 编制维度组合键 | varchar | 500 |  | √ | ' ' | 编制维度组合键 |
| 2 | fusedbillno | 控制单据编号 | varchar | 50 |  | √ | ' ' | 控制单据编号 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fusedbillformid | 控制单据 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fdscheme | 预算方案 | int8 | 64 |  | √ | 0 | [预算方案 xkbm_scheme](../xkbm_files/xkbm_scheme.md) |
| 6 | fusetype | 预算影响类型 | varchar | 50 |  | √ | ' ' | 预算影响类型 |
| 7 | fdorgunit | 控制组织 | int8 | 64 |  | √ | 0 | [预算组织 xkbm_budgetorgunit](../xkbm_files/xkbm_budgetorgunit.md) |
| 8 | fdyear | 控制年度 | varchar | 50 |  | √ | ' ' | 控制年度 |
| 9 | fdperiod | 控制期间 | int4 | 32 |  | √ | 0 | 控制期间 |
| 10 | fbackvalue | 冲回数 | numeric | 23 | 10 | √ | 0 | 冲回数 |
| 11 | fusedvalue | 已使用数 | numeric | 23 | 10 | √ | 0 | 已使用数 |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 13 | fusedbilldate | 控制单据日期 | timestamp | 0 |  |  | null | 控制单据日期 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_ctrllogsub_id |  | fentryid |
| 2 | pk_t_xkbm_ctrllogsubentity |  | fdetailid |
