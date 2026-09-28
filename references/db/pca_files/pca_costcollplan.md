# 项目成本来源设置-pca_costcollplan

## 来源应付-子表 t_pca_costcollplan_ap

- **表名称：** 来源应付-子表
- **表名：** t_pca_costcollplan_ap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 2 :不影响 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsrcbilltype | 来源业务单据 | varchar | 50 |  | √ | ' ' | 来源业务单据,枚举: ap_busbill :暂估应付单 ap_finapbill :财务应付单 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costcollplan_ap_fid |  | fid,fseq |
| 2 | pk_pca_costcollplan_ap |  | fentryid |

---

## 来源存货核算-子表 t_pca_costcollplan_cal

- **表名称：** 来源存货核算-子表
- **表名：** t_pca_costcollplan_cal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 2 :不影响 |
| 3 | fbizentityobjectid | 来源核算单 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 4 | fcollconfigid | 映射配置(隐藏字段) | int8 | 64 |  | √ | 0 | 项目归集配置单 pca_collconfig |
| 5 | fcalbilltype | 核算单类型 | varchar | 50 |  | √ | ' ' | 核算单类型,枚举: OUT :出库 IN :入库 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcalbillruleid | fcalbillruleid | int8 | 64 |  | √ | 0 |  |
| 8 | fsrcbilltype | 来源业务单据 | varchar | 50 |  | √ | ' ' | 来源业务单据,枚举: cal_costrecord_subentity :核算成本记录 cal_costadjust_subentity :成本调整单 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costcollplan_cal |  | fentryid |
| 2 | idx_pca_costcollplan_cal_fid |  | fid,fseq |

---

## 项目成本来源设置-主表 t_pca_costcollplan

- **表名称：** 项目成本来源设置-主表
- **表名：** t_pca_costcollplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsrcsystype | 来源业务系统 | varchar | 100 |  | √ | ' ' | 来源业务系统,枚举: 1 :总账 2 :费用报销 3 :存货核算 4 :实际成本核算 5 :应付 |
| 13 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | 项目核算主体 pca_costaccount |
| 14 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 16 | fprojectgroupid | 项目分类 | int8 | 64 |  | √ | 0 | 项目分类 bd_projectkind |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costcollplan_num |  | fnumber |
| 2 | idx_pca_costcollplan_costaccount |  | fcostaccountid,fprojectgroupid |
| 3 | pk_pca_costcollplan |  | fid |

---

## 项目成本来源设置-多语言表 t_pca_costcollplan_l

- **表名称：** 项目成本来源设置-多语言表
- **表名：** t_pca_costcollplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costcollplan_l_0 |  | fid,flocaleid |
| 2 | pk_pca_costcollplan_l |  | fpkid |

---

## 来源系统总账-子表 t_pca_costcollplan_gl

- **表名称：** 来源系统总账-子表
- **表名：** t_pca_costcollplan_gl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 |
| 3 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | 成本子要素 cad_subelement |
| 4 | fassgrp | 科目核算维度值 | varchar | 2000 |  | √ | ' ' | 科目核算维度值 |
| 5 | fcollconfigid | 映射配置(隐藏字段) | int8 | 64 |  | √ | 0 | 项目归集配置单 pca_collconfig |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | faccountviewid | 会计科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | faccountbookid | 总账账簿 | int8 | 64 |  | √ | 0 | 账簿 gl_accountbook |
| 10 | facctviewbaltype | 科目余额类型 | varchar | 50 |  | √ | ' ' | 科目余额类型,枚举: 1 :实际损益发生额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costcollplan_gl |  | fentryid |
| 2 | idx_pca_costcollplan_gl_fid |  | fid,fseq |

---

## 来源实际成本核算-子表 t_pca_costcollplan_aca

- **表名称：** 来源实际成本核算-子表
- **表名：** t_pca_costcollplan_aca

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 2 :不影响 |
| 3 | fisgenmatcost | 只取通用料成本 | bpchar | 1 |  | √ | '0' | 只取通用料成本 |
| 4 | fcollconfigid | 映射配置(隐藏字段) | int8 | 64 |  | √ | 0 | 项目归集配置单 pca_collconfig |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsrcbilltype | 来源业务单据 | varchar | 50 |  | √ | ' ' | 来源业务单据,枚举: aca_matalloc :材料耗用分配 cad_mfgfeeallocco :成本中心内分配 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costcollplan_aca_fid |  | fid,fseq |
| 2 | pk_pca_costcollplan_aca |  | fentryid |

---

## 来源费用报销-子表 t_pca_costcollplan_rmb

- **表名称：** 来源费用报销-子表
- **表名：** t_pca_costcollplan_rmb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 2 :不影响 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsrcbilltype | 来源业务单据 | varchar | 50 |  | √ | ' ' | 来源业务单据,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsrcdatetype | 入账日期 | varchar | 50 |  | √ | ' ' | 入账日期,枚举: 1 :审核日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costcollplan_rmb |  | fentryid |
| 2 | idx_pca_costcollplan_rmb_fid |  | fid,fseq |
