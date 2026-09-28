# 规则取数主表-bdtaxr_rule_fetch_main

## 规则取数主表-主表 t_bdtaxr_rulefetch_main

- **表名称：** 规则取数主表-主表
- **表名：** t_bdtaxr_rulefetch_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdraftid | 底稿id | int8 | 64 |  | √ | 0 | 底稿id |
| 3 | fdatastatus | 数据状态 | varchar | 50 |  | √ | '1' | 数据状态,枚举: 0 :临时数据 1 :正式数据 |
| 4 | ftemplateid | 模板id | int8 | 64 |  | √ | 0 | 模板id |
| 5 | fskssqz | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fpurpose | 用途 | varchar | 50 |  | √ | ' ' | 用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 11 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 12 | fskssqq | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rulefetch_main_union1 |  | forgid,fskssqq,fskssqz,ftemplateid |
| 2 | pk_bdtaxr_rulefetch_main |  | fid |
