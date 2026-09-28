# 显示方案-ssm_displayscheme

## 显示方案-主表 t_ssm_displayscheme

- **表名称：** 显示方案-主表
- **表名：** t_ssm_displayscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fstockoutmaterial | 仅显示缺货物料 | bpchar | 1 |  | √ | '0' | 仅显示缺货物料 |
| 4 | fhideblankcol | 隐藏计划空白列 | bpchar | 1 |  | √ | '0' | 隐藏计划空白列 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | funittype | 计量单位 | varchar | 50 |  | √ | ' ' | 计量单位,枚举: baseunit :以基本单位显示 purchaseunit :以采购单位显示 |
| 7 | fdisplayqty | 以净需求数量显示 | bpchar | 1 |  | √ | '0' | 以净需求数量显示 |
| 8 | fexporteditemcontrol | 引出字段控制 | varchar | 500 |  | √ | ' ' | 引出字段控制,枚举: 10 :采购组织 11 :采购计划协议 12 :协议起始日期 13 :协议截止日期 14 :订货供应商 15 :订货联系人 16 :订货联系电话 17 :订货联系地址 18 :供货供应商 19 :供货联系人 20 :供货联系电话 21 :供货联系地址 22 :计划类型 23 :计划生成时间 24 :发送状态 25 :发送时间 100 :物料编码 101 :物料名称 102 :规格型号 103 :物料版本 104 :辅助属性 105 :交货地址 106 :采购单位 107 :累计收货数量 108 :在途数量 109 :欠货数量 110 :计划类型 111 :发放号 112 :滚动收货计划发放号 113 :供应商交货计划发放号 114 :供应商预测计划发放号 |
| 9 | fdefaultscheme | 默认方案 | varchar | 50 |  | √ | ' ' | 默认方案,枚举: 0 :是 1 :否 |
| 10 | fschemename | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 11 | fdisplaycontrol | 显示控制 | varchar | 50 |  | √ | ' ' | 显示控制,枚举: 0 :行号 1 :发放号 2 :状态 3 :日志编号 4 :计划类型 6 :在途数量 5 :累计已入库数量 |
| 12 | fdisplayplandetail | 显示计划明细 | bpchar | 1 |  | √ | '0' | 显示计划明细 |
| 13 | fmaterialinfoconfig | 物料信息 | varchar | 50 |  | √ | ' ' | 物料信息,枚举: 0 :物料编码 1 :物料名称 2 :规格型号 3 :物料版本 4 :辅助属性 |
| 14 | fproductionorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fplantype | 计划类型 | varchar | 50 |  | √ | ' ' | 计划类型,枚举: 0 :滚动收货计划 1 :供应商交货计划 2 :供应商预测计划 3 :供应商交货+供应商预测（合并显示） 4 :供应商交货+供应商预测（独立显示） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ssm_displayscheme |  | fid |
| 2 | idx_ssm_displayscheme_m0 |  | fdisplaycontrol |
