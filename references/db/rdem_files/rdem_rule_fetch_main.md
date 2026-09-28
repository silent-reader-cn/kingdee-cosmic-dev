# 规则取数主表-rdem_rule_fetch_main

## 规则取数主表-主表 t_rdem_rulefetch_main

- **表名称：** 规则取数主表-主表
- **表名：** t_rdem_rulefetch_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatastatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: 0 :临时数据 1 :正式数据 |
| 3 | ftemplateid | 模板id | int8 | 64 |  | √ | 0 | 模板id |
| 4 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fskssqz | 所属税期.结束 | timestamp | 0 |  |  | null | 所属税期.结束 |
| 7 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | ftaxsystem | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 10 | fpurpose | 用途 | varchar | 50 |  | √ | ' ' | 用途,枚举: nssb :纳税申报 sjjt :税金计提 |
| 11 | fskssqq | 所属税期.开始 | timestamp | 0 |  |  | null | 所属税期.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rdem_rulefetch_main |  | fid |
| 2 | idx_rdem_rulefetch_main_m0 |  | ftaxareagroup |
