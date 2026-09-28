# 投标单(工具)-tnd_tenderbill_tool

## 模板分录-子表 t_src_projecttpl

- **表名称：** 模板分录-子表
- **表名：** t_src_projecttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomponentid | 业务组件 | int8 | 64 |  | √ | 0 | [组件注册 pds_compreg](../pds_files/pds_compreg.md) |
| 3 | ftemplateid | 组件模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
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

## 投标单(工具)-主表 t_src_biddocbill

- **表名称：** 投标单(工具)-主表
- **表名：** t_src_biddocbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fissplitdoc | 是否拆分标书文件 | bpchar | 1 |  | √ | '0' | 是否拆分标书文件 |
| 4 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | ' ' | 业务状态,枚举: A :未开始 B :处理中 C :已处理 D :已终止 E :已废标 Z :无需处理 |
| 5 | fbilldate | 投标时间 | timestamp | 0 |  |  | null | 投标时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fisneedbiddoc | 供应商必须上传标书 | bpchar | 1 |  | √ | '0' | 供应商必须上传标书 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fsumamount | 未税总价 | numeric | 23 | 10 | √ | 0 | 未税总价 |
| 10 | fturns | 报价轮次 | varchar | 2 |  | √ | ' ' | 报价轮次,枚举: 1 :首轮 2 :议价(1) 3 :议价(2) 4 :议价(3) 5 :议价(4) 6 :议价(5) 7 :议价(6) 8 :议价(7) 9 :议价(8) 10 :议价(9) 11 :议价(10) 30 :补价(1) 31 :补价(2) 32 :补价(3) |
| 11 | fisadd | 是否允许供应商新增标的 | bpchar | 1 |  | √ | '0' | 是否允许供应商新增标的 |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fispuragent | 采购方代理投标 | bpchar | 1 |  | √ | '0' | 采购方代理投标 |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ftemplateid | 投标单模板 | int8 | 64 |  | √ | 0 | [组件模板配置 pds_tplconfig](../pds_files/pds_tplconfig.md) |
| 17 | fprojectid | 招标项目编号 | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fistender | 允许供应商修改标书 | bpchar | 1 |  | √ | '0' | 允许供应商修改标书 |
| 22 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 25 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |
| 26 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 27 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 28 | fdeadline | 投标截止时间 | timestamp | 0 |  |  | null | 投标截止时间 |
| 29 | fsumtaxamount | 含税总价 | numeric | 23 | 10 | √ | 0 | 含税总价 |
| 30 | fsupplierip | 供应商IP | varchar | 100 |  | √ | ' ' | 供应商IP |
| 31 | fisnotice | 是否已发消息 | bpchar | 1 |  | √ | '0' | 是否已发消息 |
| 32 | fnumber | 退回重新投标次数 | int4 | 32 |  | √ | 0 | 退回重新投标次数 |
| 33 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fisquote | 允许供应商修改报价 | bpchar | 1 |  | √ | '0' | 允许供应商修改报价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_biddocbill_fprojectid |  | fprojectid |
| 2 | idx_src_biddocbill_fbilldate |  | fbilldate |
| 3 | idx_src_biddocbill_fparentid |  | fparentid |
| 4 | idx_src_biddocbill_fsupplierid |  | fsupplierid |
| 5 | pk_src_biddocbill |  | fid |
| 6 | idx_src_biddocbill_fbillno |  | fbillno |

---

## 供应商用户-多选基础资料表 t_src_supplieruser

- **表名称：** 供应商用户-多选基础资料表
- **表名：** t_src_supplieruser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [供应商用户 pur_supuser](../basedata_files/pur_supuser.md) |
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
