# 报价单-tnd_quotebill

## 供应商用户-多选基础资料表 t_src_supplieruser

- **表名称：** 供应商用户-多选基础资料表
- **表名：** t_src_supplieruser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 供应商用户 pur_supuser |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supplieruser_bid |  | fbasedataid |
| 2 | pk_src_supplieruser |  | fpkid |
| 3 | idx_src_supplieruser_fid |  | fid |

---

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

## 报价单-主表 t_src_quotebill

- **表名称：** 报价单-主表
- **表名：** t_src_quotebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已终止 E :已废标 Z :无需处理 |
| 4 | fbilldate | 报价时间 | timestamp | 0 |  |  | null | 报价时间 |
| 5 | freplenishtype | 补价方式 | bpchar | 1 |  | √ | ' ' | 补价方式,枚举: 1 :补分项价格 2 :补价格及分项价格 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fvietaxamount | 竞价金额(含税) | numeric | 23 | 10 | √ | 0 | 竞价金额(含税) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fopentype | 开标方式 | bpchar | 1 |  | √ | ' ' | 开标方式,枚举: 1 :截止时间手动开标 3 :截止时间自动开标 9 :报价即开标(非密封报价) |
| 10 | fsumamount | 未税总价 | numeric | 23 | 10 | √ | 0 | 未税总价 |
| 11 | fturns | 报价轮次 | varchar | 2 |  | √ | ' ' | 报价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 30 :补价(1) 31 :补价(2) 32 :补价(3) |
| 12 | fisadd | 是否允许供应商新增标的 | bpchar | 1 |  | √ | '0' | 是否允许供应商新增标的 |
| 13 | fvieturns | 竞价轮次 | varchar | 2 |  | √ | '1' | 竞价轮次,枚举: 1 :首轮 2 :竞价(2) 3 :竞价(3) 4 :竞价(4) 5 :竞价(5) 6 :竞价(6) 7 :竞价(7) 8 :竞价(8) 9 :竞价(8) 10 :竞价(10) 11 :竞价(11) 12 :竞价(12) 13 :竞价(13) 14 :竞价(14) 15 :竞价(15) 16 :竞价(16) 17 :竞价(17) 18 :竞价(18) 19 :竞价(19) 20 :竞价(20) 21 :竞价(21) 22 :竞价(22) 23 :竞价(23) 24 :竞价(24) 25 :竞价(25) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fispuragent | 采购方代理报价 | bpchar | 1 |  | √ | '0' | 采购方代理报价 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | ftemplateid | 报价模板 | int8 | 64 |  | √ | 0 | 组件模板配置 pds_tplconfig |
| 19 | fprojectid | 招标项目编号 | int8 | 64 |  | √ | 0 | 招标项目F7 src_projectf7 |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 26 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 27 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 28 | fsuppliertype | 供应商类别 | varchar | 50 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 29 | fiscompete | 电子竞价 | bpchar | 1 |  | √ | '0' | 电子竞价 |
| 30 | fisfinish | 已完成竞价 | bpchar | 1 |  | √ | '0' | 已完成竞价 |
| 31 | fdeadline | 报价截止时间 | timestamp | 0 |  |  | null | 报价截止时间 |
| 32 | fsumtaxamount | 合计金额(含税) | numeric | 23 | 10 | √ | 0 | 合计金额(含税) |
| 33 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 34 | fisnotice | 是否已发消息 | bpchar | 1 |  | √ | '0' | 是否已发消息 |
| 35 | fnegotiatetype | 议价方式 | bpchar | 1 |  | √ | ' ' | 议价方式,枚举: 1 :线上议价 2 :线下议价(标的) 3 :线下议价(标段) 4 :电子竞价 |
| 36 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_quotebill_billdate |  | fbilldate |
| 2 | idx_src_quotebill_supplier |  | fsupplierid |
| 3 | idx_src_quotebill_parentid |  | fparentid |
| 4 | pk_src_quotebill |  | fid |
| 5 | idx_src_quotebill_billno |  | fbillno |
| 6 | idx_src_quotebill_project |  | fprojectid |
