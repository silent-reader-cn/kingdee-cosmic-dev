# 对账方案-pur_chkscheme

## 对账方案-使用范围表 t_pur_chkscheme_u

- **表名称：** 对账方案-使用范围表
- **表名：** t_pur_chkscheme_u

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
| 1 | idx_t_pur_chkscheme_u_uo |  | fuseorgid |
| 2 | pk_t_pur_chkscheme_u |  | fdataid,fuseorgid |

---

## 物料范围-多选基础资料表 t_pur_chkscheme_mat

- **表名称：** 物料范围-多选基础资料表
- **表名：** t_pur_chkscheme_mat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_chkscheme_mat_pkey |  | fpkid |
| 2 | idx_pur_chkscheme_mat_fid |  | fid,fbasedataid |

---

## 对账方案-主表 t_pur_chkscheme

- **表名称：** 对账方案-主表
- **表名：** t_pur_chkscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdifftreattype | 如果继续处理，以哪一方为准 | bpchar | 1 |  | √ | ' ' | 如果继续处理，以哪一方为准,枚举: 1 :以采购方为准 2 :以销售方为准 3 :手工填写 |
| 3 | finvdetail | 开票要求 | bpchar | 1 |  | √ | ' ' | 开票要求,枚举: 1 :汇总开具 2 :按明细开具 |
| 4 | ftaxrate | 按税率 | bpchar | 1 |  | √ | ' ' | 按税率 |
| 5 | fautocfm | 对账单确认方式 | bpchar | 1 |  | √ | ' ' | 对账单确认方式,枚举: 1 :无差异对账单自动确认 2 :无差异对账单手工确认 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fnodifftype | 判定对账有无差异的依据 | bpchar | 1 |  | √ | ' ' | 判定对账有无差异的依据,枚举: 1 :数量和金额都要相等 2 :金额相等，数量可不等 3 :数量相等，金额可不等 |
| 8 | fasstattrib | 按辅助属性 | bpchar | 1 |  | √ | ' ' | 按辅助属性 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fsumupamount | 每月对账总金额上限 | numeric | 19 | 6 | √ | 0.000000 | 每月对账总金额上限 |
| 11 | fdefault | 默认方案 | bpchar | 1 |  | √ | ' ' | 默认方案 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :保存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | finvtype | 发票种类 | bpchar | 1 |  | √ | ' ' | 发票种类,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | finvseq | 开票顺序 | varchar | 255 |  | √ | ' ' | 开票顺序 |
| 18 | fmaterial | 按物料 | bpchar | 1 |  | √ | ' ' | 按物料 |
| 19 | fdifftreattype2 | 出现差异时(完全对不上)是否继续处理 | bpchar | 1 |  | √ | ' ' | 出现差异时(完全对不上)是否继续处理,枚举: 3 :处理 4 :不处理 |
| 20 | fgoods | 按商品 | bpchar | 1 |  | √ | ' ' | 按商品 |
| 21 | fdifftreattype1 | 出现差异时(部分对得上)是否继续处理 | bpchar | 1 |  | √ | ' ' | 出现差异时(部分对得上)是否继续处理,枚举: 3 :处理 4 :不处理 |
| 22 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 23 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 24 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 25 | fdateto | 每月对账截止日 | int8 | 64 |  | √ | 0 | 每月对账截止日 |
| 26 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 27 | forgscope | 使用组织范围 | bpchar | 1 |  | √ | ' ' | 使用组织范围,枚举: 1 :所有组织 2 :指定组织 |
| 28 | fcurrency | 按结算币别 | bpchar | 1 |  | √ | ' ' | 按结算币别 |
| 29 | fdatasrc1 | 供应商数据范围 | bpchar | 1 |  | √ | ' ' | 供应商数据范围,枚举: 1 :销售发货单(含退货) |
| 30 | fsalbillno | 按采购订单 | bpchar | 1 |  | √ | ' ' | 按采购订单 |
| 31 | fsupscope | 适用供应商范围 | bpchar | 1 |  | √ | ' ' | 适用供应商范围,枚举: 1 :所有供应商 2 :指定供应商 |
| 32 | frcvorg | 按收货组织 | bpchar | 1 |  | √ | ' ' | 按收货组织 |
| 33 | fdatasrc2 | 采购方数据范围 | bpchar | 1 |  | √ | ' ' | 采购方数据范围,枚举: 1 :采购入库单(含退货) |
| 34 | fsettleorg | 按核算组织 | bpchar | 1 |  | √ | ' ' | 按核算组织 |
| 35 | fhavefinish | 订单发货状态 | bpchar | 1 |  | √ | ' ' | 订单发货状态,枚举: 1 :部分发货即可对账 2 :整单发货才能对账 |
| 36 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 37 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 38 | fpoentryid | 按订单分录行 | bpchar | 1 |  | √ | ' ' | 按订单分录行 |
| 39 | finvupamount | 发票金额上限 | numeric | 19 | 6 | √ | 0.000000 | 发票金额上限 |
| 40 | fupamount | 每张对账单金额上限 | numeric | 19 | 6 | √ | 0.000000 | 每张对账单金额上限 |
| 41 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 42 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 43 | fproject | 按项目号 | bpchar | 1 |  | √ | ' ' | 按项目号 |
| 44 | fpobillno | 按订单号 | bpchar | 1 |  | √ | ' ' | 按订单号 |
| 45 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 46 | funit | 按计量单位 | bpchar | 1 |  | √ | ' ' | 按计量单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_chkscheme_fnumber |  | fnumber |
| 2 | t_pur_chkscheme_pkey |  | fid |
| 3 | idx_t_pur_chkscheme_master |  | fmasterid |
| 4 | idx_pur_chkscheme_fmasterid |  | fmasterid |
| 5 | idx_t_pur_chkscheme_createorg |  | fcreateorgid |

