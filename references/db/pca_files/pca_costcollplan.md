# 项目成本来源设置-pca_costcollplan

## 来源自定义-子表 t_pca_costcollplan_cust

- **表名称：** 来源自定义-子表
- **表名：** t_pca_costcollplan_cust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 2 :不影响 |
| 3 | fconvsubelementid | 默认成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fpluginpath | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 5 | fcollconfigid | 自定义单据名称 | int8 | 64 |  | √ | 0 | [自定义核算单配置 pca_collconfig_cust](../pca_files/pca_collconfig_cust.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsrcbilltype | fsrcbilltype | varchar | 50 |  | √ | ' ' |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costcollplan_cust |  | fentryid |
| 2 | idx_pca_costcollplan_cust_fid |  | fid,fseq |

---

## 来源应付款管理-子表 t_pca_costcollplan_ap

- **表名称：** 来源应付款管理-子表
- **表名：** t_pca_costcollplan_ap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 2 :不影响 |
| 3 | fconvsubelementid | 默认成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsrcbilltype | 来源业务单据 | varchar | 50 |  | √ | ' ' | 来源业务单据,枚举: ap_busbill :暂估应付单 ap_finapbill :财务应付单 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsysbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

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
| 3 | fbizentityobjectid | 来源核算单 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fisgenmatcost | 只取通用料成本 | bpchar | 1 |  | √ | '0' | 只取通用料成本 |
| 5 | fcollconfigid | 映射配置(隐藏字段) | int8 | 64 |  | √ | 0 | [项目归集映射配置 pca_collconfig](../pca_files/pca_collconfig.md) |
| 6 | fcalbilltype | 核算单类型 | varchar | 50 |  | √ | ' ' | 核算单类型,枚举: OUT :出库 IN :入库 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcalbillruleid | fcalbillruleid | int8 | 64 |  | √ | 0 |  |
| 9 | fsrcbilltype | 来源业务单据 | varchar | 50 |  | √ | ' ' | 来源业务单据,枚举: cal_costrecord_subentity :核算成本记录 cal_costadjust_subentity :成本调整单 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fmaterialattr | 物料属性 | varchar | 255 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 10070 :特征件 |
| 12 | fsysbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |

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

## 来源系统总账-子表 t_pca_costcollplan_gl

- **表名称：** 来源系统总账-子表
- **表名：** t_pca_costcollplan_gl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangedcosttype | 项目成本变动类型 | varchar | 50 |  | √ | ' ' | 项目成本变动类型,枚举: 0 :减 1 :增 |
| 3 | fconvsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 4 | fassgrp | 科目核算维度值 | varchar | 2000 |  | √ | ' ' | 科目核算维度值 |
| 5 | fcollconfigid | 映射配置(隐藏字段) | int8 | 64 |  | √ | 0 | [项目归集映射配置 pca_collconfig](../pca_files/pca_collconfig.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | faccountviewid | 会计科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 8 | fdirection | 借贷方向 | varchar | 50 |  | √ | ' ' | 借贷方向,枚举: 1 :借方 -1 :贷方 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | faccountbookid | 总账账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 11 | facctviewbaltype | 取值来源 | varchar | 50 |  | √ | ' ' | 取值来源,枚举: 1 :实际损益发生额 2 :凭证 |

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

## 成本中心-多选基础资料表 t_pca_costcollplan_acactr

- **表名称：** 成本中心-多选基础资料表
- **表名：** t_pca_costcollplan_acactr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costcollplan_acactr_fk |  | fentryid |
| 2 | pk_pca_costcollplan_acactr |  | fpkid |

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
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsrcsystype | 来源业务系统 | varchar | 100 |  | √ | ' ' | 来源业务系统,枚举: 1 :总账 2 :费用核算 3 :存货核算 4 :实际成本核算 5 :应付款管理 6 :自定义 |
| 13 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 14 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 16 | fprojectgroupid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

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

## 部门-多选基础资料表 t_pca_costcollplan_calorg

- **表名称：** 部门-多选基础资料表
- **表名：** t_pca_costcollplan_calorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costcollplan_calorg_fk |  | fentryid |
| 2 | pk_pca_costcollplan_calorg |  | fpkid |

---

## 存货类别-多选基础资料表 t_pca_costcollplan_acamc

- **表名称：** 存货类别-多选基础资料表
- **表名：** t_pca_costcollplan_acamc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [存货类别 bd_materialcategory](../basedata_files/bd_materialcategory.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costcollplan_acamc |  | fpkid |
| 2 | idx_pca_costcollplan_acamc_fk |  | fentryid |

---

## 存货类别-多选基础资料表 t_pca_costcollplan_calmc

- **表名称：** 存货类别-多选基础资料表
- **表名：** t_pca_costcollplan_calmc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [存货类别 bd_materialcategory](../basedata_files/bd_materialcategory.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_costcollplan_calmc |  | fpkid |
| 2 | idx_pca_costcollplan_calmc_fk |  | fentryid |

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
| 4 | fcollconfigid | 映射配置(隐藏字段) | int8 | 64 |  | √ | 0 | [项目归集映射配置 pca_collconfig](../pca_files/pca_collconfig.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsrcbilltype | 来源业务单据 | varchar | 50 |  | √ | ' ' | 来源业务单据,枚举: aca_matalloc :材料耗用分配 cad_mfgfeeallocco :成本中心内分配 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmaterialattr | 物料属性 | varchar | 255 |  | √ | ' ' | 物料属性,枚举: 10030 :自制 10040 :外购 10050 :委外 10020 :虚拟 10070 :特征件 |

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

## 来源费用核算-子表 t_pca_costcollplan_rmb

- **表名称：** 来源费用核算-子表
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
