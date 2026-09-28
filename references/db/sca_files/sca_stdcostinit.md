# 实际成本结束初始化-sca_stdcostinit

## 单据体-子表 t_sca_startstdcostentry

- **表名称：** 单据体-子表
- **表名：** t_sca_startstdcostentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcalpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | 会计政策 cal_bd_calpolicy |
| 3 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | 标准成本方案 cad_costtype |
| 4 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fisenabled | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 7 | fstartperiodid | 启用期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fisinit | 结束初始化 | bpchar | 1 |  | √ | '0' | 结束初始化 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_startstdcostentry_pkey |  | fentryid |
| 2 | idx_sca_startstdcostentry |  | fcostaccountid,fcalpolicyid |
| 3 | idx_sca_startstdcostentry2 |  | fid |

---

## 实际成本结束初始化-主表 t_sca_startstdcost

- **表名称：** 实际成本结束初始化-主表
- **表名：** t_sca_startstdcost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcosttypeid | fcosttypeid | int8 | 64 |  | √ | 0 |  |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用 |
| 10 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_startstdcost |  | fbillstatus,forgid |
| 2 | t_sca_startstdcost_pkey |  | fid |
