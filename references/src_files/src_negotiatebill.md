# 议价单-src_negotiatebill

## 模板分录-子表 t_src_projecttpl

- **表名称：** 模板分录-子表
- **表名：** t_src_projecttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomponentid | 业务组件 | int8 | 64 |  | √ | 0 | 组件注册 pds_compreg |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 4 | fbizobject | 业务对象 | varchar | 50 |  | √ | ' ' | 业务对象 |
| 5 | fsrctplid | 来源模板ID | varchar | 50 |  | √ | ' ' | 来源模板ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_projecttpl_fscp |  | fsrctplid |
| 2 | idx_src_projecttpl_fobj |  | fbizobject |
| 3 | pk_src_projecttpl |  | fentryid |
| 4 | idx_src_projecttpl_fcom |  | fcomponentid |
| 5 | idx_src_projecttpl_fid |  | fid |
| 6 | idx_src_projecttpl_ftem |  | ftemplateid |

---

## 采购组织-多选基础资料表 t_src_negotiatebill_org

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_src_negotiatebill_org

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_negotiatebill_org |  | fpkid |
| 2 | idx_src_negbill_org_bid |  | fbasedataid |
| 3 | idx_src_negbill_org_eid |  | fid |

---

## 议价单-主表 t_src_negotiatebill

- **表名称：** 议价单-主表
- **表名：** t_src_negotiatebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已终止 E :已废标 |
| 4 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 5 | fbilldate | 发布时间 | timestamp | 0 |  |  | null | 发布时间 |
| 6 | fpurdeptid | 采购部门 | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 7 | freplenishtype | 补录价格方式 | bpchar | 1 |  | √ | ' ' | 补录价格方式,枚举: 1 :补分项价格 2 :补价格及分项价格 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fopentype | 开标方式 | bpchar | 1 |  | √ | ' ' | 开标方式,枚举: 1 :截止时间手动开标 3 :截止时间自动开标 9 :报价即开标(非密封报价) |
| 11 | fturns | 议价轮次 | varchar | 2 |  | √ | ' ' | 议价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 12 :议价(11) 13 :议价(12) 14 :议价(13) 15 :议价(14) 16 :议价(15) 17 :议价(16) 18 :议价(17) 19 :议价(18) 20 :议价(19) 21 :议价(20) 22 :议价(21) 23 :议价(22) 24 :议价(23) 25 :议价(24) 26 :议价(25) 27 :议价(26) 28 :议价(27) 29 :议价(28) 30 :议价(29) 31 :补价(1) 32 :补价(2) 33 :补价(3) 34 :补价(4) 35 :补价(5) |
| 12 | fpurgroupid | 采购组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 13 | fbillno | 议价单号 | varchar | 30 |  | √ | ' ' | 议价单号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | ftemplateid | 议价模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 16 | fprojectid | 招标项目编号 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fbidcount | 报价次数 | int4 | 32 |  | √ | 0 | 报价次数 |
| 21 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 24 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 25 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 26 | fquotenum | 开标时对报价供应商数量的要求 | bpchar | 1 |  | √ | '1' | 开标时对报价供应商数量的要求,枚举: 0 :不限制 1 :至少有一家已报价 2 :一半以上已报价 3 :所有供应商均已报价 |
| 27 | fsuppliertype | fsuppliertype | varchar | 30 |  | √ | ' ' |  |
| 28 | fcontent_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 29 | fdeadline | 报价截止时间 | timestamp | 0 |  |  | null | 报价截止时间 |
| 30 | fisnotice | 是否已发消息 | bpchar | 1 |  | √ | '0' | 是否已发消息 |
| 31 | fcontent | 内容 | varchar | 255 |  | √ | ' ' | 内容 |
| 32 | fcurrentnode | 议价节点 | int8 | 64 |  | √ | 0 | 业务节点 pds_biznode |
| 33 | fnegotiatetype | 议价方式 | bpchar | 1 |  | √ | ' ' | 议价方式,枚举: 1 :线上议价 2 :线下议价(标的) 4 :电子竞价 |
| 34 | fisreplenish | 是否补录价格 | bpchar | 1 |  | √ | '0' | 是否补录价格 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fisquotebidopen | 已议标开标 | bpchar | 1 |  | √ | '0' | 已议标开标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_negotiatebill_billdata |  | fbilldate |
| 2 | idx_src_negotiatebill_billno |  | fbillno |
| 3 | idx_src_negotiatebill_proid |  | fprojectid |
| 4 | idx_src_negotiatebill_supid |  | fsupplierid |
| 5 | idx_src_negotiatebill_parentid |  | fparentid |
| 6 | pk_src_negotiatebill |  | fid |
