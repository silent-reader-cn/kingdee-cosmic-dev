# 制造费用归集方案-sco_mfgfeeimpsch

## 单据体-子表 t_sco_mfgfeeimpschentry

- **表名称：** 单据体-子表
- **表名：** t_sco_mfgfeeimpschentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 4 | fsubelementid | fsubelementid | int8 | 64 |  | √ | 0 |  |
| 5 | fcostcentertype | 成本中心取值 | varchar | 30 |  | √ | ' ' | 成本中心取值,枚举: FIXED :固定值 MATCH :按源单匹配 |
| 6 | fproductgroupid | 产品组 | int8 | 64 |  | √ | 0 | [产品组 sco_productweight](../sco_files/sco_productweight.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | famount | 费用金额 | varchar | 255 |  | √ | ' ' | 费用金额,枚举: debitlocal :借方发生额 creditlocal :贷方发生额 e_localamt :明细•金额 |
| 9 | felementid | felementid | int8 | 64 |  | √ | 0 |  |
| 10 | fbenefcostcentertype | 受益成本中心取值 | varchar | 30 |  | √ | ' ' | 受益成本中心取值,枚举: FIXED :固定值 MATCH :按成本中心匹配 |
| 11 | fexpenseitemtype | 费用项目取值 | varchar | 30 |  | √ | ' ' | 费用项目取值,枚举: FIXED :固定值 MATCH :按源单匹配 |
| 12 | fbizdate | 业务日期 | varchar | 80 |  | √ | ' ' | 业务日期,枚举: |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fbenefcostcenterid | 受益成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_mfgfeeimpschentry2 |  | fid |
| 2 | idx_sco_mfgfeeimpschentry |  | fcostcenterid,fexpenseitemid,felementid |
| 3 | pk_sco_mfgfeeimpschentry |  | fentryid |

---

## 制造费用归集方案-主表 t_sco_mfgfeeimpsch

- **表名称：** 制造费用归集方案-主表
- **表名：** t_sco_mfgfeeimpsch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmanuorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fassgrp | 核算维度 | varchar | 2000 |  | √ | ' ' | 核算维度 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | faccountviewid | 来源科目（旧） | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 9 | fisfromgl | fisfromgl | bpchar | 1 |  | √ | ' ' |  |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fappnum | 所属应用 | varchar | 10 |  | √ | ' ' | 所属应用,枚举: sco :标准成本 aca :实际成本 eca :服务成本 |
| 12 | fsrcbill | 来源单据 | varchar | 80 |  | √ | ' ' | 来源单据,枚举: gl_voucher :凭证 ap_process :暂估应付单/财务应付单（取加工费） ap_freight :暂估应付单/财务应付单（取运费） |
| 13 | fsrcfield | 维度字段标识 | varchar | 80 |  | √ | ' ' | 维度字段标识 |
| 14 | faccountbookid | 对应账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fgroupfield | 归集合单维度 | varchar | 80 |  | √ | ' ' | 归集合单维度,枚举: bos_org :业务单元 |
| 17 | flevel | 优先级 | varchar | 10 |  | √ | ' ' | 优先级,枚举: 1 :一级 2 :二级 3 :三级 4 :四级 5 :五级 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 20 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fsrcbizsysid | 来源业务系统 | varchar | 80 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_mfgfeeimpsch |  | fcostaccountid |
| 2 | pk_sco_mfgfeeimpsch |  | fid |

---

## 制造费用归集方案-多语言表 t_sco_mfgfeeimpsch_l

- **表名称：** 制造费用归集方案-多语言表
- **表名：** t_sco_mfgfeeimpsch_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_mfgfeeimpsch_l |  | fid,flocaleid |
| 2 | pk_sco_mfgfeeimpsch_l |  | fpkid |

---

## 来源科目-多选基础资料表 t_sco_mfgimp_accountviews

- **表名称：** 来源科目-多选基础资料表
- **表名：** t_sco_mfgimp_accountviews

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sco_mfgimp_accountviews |  | fid |
| 2 | pk_sco_mfgimp_accountviews |  | fpkid |
