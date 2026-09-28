# 计税明细表-bdtaxr_tax_details

## 计税明细表-主表 t_bdtaxr_tax_details

- **表名称：** 计税明细表-主表
- **表名：** t_bdtaxr_tax_details

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdraftid | 底稿编制id | int8 | 64 |  | √ | 0 | 底稿编制id |
| 3 | ftemplateid | 模板id | int8 | 64 |  | √ | 0 | 模板id |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 7 | fintervalrateamount | 各区间税额 | numeric | 23 | 10 | √ | 0 | 各区间税额 |
| 8 | fdraftpurpose | 底稿用途 | varchar | 50 |  | √ | ' ' | 底稿用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 9 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 10 | ftaxcodetype | 税码结果类型 | int8 | 64 |  | √ | 0 | [税码明细结果类型 bastax_code_detailstype](../bastax_files/bastax_code_detailstype.md) |
| 11 | fdatastatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: 0 :临时数据 1 :正式数据 |
| 12 | fintervalamount | 各区间金额 | numeric | 23 | 10 | √ | 0 | 各区间金额 |
| 13 | ftaxratetype | 税率类型 | int8 | 64 |  | √ | 0 | [税率类型 bd_taxratetype](../basedata_files/bd_taxratetype.md) |
| 14 | frange | 区间 | varchar | 50 |  | √ | ' ' | 区间 |
| 15 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 16 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 17 | freportkey | 报表项key | varchar | 200 |  | √ | ' ' | 报表项key |
| 18 | fisupgrade | fisupgrade | bpchar | 1 |  | √ | '0' |  |
| 19 | ftaxtype | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_tax_details |  | fid |
| 2 | idx_bdtaxr_taxdet_col |  | forgid,ftaxationsys,ftaxtype,ftaxareagroup |
