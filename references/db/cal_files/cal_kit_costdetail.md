# 套件父项成本表-cal_kit_costdetail

## 套件父项成本表-主表 t_cal_kitcostdetail

- **表名称：** 套件父项成本表-主表
- **表名：** t_cal_kitcostdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisfivoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 12 | fcostrecordid | 核算成本记录单据ID | int8 | 64 |  | √ | 0 | 核算成本记录单据ID |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 15 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 16 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 18 | fcurrencyid | 交易币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_kitcostdetail |  | fid |
| 2 | idx_cal_kitcostdetail_billno |  | fbillno |

---

## 单据体-子表 t_cal_kitcostdetailentry

- **表名称：** 单据体-子表
- **表名：** t_cal_kitcostdetailentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassistpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | funitactualcost | 单位实际成本 | numeric | 23 | 10 | √ | 0 | 单位实际成本 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fmversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 9 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fproducttype | 产品类别 | varchar | 30 |  | √ | ' ' | 产品类别,枚举: kitparent :套件父项 kitchild :套件子项 |
| 11 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fkitsettleway | 套件内部结算方式 | varchar | 50 |  | √ | ' ' | 套件内部结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 14 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 15 | fownerid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | factualcost | 实际成本 | numeric | 23 | 10 | √ | 0 | 实际成本 |
| 17 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 18 | fownertype | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :核算组织 bd_supplier :供应商 bd_customer :客户 |
| 19 | fsuitesettletype | 套件结算方式 | varchar | 50 |  | √ | ' ' | 套件结算方式,枚举: kitparent :父项结算 kitchild :子项结算 |
| 20 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 21 | flot | 批号 | varchar | 510 |  | √ | ' ' | 批号 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 23 | fsuitedeliverytype | 套件发货方式 | varchar | 50 |  | √ | ' ' | 套件发货方式,枚举: kitdeliver :成套发货 nonkitdeliver :非成套发货 kitreturn :成套退货 nonkitreturn :非成套退货 |
| 24 | fbizbillentryid | 业务单据分录Id | int8 | 64 |  | √ | 0 | 业务单据分录Id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_kitcostdetailentry |  | fentryid |
| 2 | idx_cal_kitcostdetailentry_fid |  | fid |
| 3 | idx_cal_kitcostdetailentry_fparentrowid |  | fparentrowid |
| 4 | idx_cal_kitcostdetailentry_fmaterialid |  | fmaterialid |
