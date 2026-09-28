# 启用实际成本核算-sca_startstdcost

## 单据体-子表 t_sca_startstdcostentry

- **表名称：** 单据体-子表
- **表名：** t_sca_startstdcostentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartsfcperiodid | 启用年期（工序） | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fstartperiodid | 启用期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fisinit | 结束初始化 | bpchar | 1 |  | √ | '0' | 结束初始化 |
| 6 | fcalpolicyid | 会计政策 | int8 | 64 |  | √ | 0 | [会计政策 cal_bd_calpolicy](../cal_files/cal_bd_calpolicy.md) |
| 7 | fisenabledsfc | 启用（工序） | bpchar | 1 |  | √ | '0' | 启用（工序） |
| 8 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 9 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 10 | fisenabledsfcseq | 按工序号核算 | bpchar | 1 |  | √ | '0' | 按工序号核算 |
| 11 | fisenabled | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 12 | fisenabledsfcstep | 启用分步结转 | bpchar | 1 |  | √ | '0' | 启用分步结转 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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

## 启用实际成本核算-主表 t_sca_startstdcost

- **表名称：** 启用实际成本核算-主表
- **表名：** t_sca_startstdcost

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcosttypeid | fcosttypeid | int8 | 64 |  | √ | 0 |  |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用 |
| 10 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 11 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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
