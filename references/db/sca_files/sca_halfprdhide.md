# 期初半成品结构单-隐藏-sca_halfprdhide

## 期初半成品结构单-隐藏-主表 t_sca_halfprdhide

- **表名称：** 期初半成品结构单-隐藏-主表
- **表名：** t_sca_halfprdhide

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fperiodid | 会计期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fauxpropid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | 'A' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fmaterialid | 产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | ftotalamount | 单位实际成本 | numeric | 23 | 10 | √ | 0.0000000000 | 单位实际成本 |
| 11 | fprdorgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | frootid | frootid | int8 | 64 |  | √ | 0 |  |
| 16 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | [成本主体 cal_bd_costaccount](../cal_files/cal_bd_costaccount.md) |
| 17 | fisimport | fisimport | int8 | 64 |  | √ | 0 |  |
| 18 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 19 | fstorageorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | flot | 批号 | varchar | 100 |  | √ | ' ' | 批号 |
| 21 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sca_halfprdhide |  | fid |
| 2 | idx_sca_halfprdhidemat |  | fmaterialid,fmaterialversionid,fauxpropid |
| 3 | idx_sca_halfprdhide |  | fcostaccountid,fprdorgid,fperiodid |

---

## 期初半成品结构单-隐藏-多语言表 t_sca_halfprdhide_l

- **表名称：** 期初半成品结构单-隐藏-多语言表
- **表名：** t_sca_halfprdhide_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  |  | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | 'ZH_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sca_halfprdhide_l |  | fpkid |
| 2 | idx_sca_halfprdhide_l |  | fid |

---

## 单据体-子表 t_sca_halfprdhideentry

- **表名称：** 单据体-子表
- **表名：** t_sca_halfprdhideentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 单耗数量 | numeric | 23 | 10 | √ | 0.0000000000 | 单耗数量 |
| 3 | fsublot | fsublot | varchar | 100 |  | √ | ' ' |  |
| 4 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 5 | fisleaf | 是否叶子节点 | varchar | 1 |  | √ | '1' | 是否叶子节点 |
| 6 | fisunabsorb | 来源未吸收 | varchar | 2 |  | √ | ' ' | 来源未吸收,枚举: B :是 A :否 |
| 7 | ftmptotalamt | tmptotalamt | numeric | 23 | 10 | √ | 0.0000000000 | tmptotalamt |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | famountcoeff | 金额系数 | numeric | 23 | 10 | √ | 0.0000000000 | 金额系数 |
| 10 | famount | 单耗金额 | numeric | 23 | 10 | √ | 0.0000000000 | 单耗金额 |
| 11 | felement | 成本要素 | int8 | 64 |  | √ | 0 | [成本要素 cad_element](../basedata_files/cad_element.md) |
| 12 | fsubmaterialversionid | 子项物料版本 | int8 | 64 |  | √ | 0 | [物料版本（作废） bd_materialversion](../basedata_files/bd_materialversion.md) |
| 13 | fvrtdionno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 14 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 15 | fqtycoeff | fqtycoeff | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 16 | fsubmaterialauxpropid | 子项物料辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 17 | ftreepath | 树路径 | varchar | 2000 |  | √ | ' ' | 树路径 |
| 18 | fsubmaterialid | 子项物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 19 | fissprit | 是否被拆 | bpchar | 1 |  | √ | '0' | 是否被拆 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sca_halfprdhideentry |  | fentryid |
| 2 | idx_sca_halfprdhideentrymat |  | fsubelementid,fsubmaterialid |
| 3 | idx_sca_halfprdhideentry |  | fid,fentryid |
