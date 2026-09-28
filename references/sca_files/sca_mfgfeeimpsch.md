# 制造费用引入方案-sca_mfgfeeimpsch

## 来源科目-多选基础资料表 t_sca_mfgimp_accountviews

- **表名称：** 来源科目-多选基础资料表
- **表名：** t_sca_mfgimp_accountviews

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_mfgimp_accountviews |  | fpkid |
| 2 | idx_mfgimp_basedata |  | fid,fbasedataid |

---

## 单据体-子表 t_sca_mfgfeeimpschentry

- **表名称：** 单据体-子表
- **表名：** t_sca_mfgfeeimpschentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fsubelementid | fsubelementid | int8 | 64 |  | √ | 0 |  |
| 5 | fcostcentertype | 成本中心取值 | varchar | 30 |  | √ | ' ' | 成本中心取值,枚举: FIXED :固定值 MATCH :按源单匹配 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | famount | 费用金额 | varchar | 200 |  | √ | ' ' | 费用金额,枚举: debitlocal :借方发生额 creditlocal :贷方发生额 e_localamt :明细•金额 |
| 8 | felementid | felementid | int8 | 64 |  | √ | 0 |  |
| 9 | fbenefcostcentertype | 受益成本中心取值 | varchar | 30 |  | √ | ' ' | 受益成本中心取值,枚举: FIXED :固定值 MATCH :按成本中心匹配 |
| 10 | fexpenseitemtype | 费用项目取值 | varchar | 30 |  | √ | ' ' | 费用项目取值,枚举: FIXED :固定值 MATCH :按源单匹配 |
| 11 | fbizdate | 业务日期 | varchar | 60 |  |  | ' ' | 业务日期,枚举: |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | fbenefcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_mfgfeeimpschentry |  | fentryid |
| 2 | idx_sca_mfgfeeimpschentry2 |  | fid |

---

## 制造费用引入方案-多语言表 t_sca_mfgfeeimpsch_l

- **表名称：** 制造费用引入方案-多语言表
- **表名：** t_sca_mfgfeeimpsch_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_mfgfeeimpsch_l |  | fpkid |

---

## 制造费用引入方案-主表 t_sca_mfgfeeimpsch

- **表名称：** 制造费用引入方案-主表
- **表名：** t_sca_mfgfeeimpsch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fassgrp | 核算维度 | varchar | 2000 |  | √ | ' ' | 核算维度 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | faccountviewid | 来源科目（旧） | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 9 | fisfromgl | fisfromgl | bpchar | 1 |  | √ | ' ' |  |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fappnum | 所属应用 | varchar | 100 |  | √ | ' ' | 所属应用,枚举: sca :标准成本 aca :实际成本 |
| 12 | fsrcbill | 来源单据 | varchar | 60 |  | √ | ' ' | 来源单据,枚举: gl_voucher :凭证 ap_process :暂估应付单/财务应付单（取加工费） ap_freight :暂估应付单/财务应付单（取运费） |
| 13 | faccountbookid | 对应账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 17 | fbillno | 单据编码 | varchar | 60 |  | √ | ' ' | 单据编码 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 19 | fsrcbizsysid | 来源业务系统 | varchar | 60 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sca_mfgfeeimpsch |  | fid |