---

## 对账方案-分表 t_pur_chkscheme_a

- **表名称：** 对账方案-分表
- **表名：** t_pur_chkscheme_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 7 | fdisablerid | fdisablerid | int8 | 64 |  | √ | 0 |  |
| 8 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_chkscheme_a_pkey |  | fid |
| 2 | idx_pur_chkscheme_fcreatetime |  | fcreatetime |

---

## 核算组织范围-多选基础资料表 t_pur_chkscheme_org

- **表名称：** 核算组织范围-多选基础资料表
- **表名：** t_pur_chkscheme_org

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
| 1 | idx_pur_chkscheme_org_fid |  | fid,fbasedataid |
| 2 | t_pur_chkscheme_org_pkey |  | fpkid |

---

## 对账方案-使用范围位图表 t_pur_chkscheme_m

- **表名称：** 对账方案-使用范围位图表
- **表名：** t_pur_chkscheme_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_chkscheme_m |  | forgid |

---

## 对账方案-多语言表 t_pur_chkscheme_l

- **表名称：** 对账方案-多语言表
- **表名：** t_pur_chkscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_chkscheme_l_pkey |  | fpkid |
| 2 | idx_pur_chkscheme_l_fid |  | fid,flocaleid |

---

## 采购类型范围(入库单)-多选基础资料表 t_pur_chkscheme_inv

- **表名称：** 采购类型范围(入库单)-多选基础资料表
- **表名：** t_pur_chkscheme_inv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 协同辅助资料 pbd_mallextdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_chkscheme_inv_fid |  | fbasedataid |
| 2 | t_pur_chkscheme_inv_pkey |  | fpkid |

---

## 采购类型范围(收货单)-多选基础资料表 t_pur_chkscheme_rcv

- **表名称：** 采购类型范围(收货单)-多选基础资料表
- **表名：** t_pur_chkscheme_rcv

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 协同辅助资料 pbd_mallextdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_chkscheme_rcv_pkey |  | fpkid |
| 2 | idx_pur_chkscheme_rcv_fid |  | fid,fbasedataid |
