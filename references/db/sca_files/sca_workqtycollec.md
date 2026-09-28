# 作业数量归集-sca_workqtycollec

## 作业数量归集-主表 t_sca_workqtycollec

- **表名称：** 作业数量归集-主表
- **表名：** t_sca_workqtycollec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 3 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 6 | fworkactivityid | 作业活动 | int8 | 64 |  | √ | 0 | 作业活动 cad_new_workactivity |
| 7 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 核算组织(202306版本多核算体系废弃) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbizdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | '0' | 成本主体 cal_bd_costaccount |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fbillno | 单据编号 | varchar | 60 |  | √ | ' ' | 单据编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fcostdriverid | 费用分配标准 | int8 | 64 |  | √ | 0 | 费用分配标准 cad_costdriver |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_workqtycol_worka |  | fworkactivityid |
| 2 | t_sca_workqtycollec_pkey |  | fid |
| 3 | idx_sca_workqtycollec |  | forgid,fbizdate,fcostcenterid |
| 4 | idx_workqtycol_costc |  | fcostcenterid |

---

## 单据体-子表 t_sca_workqtycollecentry

- **表名称：** 单据体-子表
- **表名：** t_sca_workqtycollecentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fcostobjectid | 成本核算对象 | int8 | 64 |  | √ | 0 | 成本核算对象 cad_costobjectf7 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbenefcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sca_workqtycollecentry2 |  | fid |
| 2 | t_sca_workqtycollecentry_pkey |  | fentryid |
| 3 | idx_sca_workqtycollecentry |  | fbenefcostcenterid,fcostobjectid |
| 4 | idex_wqcolentry_costobj |  | fcostobjectid |

---

## 作业数量归集-多语言表 t_sca_workqtycollec_l

- **表名称：** 作业数量归集-多语言表
- **表名：** t_sca_workqtycollec_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sca_workqtycollec_l_pkey |  | fpkid |
| 2 | idx_sca_workqtycollec_l |  | fid,flocaleid |
