# 代扣代缴税收缴款凭证-tdm_withholding_tax

## 代扣代缴税收缴款凭证-主表 t_tdm_withholding_tax

- **表名称：** 代扣代缴税收缴款凭证-主表
- **表名：** t_tdm_withholding_tax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ftaxcode | 凭证编号 | varchar | 200 |  | √ | ' ' | 凭证编号 |
| 8 | fsigndate | 填发日期 | timestamp | 0 |  |  | null | 填发日期 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | ftaxpayername | 纳税人名称 | varchar | 50 |  | √ | ' ' | 纳税人名称 |
| 11 | famount | 金额合计 | numeric | 23 | 10 | √ | 0.0000000000 | 金额合计 |
| 12 | fsourcesys | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fsignname | 填票人 | varchar | 50 |  | √ | ' ' | 填票人 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fperiod | 抵扣属期 | timestamp | 0 |  |  | null | 抵扣属期 |
| 17 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: 1 :手工新增 2 :模板导入 3 :系统同步 |
| 18 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | ' ' | 生成凭证 |
| 19 | ftaxoffice | 税务机关 | varchar | 50 |  | √ | ' ' | 税务机关 |
| 20 | fofficetax | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | ftaxpayernumber | 纳税人识别号 | varchar | 50 |  | √ | ' ' | 纳税人识别号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_withholding_tax |  | forgid |
| 2 | pk_tdm_withholding_tax |  | fid |

---

## 明细行-子表 t_tdm_withholding_items

- **表名称：** 明细行-子表
- **表名：** t_tdm_withholding_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxcategory | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 3 | factualpayment | 实缴金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实缴金额 |
| 4 | forigintaxcode | 原凭证号 | varchar | 50 |  | √ | ' ' | 原凭证号 |
| 5 | fstart | 税款所属期起 | timestamp | 0 |  |  | null | 税款所属期起 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fend | 税款所属期止 | timestamp | 0 |  |  | null | 税款所属期止 |
| 8 | finputdate | 入库日期 | timestamp | 0 |  |  | null | 入库日期 |
| 9 | fitemname | 品目名称 | varchar | 50 |  | √ | ' ' | 品目名称 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ftaxtype | 税种 | varchar | 30 |  | √ | ' ' | 税种,枚举: zzs :增值税 qysds :企业所得税 cswhjss :城市维护建设税 jyffj :教育费附加 dfjyffj :地方教育附加 xfs :消费税 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tdm_withholding_items |  | fentryid |
| 2 | idx_tdm_withholding_items_fk |  | fid |
