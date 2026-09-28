# 红字确认单（全电发票）-sim_red_confirm_bill

## 红字确认单（全电发票）-使用范围表 t_sim_red_confirm_bill_u

- **表名称：** 红字确认单（全电发票）-使用范围表
- **表名：** t_sim_red_confirm_bill_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_red_confirm_bill_u |  | fdataid,fuseorgid |
| 2 | idx_t_sim_red_confirm_bill_u_uo |  | fuseorgid |

---

## 红字确认单（全电发票）-多语言表 t_sim_red_confirm_bill_l

- **表名称：** 红字确认单（全电发票）-多语言表
- **表名：** t_sim_red_confirm_bill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_red_confirm_bill_l |  | fpkid |
| 2 | idx_sim_red_confirm_bill_l |  | fid,flocaleid |

---

## 单据体-子表 t_sim_red_confirm_items

- **表名称：** 单据体-子表
- **表名：** t_sim_red_confirm_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 3 | ftaxrate | 税率 | varchar | 30 |  | √ | ' ' | 税率,枚举: 0 :0% 0.01 :1% 0.03 :3% 0.05 :5% 0.06 :6% 0.09 :9% 0.10 :10% 0.11 :11% 0.13 :13% 0.16 :16% 0.17 :17% |
| 4 | frowtype | 发票行性质 | varchar | 30 |  | √ | ' ' | 发票行性质,枚举: 0 :正常行 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 8 | ftaxunitprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 9 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 10 | fgoodscode | 税收分类编码 | varchar | 50 |  | √ | ' ' | 税收分类编码 |
| 11 | fgoodsname | 商品名称 | varchar | 150 |  | √ | ' ' | 商品名称 |
| 12 | fspecification | 规格型号 | varchar | 60 |  | √ | ' ' | 规格型号 |
| 13 | ftax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 14 | fbillsourceid | 单据来源id | varchar | 50 |  | √ | ' ' | 单据来源id |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | funit | 单位 | varchar | 60 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sim_red_confirm_items_fk |  | fid |
| 2 | pk_t_sim_red_confirm_items |  | fentryid |

---

## 红字确认单（全电发票）-主表 t_sim_red_confirm_bill

- **表名称：** 红字确认单（全电发票）-主表
- **表名：** t_sim_red_confirm_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织（没用上） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftotalamount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 5 | fhsbz | 含税标志 | varchar | 30 |  | √ | '0' | 含税标志,枚举: 0 :不含税 1 :含税 |
| 6 | fconfirmstatus | 确认状态 | varchar | 30 |  | √ | ' ' | 确认状态,枚举: 01 :无需确认 02 :销方录入待购方确认 03 :购方录入待销方确认 04 :购销双方已确认 05 :作废（销方录入购方否认） 06 :作废（购方录入销方否认） 07 :作废（超72小时未确认） 08 :作废（发起方已撤销） 09 :作废（确认后撤销） 10 :作废（异常凭证） |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsource | 数据来源 | varchar | 30 |  | √ | '1' | 数据来源,枚举: 1 :手工新增 2 :税局下载 5 :单据开票 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 审核状态 | varchar | 30 |  | √ | ' ' | 审核状态,枚举: A :暂存 B :已提交 C :已审核 D :无需审批 |
| 11 | ftotaltax | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fgovuuid | 税局返回uuid | varchar | 50 |  | √ | ' ' | 税局返回uuid |
| 17 | fbuyername | 购方名称 | varchar | 150 |  | √ | ' ' | 购方名称 |
| 18 | finvoiceno | 红票号码 | varchar | 50 |  | √ | ' ' | 红票号码 |
| 19 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 20 | fsalertaxno | 销方税号 | varchar | 50 |  | √ | ' ' | 销方税号 |
| 21 | fcreateorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fbuyertaxno | 购方税号 | varchar | 50 |  | √ | ' ' | 购方税号 |
| 23 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fredreason | 红冲原因 | varchar | 30 |  | √ | '01' | 红冲原因,枚举: 01 :开票有误 03 :服务终止 04 :销售折让 |
| 27 | foriginalinvoiceno | 原蓝票号码 | varchar | 30 |  | √ | ' ' | 原蓝票号码 |
| 28 | fapplicant | 购销身份 | varchar | 30 |  | √ | '2' | 购销身份,枚举: 2 :我是销方 1 :我是购方 |
| 29 | forderno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 30 | foriginalinvoicetype | 原蓝票发票种类 | varchar | 30 |  | √ | ' ' | 原蓝票发票种类,枚举: 10xdp :全电发票（普通发票） 08xdp :全电发票（增值税专用发票） |
| 31 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | '7' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 32 | foriginalissuetime | 原蓝票开票日期 | timestamp | 0 |  |  | null | 原蓝票开票日期 |
| 33 | fuploadstatus | 录入状态 | varchar | 30 |  | √ | '0' | 录入状态,枚举: 0 :未录入 1 :已录入 2 :录入失败 |
| 34 | finvoicetype | 发票种类 | varchar | 30 |  | √ | ' ' | 发票种类,枚举: 08xdp :全电发票（增值税专用发票） 10xdp :全电发票（普通发票） |
| 35 | foriginalinvoicecode | 原蓝票代码 | varchar | 30 |  | √ | ' ' | 原蓝票代码 |
| 36 | finvoiceamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 37 | fsalername | 销方名称 | varchar | 150 |  | √ | ' ' | 销方名称 |
| 38 | fissuestatus | 开票状态 | varchar | 30 |  | √ | '2' | 开票状态,枚举: 0 :已开票 2 :未开票 |
| 39 | fsystemsource | 数据系统来源 | varchar | 50 |  | √ | ' ' | 数据系统来源 |
| 40 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 41 | fnumber | 红字确认单编号 | varchar | 50 |  | √ | ' ' | 红字确认单编号 |
| 42 | fuploaddate | 税局返回录入日期 | timestamp | 0 |  |  | null | 税局返回录入日期 |
| 43 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_red_confirm_bill |  | fid |
| 2 | idx_sim_red_confirm_number |  | fnumber |
| 3 | idx_t_sim_red_confirm_bill_createorg |  | fcreateorgid |
| 4 | idx_sim_red_confirm_createorg |  | fcreateorgid |
| 5 | idx_sim_red_confirm_createtime |  | fcreatetime |
| 6 | idx_t_sim_red_confirm_bill_master |  | fmasterid |
| 7 | idx_sim_red_confirm_master |  | fmasterid |
