# 参考税负率-tdm_ref_taxrate

## 参考税负率-主表 t_tdm_ref_taxrate

- **表名称：** 参考税负率-主表
- **表名：** t_tdm_ref_taxrate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 3 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fminrate | 最小税负率 | numeric | 23 | 10 | √ | 0 | 最小税负率 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fexpdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 8 | fmaxrate | 最大税负率 | numeric | 23 | 10 | √ | 0 | 最大税负率 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | ftaxationsys | 税收制度 | int8 | 64 |  | √ | 0 | 税收制度 bd_taxationsys |
| 11 | ftaxcategory | 税种 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | 税收辖区 bastax_taxareagroup |
| 16 | findustrycode | 行业 | int8 | 64 |  | √ | 0 | 行业代码及名称 tpo_tcvat_industrycode |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 200 |  | √ | ' ' | 编码 |
| 19 | favgrate | 平均税负率 | numeric | 23 | 10 | √ | 0 | 平均税负率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_refrate_num |  | fnumber |
| 2 | pk_tdm_ref_taxrate |  | fid |

---

## 参考税负率-多语言表 t_tdm_ref_taxrate_l

- **表名称：** 参考税负率-多语言表
- **表名：** t_tdm_ref_taxrate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tdm_ref_taxrate_l_0 |  | fid,flocaleid |
| 2 | pk_tdm_ref_taxrate_l |  | fpkid |
